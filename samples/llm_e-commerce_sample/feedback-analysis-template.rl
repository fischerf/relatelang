Remember this:

# 1. Analysis Structure Definition
define FeedbackAnalysis as "Analysis of customer feedback".
FeedbackAnalysis has required_aspects of [
    "sentiment",
    "main_topic",
    "urgency",
    "product_related",
    "service_related"
].

# 2. Evaluation Criteria Definition
define Sentiment as "Feedback sentiment".
Sentiment has possible_values of ["positive", "neutral", "negative"].
Sentiment has confidence_score of number.

define Topic as "Main topic of feedback".
Topic has categories of [
    "product_quality",
    "delivery",
    "customer_service",
    "user_experience",
    "price"
].

define Urgency as "Processing urgency".
Urgency has levels of ["high", "medium", "low"].

# 3. Output Structure Definition
define AnalysisOutput as "Structured analysis output".
AnalysisOutput has format of "json".
AnalysisOutput has required_fields of FeedbackAnalysis has required_aspects.
AnalysisOutput has confidence_threshold of 0.7.

# 4. Processing Rules
if Feedback contains "immediately" or "urgent",
    then ensure Urgency has level of "high".

if Sentiment has confidence_score < AnalysisOutput has confidence_threshold,
    then ensure AnalysisOutput has flag of "review_needed".

# 5. Action Rules
if Urgency has level of "high",
    then ensure Action is "escalate_to_support".

if Topic has category of "product_quality" and Sentiment is "negative",
    then ensure Action is "forward_to_quality_team".

# 6. Expected LLM Output Example
define ExpectedResponse as "Format of LLM response".
ExpectedResponse has structure of {
    "sentiment": {
        "value": "Sentiment has value",
        "confidence": "Sentiment has confidence_score"
    },
    "main_topic": "Topic has category",
    "urgency": "Urgency has level",
    "product_related": "boolean",
    "service_related": "boolean",
    "actions_required": ["Action"],
    "confidence_flags": ["review_needed"] if applicable
}.

# 7. Validation Rules
ensure AnalysisOutput contains all FeedbackAnalysis has required_aspects.
ensure AnalysisOutput has format matches ExpectedResponse has structure.
ensure Sentiment has confidence_score is number between 0 and 1.