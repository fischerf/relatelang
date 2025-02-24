import os
import time
import re
import json
import requests
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from typing import Dict, List, Optional

class LogMonitor(FileSystemEventHandler):
    def __init__(self, log_file: str, output_dir: str):
        self.log_file = os.path.abspath(log_file)
        self.output_dir = os.path.abspath(output_dir)
        self.last_position = 0
        
        print("\n[INIT] Initializing LogMonitor...")
        print(f"[INIT] Log file path: {self.log_file}")
        print(f"[INIT] Output directory: {self.output_dir}")
        
        # Create log file if it doesn't exist
        log_dir = os.path.dirname(self.log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"[INIT] Created log directory: {log_dir}")
        
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                pass
            print(f"[INIT] Created empty log file: {self.log_file}")
        else:
            with open(self.log_file, 'r') as f:
                f.seek(0, 2)
                self.last_position = f.tell()
            print(f"[INIT] Using existing log file, last position: {self.last_position}")
    
    def parse_log_entry(self, line: str) -> Optional[Dict]:
        """Parse a log line into structured data."""
        pattern = r'\[(.*?)\] \[(WARNING|ERROR)\] \[(.*?)\] (.*)'
        match = re.match(pattern, line.strip())
        
        if match:
            timestamp, level, component, message = match.groups()
            entry = {
                "timestamp": timestamp,
                "severity": level,
                "component": component,
                "message": message,
                "stack_trace": "",
                "metrics": {}
            }
            print(f"\n[PARSE] Found {level} log entry:")
            print(f"[PARSE] Timestamp: {timestamp}")
            print(f"[PARSE] Component: {component}")
            print(f"[PARSE] Message: {message}")
            return entry
        return None

    def get_RelateLang_template(self, severity: str) -> str:
        """Load and return the appropriate RelateLang template based on severity."""
        template_file = os.path.join("", "mon_template.rl")
        
        try:
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Split content into sections by headers
            templates = {}
            current_section = None
            current_content = []
            
            for line in content.split('\n'):
                if line.startswith('[') and line.endswith(']'):
                    if current_section:
                        templates[current_section] = '\n'.join(current_content).strip()
                    current_section = line.strip('[]')
                    current_content = []
                else:
                    current_content.append(line)
                    
            # Add the last section
            if current_section:
                templates[current_section] = '\n'.join(current_content).strip()
            
            # Return the appropriate template
            return templates.get(severity, "")
        except Exception as e:
            print(f"[ERROR] Failed to load template file: {str(e)}")
            return ""
        finally:
            if f is not None:
                f.close()

    def process_log_entry(self, entry: Dict):
        """Process a single log entry using RelateLang and LLM."""
        print(f"\n[PROCESS] Starting to process {entry['severity']} entry")
        
        template = self.get_RelateLang_template(entry['severity'])
        populated_template = template.format(
            timestamp=entry['timestamp'],
            severity=entry['severity'],
            severity_level=entry['severity'],
            component=entry['component'],
            message=entry['message'],
            stack_trace=entry['stack_trace'],
            system_name="Application Monitoring",
            support_email="support_team@xyz.com"
        )
        
        print("[PROCESS] Template populated with log data\n")

        final_prompt = f"""Here is an error log entry and a RelateLang template for processing it.
Please analyze this error and generate an email notification based on the template.
Output only the EMail Message!
        
RelateLang Template:
{populated_template}"""

        json_comp = json.dumps(final_prompt) #, ensure_ascii=False, indent=2)

        message = {
                    "messages": [
                      {
                        "role": "user",
                        "content": json_comp
                      }
                    ]
                }

        try:
            print("[PROCESS] Sending request to LLM...")
            url = "https://api.xxx"
            headers = {
                "Content-type": "application/json",
                "api-key": "12345"
            }
            
            # Make the POST request
            response = requests.post(url, headers=headers, json=message, timeout=5)
            print("[PROCESS] Received response from LLM")
            
            self.save_email_notification(entry, response.content)
        except Exception as e:
            print(f"[ERROR] Failed to process log entry: {str(e)}")
            print(response.status_code)
            print(response.text)

    def save_email_notification(self, entry: Dict, analysis: str):
        """Save the generated email notification to a file."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"notification_{entry['severity'].lower()}_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            # Convert byte to string if nessesary
            if isinstance(analysis, bytes):
                analysis = analysis.decode('utf-8')
                # Parse the JSON string into a Python dictionary
                parsed_data = json.loads(analysis)
                # Extract the message content
                message_content = parsed_data['choices'][0]['message']['content']

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(message_content)
            print(f"[SAVE] Successfully saved notification to: {filepath}")
        except Exception as e:
            print(f"[ERROR] Failed to save notification: {str(e)}")

    def on_modified(self, event):
        if event.src_path == self.log_file:
            print(f"\n[WATCH] Detected changes in log file: {event.src_path}")
            self.check_new_logs()

    def check_new_logs(self):
        """Check for new log entries and process them."""
        try:
            print("\n[CHECK] Checking for new log entries...")
            with open(self.log_file, 'r', encoding='utf-8') as f:
                f.seek(0, 2)
                file_size = f.tell()
                
                if self.last_position > file_size:
                    print("[CHECK] File was truncated, resetting position to start")
                    self.last_position = 0
                
                f.seek(self.last_position)
                print(f"[CHECK] Reading from position: {self.last_position}")
                
                current_entry = None
                lines_read = 0
                
                for line in f:
                    lines_read += 1
                    parsed = self.parse_log_entry(line)
                    
                    if parsed:
                        if current_entry:
                            print("[CHECK] Processing previous entry before starting new one")
                            self.process_log_entry(current_entry)
                        current_entry = parsed
                    elif current_entry and line.strip():
                        print(f"[CHECK] Adding line to stack trace: {line.strip()}")
                        current_entry['stack_trace'] += line
                
                if current_entry:
                    print("[CHECK] Processing final entry")
                    self.process_log_entry(current_entry)
                
                self.last_position = f.tell()
                print(f"[CHECK] Finished checking logs. Lines read: {lines_read}")
                if lines_read == 0:
                    print("[CHECK] No new log entries found")
                print(f"[CHECK] New file position: {self.last_position}")
                
        except Exception as e:
            print(f"[ERROR] Failed to check logs: {str(e)}")

def main():
    print("\n=== Log Monitor Starting ===\n")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_dir, "logs")
    log_file = os.path.join(log_dir, "application.log")
    output_dir = os.path.join(script_dir, "notifications")
    
    print("[SETUP] Creating required directories...")
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            pass
        print(f"[SETUP] Created empty log file: {log_file}")
    
    print(f"[SETUP] Configuration:")
    print(f"[SETUP] Log file: {log_file}")
    print(f"[SETUP] Output directory: {output_dir}")
    
    try:
        print("\n[SETUP] Initializing monitor and observer...")
        event_handler = LogMonitor(log_file, output_dir)
        observer = Observer()
        
        observer.schedule(event_handler, path=os.path.dirname(log_file), recursive=False)
        
        observer.start()
        print(f"\n[RUNNING] Started monitoring {log_file} for warnings and errors")
        print("[RUNNING] Press Ctrl+C to stop\n")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Stopping monitor (Ctrl+C received)")
        observer.stop()
    except Exception as e:
        print(f"\n[ERROR] Fatal error: {str(e)}")
        if 'observer' in locals():
            observer.stop()
    finally:
        if 'observer' in locals():
            observer.join()
            print("[SHUTDOWN] Monitor stopped")

if __name__ == "__main__":
    main()