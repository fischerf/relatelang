
# RelateScript: A Declarative Meta-Language for Consistent LLM Prompt Engineering


## Abstract
RelateScript is a declarative meta-language designed to streamline the creation of structured and consistent prompts for large language models (LLMs). This paper introduces RelateScript's syntax, highlighting its foundation in relational and predicate logic. By focusing on relationships, conditions, and context, RelateScript bridges the gap between natural language expressiveness and the precision required for effective LLM interaction. It facilitates a novel approach to prompt engineering, where humans and LLMs collaboratively develop structured prompts that can be easily modified and reused for diverse tasks, enhancing the reliability and automation capabilities of LLM-driven workflows.

---

## 1. Introduction
In the rapidly evolving field of large language models (LLMs), the effectiveness of interactions heavily relies on the quality of prompts. Traditional imperative programming languages often impose rigid structures that contrast with the nuanced and context-sensitive nature of human reasoning. While natural language offers unparalleled flexibility for interacting with LLMs, it can lead to ambiguity and inconsistency in prompt outputs. To address these challenges, we introduce RelateScript, a declarative meta-language specifically designed for crafting structured prompts. RelateScript enables users to define entities, relationships, and conditions in a format that is both readable and logically precise. RelateScript is not intended as a traditional programming language with a separate parser, but rather as a structured input format that leverages the inherent understanding capabilities of LLMs.

### 1.1 Motivation
RelateScript addresses the growing need for a more systematic and reliable approach to prompt engineering. As LLMs become increasingly sophisticated, the ability to articulate complex instructions and define precise conditions becomes crucial for harnessing their full potential. RelateScript provides an accessible and intuitive way of describing relationships and dependencies between entities, enabling users to express intricate logic in a manner that aligns closely with human reasoning. With a syntax designed for readability, RelateScript empowers users to generate consistent prompts, making it particularly suited for building reusable prompt templates that can be adapted for different scenarios, thus enhancing the efficiency and reliability of LLM interactions. It also allows for combining the strengths of human domain knowledge with the structure of a logical form.

---

## 2. Language Design

### 2.1 Syntax
The syntax of RelateScript emphasizes natural language structure, allowing for readable declarations of entities, relationships, and conditions. Its main constructs include:
- **Definitions**: `define <Entity> as <Description>.`
- **Predicates**: `<Entity> is <Predicate>.`
- **Attributes**: `<Entity> has <Attribute> of <Value>.`
- **Relations**: `relate <Entity1> and <Entity2> as <RelationType> [ if <Condition> ].`
- **Conditions**: `if <Condition>, then <Action>.`
- **Goals**: `ensure <Goal>.`

### 2.2 Example

A prompt with compound instructions and multi-level logic.

```plaintext
define City as "A collection of buildings and people".
Berlin is a City.
Berlin has Population of 3_500_000.
define Metropolis as "A city with more than 1_000_000 inhabitants".

if City has Population > 1_000_000,
    then ensure City is a Metropolis.
```

Expected Behavior: The LLM should recognize that Berlin is a "Metropolis" because its population is greater than 1,000,000.

> more [Samples](/samples/)

### 2.3 eBNF Grammar
The following Extended Backus-Naur Form (eBNF) defines RelateScript's syntax:

```ebnf
program          ::= { statement } ;
statement        ::= definition | predicate | attribute | relation | condition | goal ;
definition       ::= "define" entity "as" string "." ;
predicate        ::= entity "is" predicate_value "." ;
attribute        ::= entity "has" attribute_name "of" attribute_value "." ;
relation         ::= "relate" entity "and" entity "as" relation_type [ "if" condition ] "." ;
condition        ::= "if" condition_expr ", then" action "." ;
goal             ::= "ensure" goal_expr "." ;
condition_expr   ::= entity predicate_operator predicate_value 
                     | entity attribute_operator attribute_value 
                     | entity relation_operator entity ;
goal_expr        ::= entity relation_type entity ;
action           ::= "ensure" goal_expr ;
entity           ::= identifier ;
predicate_value  ::= identifier ;
attribute_name   ::= identifier ;
attribute_value  ::= identifier | number ;
relation_type    ::= string ;
predicate_operator ::= "is" | "is not" ;
attribute_operator ::= "has" | "does not have" ;
relation_operator  ::= "relates to" | "does not relate to" ;
identifier       ::= letter { letter | digit | "_" } ;
letter           ::= "a" | "b" | " ..." | "z";
string           ::= '"' { character } '"' ;
number           ::= digit { digit } ;
character        ::= lowercase-char | uppercase-char | digit | special-char;
lowercase-char   ::= "a" | "b" | "..." | "z";
uppercase-char   ::= "A" | "B" | "..." | "Z";
special-char     ::= "-" | "_";
digit            ::= "0" | "1" | "..." | "9";
```

