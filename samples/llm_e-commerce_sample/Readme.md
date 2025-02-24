## Feedback-Analysis-System

The rules of our Feedback-Analysis-System are defined in ```feedback-analysis-template.rl```.

1. Pass the content ```feedback-analysis-template.rl``` to your llm as context.

2. Now you can pass feedback to your llm and it generates a structured analysis output, which you can then process further.

```plaintext
Output only the json:

Feedback = """
I am very disappointed with the delivery of my new laptop. 
The package arrived damaged, and I urgently need a solution 
as I need the computer for work. The quality of the 
packaging was inadequate.
"""
```

3. Expected output:

```plaintext
{
    "sentiment": {
        "value": "negative",
        "confidence": 0.92
    },
    "main_topic": "delivery",
    "urgency": "high",
    "product_related": true,
    "service_related": true,
    "actions_required": [
        "escalate_to_support",
        "forward_to_quality_team"
    ]
}
```

## The advantages of this structure are:

1. **Consistency**: The LLM is required to analyze the same aspects every time and respond in a predefined format.

2. **Validability**: The output can be automatically checked against the defined rules.

3. **Automation**: Automatic actions can be triggered based on the structured analysis.

4. **Scalability**: The system can be easily extended with new aspects or rules.

The main difference from a regular prompt like "Analyze this feedback and tell me what to do" lies in the:
- Structured output
- Guaranteed completeness of analysis
- Possibility for automatic processing
- Consistency across multiple analyses
