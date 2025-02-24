# Example Feedback 1

Output only the json:

Feedback = """
I am very disappointed with the delivery of my new laptop. 
The package arrived damaged, and I urgently need a solution 
as I need the computer for work. The quality of the 
packaging was inadequate.
"""

# LLM Output
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