### 2.4 Explanations of the rules

1. **Main structure (`program`)**: A program (prompt) consists of a sequence of `statements`, each of which defines a particular piece of information, relationship or statement.

2. **Statements**:
- **Definition** (`definition`): Defines an entity with a name and a description.
- **Predicate** (`predicate`): Assigns a property or state to an entity.
- **Attributes** (`attribute`): Associates an entity with an attribute and a value.
- **Relationships** (`relation`): Defines a relationship between two entities, optionally with a condition.
- **Conditions** (`condition`): Defines a condition and a resulting action.
- **Goals** (`goal`): Describes a goal that is to be achieved.

3. **Expression rules**:
- **condition expressions** (`condition_expr`): Check relationships or properties between entities.
- **Goal expressions** (`goal_expr`): Describe what is to be achieved.
- **Actions** (`action`): Relate to the goal that is to be fulfilled.

4. **Basic structures**:
- `entity`, `predicate_value`, `attribute_name`, `attribute_value` and `relation_type` are basic components represented by identifiers (e.g. names) or values (such as numbers).

5. **Operators**:
- `predicate_operator`, `attribute_operator`, and `relation_operator` define the type of relationships or conditions, e.g. “is”, “has”, “relates to”.

6. **Terminals**:
- `identifier` represents names and must begin with a letter.
- `string` stands for text and is enclosed in quotation marks.

---

## 3. Combining RelateScript and Natural Language

RelateScript offers a structured, logic-driven framework that seamlessly complements natural language-based prompting approaches. While natural language excels in conveying nuance and ambiguity, particularly for creative tasks, RelateScript provides clarity, precision, and logical consistency—essential qualities for complex and multi-step interactions with LLMs.

### 3.1 **Integration with Natural Language Prompting**
RelateScript can be effectively paired with natural language inputs to combine the strengths of both methods:

- **Natural Language**:  Sets the context, describes abstract ideas, and initiates creative exploration through flexible phrasing.
- **RelateScript**: Ensures logical rigor by explicitly defining entities, relationships, and conditional rules within a structured template.

For example, a user might begin with a natural language prompt such as:  
*"Help me build a sales model. Start by making basic assumptions about customers and products."*  

This context can then be supported by a RelateScript block:  
```plaintext
define Product as "A product for sale".
Product is available.
Product has price of 100.
Product has category of "Electronics".

define Customer as "A person who wants to buy a product".
Customer has budget of 150.

relate Customer and Product as "buys" if Product is available and Customer has budget of 150.

ensure Customer buys Product.
```

This combination allows LLMs to leverage the intuitive and context-rich setup of natural language while adhering to the logical structure and precision of RelateScript.

### 3.2 **Complementing LLM Prompting Techniques**
RelateScript aligns with advanced prompting techniques for LLMs, such as:
1. **Logical and Sequential Processing**: By explicitly structuring steps and conditions, RelateScript mirrors techniques like Chain-of-Thought (CoT) prompting, enhancing the LLM's ability to reason through multi-step tasks.
2. **Specificity and Targeting**: RelateScript's declarative syntax inherently reduces ambiguity, making it particularly suited for Target-your-response (TAR) prompts or goal-driven interactions.
3. **Contextual Understanding**: The structured representation of relationships and dependencies enables LLMs to maintain coherent outputs across context-rich or multi-step scenarios.

### 3.3 **Applications and Limitations**
RelateScript is ideal for tasks requiring:
- Precise execution of logical rules and conditions.
- Modeling of structured systems like workflows, decision trees, or knowledge graphs.
- Creating reusable prompt templates for consistent LLM interactions.

However, natural language remains superior for:
- Creative, open-ended tasks where ambiguity or nuance is a feature, not a limitation.
- Rapid prototyping of ideas without requiring formalized structures.

