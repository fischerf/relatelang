[ERROR]
define MonitoredSystem as "A system being monitored for errors".
MonitoredSystem has log_level of ["ERROR", "WARNING", "INFO"].
MonitoredSystem has components of ["database", "api", "frontend"].

define ErrorLog as "Log entry containing error information".
ErrorLog has timestamp of "{timestamp}".
ErrorLog has severity of "{severity}".
ErrorLog has message of "{message}".
ErrorLog has stack_trace of "{stack_trace}".
ErrorLog has component of "{component}".

define Analysis as "Error analysis result".
Analysis has problem_type of ["configuration", "resource", "code", "network"].
Analysis has severity_level of ["critical", "high", "medium", "low"].
Analysis has suggested_solution of "text".
Analysis has required_expertise of ["database", "network", "application"].

define Notification as "Error notification email".
Notification has priority of "{severity_level}".
Notification has solution_steps of "list".

relate ErrorLog and MonitoredSystem as "generated_by".
relate Analysis and ErrorLog as "analyzes".
relate Notification and Analysis as "based_on".

ensure Analysis identifies ErrorLog has problem_type.
ensure Notification includes Analysis has suggested_solution.
ensure EmailTemplate generates Notification with [[
	to: {support_email}
	priority: priority
    subject: "[severity_level] Error in {system_name}: problem_type"
    body:
    Error Details:
    - System: {system_name}
    - Component: component
    - Timestamp: timestamp
    - Severity: severity_level
    
    Message:
    message
    
    Required Expertise:
    required_expertise
    
    Action Items:
    solution_steps
    
    Stack Trace:
    {stack_trace}
]]
