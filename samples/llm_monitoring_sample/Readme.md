1. Add the URL of your LLM-Service to log-monitor.py:

```plaintext
url = "https://api.xxx"
```

2. Add the API-Key of your LLM-Service to log-monitor.py:

```plaintext
"api-key": "12345"
```

3. Start monitoring:

> python log-monitor.py

4. Generate log entries in log/application.log

5. A llm feedback notification should be generated in the notifications/ folder which can be send via eMail to your support team.