### 3.4 **Recommendation**
The most effective use of RelateScript lies in its hybrid application, where it acts as a supplement to natural language inputs. This approach allows users to balance creativity and logical consistency, enabling LLMs to handle a wider range of tasks with both precision and adaptability. We advocate for an iterative workflow where RelateScript prompts are continuously refined based on LLM feedback, leading to increasingly effective and reliable interactions.

---

## 4. Comparison with Existing Languages

Several languages and frameworks offer relational, declarative, or context-sensitive capabilities. Here, we compare RelateScript to similar systems.

### 4.1 Prolog
**Prolog** is a logic programming language commonly used in AI. It uses facts and rules to derive new information.
- **Similarity**: Both languages use declarative structures to represent relations.
- **Difference**: Prolog's syntax and predicate logic make it less readable for non-technical users.

### 4.2 Datalog
**Datalog** is a simplified version of Prolog, used for database queries and logical reasoning.
- **Similarity**: Datalog’s focus on facts and rules aligns with RelateScript's relational approach.
- **Difference**: Datalog lacks natural language readability and context-sensitive features.

### 4.3 SPARQL and RDF
**SPARQL** and **RDF** model data as a graph of subject-predicate-object relationships, often for the semantic web.
- **Similarity**: Both use declarative syntax to express relationships.
- **Difference**: SPARQL and RDF are tailored for distributed knowledge bases, not flexible programming.

### 4.4 Description Logic (DL)
**Description Logic** is a formal language for knowledge representation in ontologies.
- **Similarity**: Both use logical relations to define entities and their attributes.
- **Difference**: Description Logic's formalism is more complex and less natural for general programming.

### 4.5 Rules Engines (e.g., Drools)
**Rules Engines** use declarative rules for automated decision-making in business applications.
- **Similarity**: They support `if-then` logic, like RelateScript’s conditions and goals.
- **Difference**: Rules engines are often restricted to business applications and lack RelateScript’s flexible syntax.

---

## 5. Applications

RelateScript’s structure is ideal for:
- **AI Systems**: Defining context-aware rules for automated reasoning.
- **Knowledge Representation**: Modeling entities, attributes, and relationships within a specific domain.
- **Decision-Making Systems**: Using goals and conditions to dynamically adjust program behavior.

### 5.1 Advantages of RelateScript for an LLM
1. **Clarity and Precision**: RelateScript is clearly structured, with defined rules and terms. This reduces the ambiguity often found in natural language and ensures that the LLM correctly interprets the intended meaning.
  
2. **Clear Relationships and Conditions**: The declarative structure of RelateScript is particularly suited to explicitly formulate connections and conditions. This can help an LLM draw conclusions or coordinate sequential steps.

3. **Reduced Interpretation**: Since RelateScript is based on a logical grammar, the "interpretation work" for an LLM is often easier. It requires less contextual understanding of the language itself and can focus on the instructions.

### 5.2 Limitations of RelateScript Compared to Natural Language
1. **Comprehensibility and Accessibility**: For many users, natural language is more intuitive and easier to use, as it requires no specific structure or defined syntax. This is an advantage when the instructions for the LLM are created by non-programmers.

2. **Flexibility and Expressiveness**: Natural language is much more flexible and can convey complex, nuanced instructions that are harder to express in a highly structured system like RelateScript. Examples include metaphors, vague terms, or context descriptions common in human communication.

3. **Processing Capability of LLMs**: Modern LLMs like GPT-4 are designed to understand natural language and process it contextually. They are often already capable of interpreting complex instructions without requiring a formalized language. In many cases, LLMs understand natural language accurately enough, so RelateScript offers fewer advantages.

---

## 6. Scenarios

### 6.1 Scenario 1:

Evaluate employee performance based on specific criteria and assign performance ratings.

```plaintext
define Employee as "A person employed by the company".
Employee has name of "John Doe".
Employee has performance_score of 85.

define Performance_Rating as "A rating given to employees based on performance score".
Performance_Rating has value of "Excellent" if Employee has performance_score >= 90.
Performance_Rating has value of "Good" if Employee has performance_score >= 75 and Employee has performance_score < 90.
Performance_Rating has value of "Average" if Employee has performance_score >= 50 and Employee has performance_score < 75.
Performance_Rating has value of "Needs Improvement" if Employee has performance_score < 50.

relate Employee and Performance_Rating as "has_rating".

ensure Employee has_rating Performance_Rating.
```

Expected Behavior: The system should assign a performance rating to the employee based on their performance score.

You can use this as a template for other employees by simply replacing the name and rating. By providing this in a consistent format to the LLM, you can process it further with additional questions to generate analyses, letters, or other types of responses.

### 6.2 Scenario 2:

Predict sales based on historical data and market trends.

```plaintext
define Product as "A sellable item".
Product has name of "Smartphone".
Product has historical_sales of [100, 150, 200, 250, 300].

define Market_Trend as "An indicator of market conditions affecting sales".
Market_Trend has trend of "Increasing".

define Sales_Prediction as "An estimated future sales figure".
Sales_Prediction has value of 350 if Market_Trend has trend of "Increasing" and Product has historical_sales[-1] < 350.

relate Product and Sales_Prediction as "predicted_sales".

ensure Product predicted_sales Sales_Prediction.
```

Expected Behavior: The system should predict the future sales of the "Smartphone" based on the increasing market trend and the last recorded historical sales figure.

### 6.3 Scenario 3:

Manage project milestones and ensure deadlines are met.

```plaintext
define Project as "A planned undertaking involving resources and activities".
Project has name of "Website Redesign".
Project has start_date of "2023-10-01".
Project has end_date of "2023-12-31".

define Milestone as "A significant point in the project timeline".
Milestone has name of "Design Phase".
Milestone has due_date of "2023-10-31".
Milestone has status of "Not Started".

relate Project and Milestone as "includes" if Milestone has due_date <= Project has end_date.

define Deadline as "A critical date by which a task must be completed".
Deadline has date of "2023-10-31".

if Milestone has due_date = Deadline.date,
    then ensure Milestone has status of "Started".

ensure Project includes Milestone.
```

Expected Behavior: The system should recognize that the "Design Phase" milestone is part of the "Website Redesign" project and update its status to "Started" when the due date matches the deadline.

---

## 7. Conclusion

RelateScript provides a structured, declarative framework for tasks that require precision and logical consistency, making it a powerful tool in applications such as knowledge representation, decision-making, and AI systems. Its syntax emphasizes readability and ease of understanding, allowing users to convey complex conditions and objectives in a manner that resonates with natural human language.

By integrating RelateScript with natural language prompting, users can leverage the best of both worlds—combining the intuitive, creative capabilities of natural language with the rigor and repeatability of logical reasoning. This hybrid approach broadens the scope of RelateScript's applications and positions it as an essential tool for enhancing LLM-driven workflows, paving the way for more reliable, efficient, and automated interactions with large language models.

Future work could involve [testing](/test/testsuite.md) the language in real-world AI and knowledge management systems. Further research will also focus on refining the language's syntax, exploring its scalability, and addressing potential security vulnerabilities.
 
---

## Author
*By Florian Fischer*  
*https://github.com/fischerf/*

## References
1. Clocksin, W.F., & Mellish, C.S. (1981). *Programming in Prolog*. Springer-Verlag.
2. Ullman, J.D. (1988). *Principles of Database and Knowledge-Base Systems*. Computer Science Press.
3. Berners-Lee, T., Hendler, J., & Lassila, O. (2001). "The Semantic Web". *Scientific American*.
4. Baader, F., Calvanese, D., McGuinness, D., Nardi, D., & Patel-Schneider, P.F. (2003). *The Description Logic Handbook: Theory, Implementation, and Applications*. Cambridge University Press.
5. Ni, Y., & Mendling, J. (2008). "Business Rule Management for a Pragmatic Approach". *Proceedings of the International Conference on Knowledge Management*.
6. Fagbohun, O., Harrison, R. M., Dereventsov, A. (2024). An Empirical Categorization of Prompting Techniques for Large Language Models: A Practitioner’s Guide. Preprint presented at the 4th International Conference on AI, ML, Data Science, and Robotics.
7. Liu, P., et al. (2023). Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM Computing Surveys, 55(9).
8. Yu, Z., et al. (2023). Towards better chain-of-thought prompting strategies: A survey. arXiv preprint arXiv:2310.04959.