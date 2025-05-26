# RelateLang: A Declarative Meta-Language for Consistent LLM Prompt Engineering

## Abstract
**RelateLang** is a declarative meta-language designed to streamline the creation of structured and consistent prompts for large language models (LLMs).

This paper introduces RelateLang's syntax, highlighting its foundation in relational and predicate logic. By focusing on relationships, conditions, and context, RelateLang bridges the gap between natural language expressiveness and the precision required for effective LLM interaction. It facilitates a novel approach to prompt engineering, where humans and LLMs collaboratively develop structured prompts that can be easily modified and reused for diverse tasks, enhancing the reliability and automation capabilities of LLM-driven workflows. The language is particularly valuable in scenarios requiring structured input, chain-of-thought guidance, and maintainable prompt management in production systems.

---

## 1. Introduction
In the rapidly evolving field of large language models (LLMs), the effectiveness of interactions heavily relies on the quality of prompts. Traditional imperative programming languages often impose rigid structures that contrast with the nuanced and context-sensitive nature of human reasoning. While natural language offers unparalleled flexibility for interacting with LLMs, it can lead to ambiguity and inconsistency in prompt outputs. To address these challenges, we introduce RelateLang, a declarative meta-language specifically designed for crafting structured prompts. RelateLang enables users to define entities, relationships, and conditions in a format that is both readable and logically precise. RelateLang is not intended as a traditional programming language with a separate parser, but rather as a structured input format that leverages the inherent understanding capabilities of LLMs.

### 1.1 Motivation
RelateLang addresses the growing need for a more systematic and reliable approach to prompt engineering. As LLMs become increasingly sophisticated, the ability to articulate complex instructions and define precise conditions becomes crucial for harnessing their full potential. RelateLang provides an accessible and intuitive way of describing relationships and dependencies between entities, enabling users to express intricate logic in a manner that aligns closely with human reasoning. 

The language serves multiple purposes:
1. **Structured Input**: When ambiguity needs to be minimized
2. **Chain-of-Thought Guidance**: Leading LLMs through multi-step reasoning processes
3. **Maintainable Integration**: Standardizing prompts across development teams

With a syntax designed for readability, RelateLang empowers users to generate consistent prompts, making it particularly suited for building reusable prompt templates that can be adapted for different scenarios, thus enhancing the efficiency and reliability of LLM interactions.

### 1.2 The Challenge of Prompt Consistency

Consider a practical example from software development. When multiple developers embed LLM prompts in production code, linguistic and structural differences emerge:

```java
// Developer 1 (German native speaker)
String prompt = "The customer has bought items for 1500 euros last month. " +
                "He lives in Berlin which is a big city. Check if customer " + 
                "is premium when he buys more than 1000 euro.";

// Developer 2 (Indian English)
String prompt = "Customer has a purchase history of 1500 euros in previous month. " +
                "Customer's location is Berlin (metropolitan city). " +
                "Kindly verify premium status for purchases exceeding 1000 euros.";

// Developer 3 (American, after refactoring)
String prompt = "Given: A customer from Berlin (major city) with $1500 in purchases " +
                "last month. Task: Determine premium status (threshold: $1000).";
```

All three prompts attempt the same logic, but with different linguistic styles, structures, and even currency assumptions. This creates:
- **Maintenance nightmares**: Which version is correct? What's the actual threshold?
- **Review difficulties**: Code reviewers struggle to verify prompt logic
- **Testing challenges**: Inconsistent outputs from semantically equivalent prompts
- **Onboarding issues**: New developers must decipher various prompt styles

This standardization becomes crucial as teams scale and prompts encode important business logic.

### 1.3 RelateLang: Standardizing Prompts as Code

RelateLang solves this by providing a structured format that transcends linguistic differences:

```python
String prompt = """
    define Customer as "A person who purchases products".
    Customer has monthly_purchases of 1500.
    Customer has location of "Berlin".
    
    define PremiumCustomer as "Customer with high purchase value".
    
    if Customer has monthly_purchases > 1000,
        then ensure Customer is PremiumCustomer.
    """;
```

This approach mirrors how SQL standardized database queries across teams—you don't write "Please get me all customers from Berlin," you write `SELECT * FROM customers WHERE city = 'Berlin'`. RelateLang applies this principle to LLM prompts.

### 1.4 Key Benefits for Production Systems

1. **Language-Agnostic Structure**: Developers from any linguistic background write identical structures
2. **Code Review Friendly**: Business logic is explicit and reviewable
3. **Testable**: Prompt logic can be unit tested like any other code
4. **Maintainable**: Changes to business rules have clear, single update points
5. **Version Control Friendly**: Structured format produces clean diffs

---

## 2. Language Design

### 2.1 Design Principles for Production Use

RelateLang's syntax prioritizes:
- **Clarity over brevity**: Explicit is better than implicit
- **Standardization over flexibility**: One way to express common patterns  
- **Readability**: Non-technical stakeholders can understand business logic
- **LLM-native interpretation**: No parsing or compiler needed; LLMs understand directly

### 2.2 Syntax
The syntax of RelateLang emphasizes natural language structure, allowing for readable declarations of entities, relationships, and conditions. Its main constructs include:
- **Definitions**: `define <Entity> as <Description>.`
- **Predicates**: `<Entity> is <Predicate>.`
- **Attributes**: `<Entity> has <Attribute> of <Value>.`
- **Relations**: `relate <Entity1> and <Entity2> as <RelationType> [ if <Condition> ].`
- **Conditions**: `if <Condition>, then <Action>.`
- **Goals**: `ensure <Goal>.`

### 2.3 eBNF Grammar
The following Extended Backus-Naur Form (eBNF) defines RelateLang's core syntax:

```ebnf
program          ::= { statement } ;
statement        ::= definition | predicate | attribute | relation | condition | goal ;
definition       ::= "define" entity "as" string "." ;
predicate        ::= entity "is" predicate_value "." ;
attribute        ::= entity "has" attribute_name "of" attribute_value "." ;
relation         ::= "relate" entity "and" entity "as" relation_type [ "if" condition_expr ] "." ;
condition        ::= "if" condition_expr ", then" action "." ;
goal             ::= "ensure" goal_expr "." ;

condition_expr   ::= natural_expression ;
goal_expr        ::= natural_expression ;
action           ::= "ensure" natural_expression ;
natural_expression ::= { word | property_access | number | string } ;
property_access  ::= entity "." attribute_name ;

entity           ::= identifier ;
predicate_value  ::= identifier | string ;
attribute_name   ::= identifier ;
attribute_value  ::= identifier | number | string ;
relation_type    ::= string ;
word             ::= identifier ;

identifier       ::= ( lowercase-char | uppercase-char ) { lowercase-char | uppercase-char | digit | "_" } ;
string           ::= '"' { character } '"' ;
number           ::= [ "-" ] digit { digit } [ "." digit { digit } ] ;
character        ::= lowercase-char | uppercase-char | digit | special-char | " " ;
lowercase-char   ::= "a" | "b" | "..." | "z" ;
uppercase-char   ::= "A" | "B" | "..." | "Z" ;
special-char     ::= "-" | "_" | "'" | "," | ":" | ";" | "!" | "?" | "/" | "(" | ")" | ">" | "<" | "=" | "*" | "+" ;
digit            ::= "0" | "1" | "..." | "9" ;
```

**Design Philosophy:**
This grammar captures RelateLang's essential structure while maintaining the flexibility needed for LLM interpretation. Complex expressions, operators, and logic are handled as `natural_expression` - allowing LLMs to interpret conditions, comparisons, and actions using their natural language understanding rather than rigid parsing rules.

### 2.4 Explanations of the Rules

1. **Main structure (`program`)**: A program (prompt) consists of a sequence of `statements`, each of which defines a particular piece of information, relationship, or statement.

2. **Statements**:
- **Definition** (`definition`): Defines an entity with a name and a description.
- **Predicate** (`predicate`): Assigns a property or state to an entity.
- **Attributes** (`attribute`): Associates an entity with an attribute and its value.
- **Relationships** (`relation`): Defines a relationship between two entities, optionally with a condition.
- **Conditions** (`condition`): Defines a condition and a resulting action.
- **Goals** (`goal`): Describes a goal that is to be achieved.

3. **Expression rules**:
- **Condition expressions** (`condition_expr`): Checks relationships or properties between entities.
- **Goal expressions** (`goal_expr`): Describes what is to be achieved.
- **Actions** (`action`): Relates to the goal that is to be fulfilled.

4. **Basic structures**:
- `entity`, `predicate_value`, `attribute_name`, `attribute_value` and `relation_type` are basic components represented by identifiers (e.g. names) or values (such as numbers).

5. **Operators**:
- `predicate_operator`, `attribute_operator`, and `relation_operator` define the type of relationships or conditions, e.g. "is", "has", "relates to".

6. **Terminals**:
- `identifier` represents names and must begin with a letter.
- `string` stands for text and is enclosed in quotation marks.

### 2.5 Production Example: Fraud Detection System

```prolog
define Transaction as "A financial operation".
Transaction has amount of 2500.
Transaction has location of "Moscow".
Transaction has time of "03:00".
Transaction has merchant_category of "jewelry".

define UserProfile as "Historical user behavior".
UserProfile has home_location of "London".
UserProfile has typical_amount of 200.
UserProfile has typical_time_range of "09:00-22:00".

define RiskLevel as "Transaction risk assessment".

if Transaction has amount > (UserProfile.typical_amount * 5),
    then ensure RiskLevel is "high".

if Transaction.location != UserProfile.home_location and 
   Transaction.time not in UserProfile.typical_time_range,
    then ensure RiskLevel is "high".

ensure evaluate Transaction for fraud_risk.
```

This structure provides:
- **Reviewable**: "Why is the multiplier 5? Should it be 3?"
- **Testable**: Can verify logic with test transactions
- **Maintainable**: Threshold changes are single-line updates

### 2.6 Chain-of-Thought Guidance

Beyond production systems, RelateLang excels at guiding LLMs through complex reasoning processes by breaking down multi-step problems into structured logical sequences. This capability is particularly valuable when moving from simple rule-based scenarios (like the fraud detection example above) to more complex optimization problems.
RelateLang naturally guides LLMs through reasoning steps:

```prolog
define Location as "A point in the delivery network".
define Route as "A path connecting two or more locations".
define Vehicle as "The transport used for delivery".
Vehicle has capacity of 20. // units
Location has demand of 5. // units

define Step1_Result as "All possible route segments are identified".
define Step2_Result as "Routes exceeding vehicle capacity are eliminated".
define Step3_Result as "The shortest valid route is selected".

// Chain of logic
if Location exists,
    then ensure Step1_Result is achieved.

if Step1_Result is achieved and Route.total_demand > Vehicle.capacity,
    then ensure Route is invalid.

if Step2_Result is achieved,
    then ensure Step3_Result is achieved by optimizing for minimal_distance.

ensure generate optimal_route based on Step3_Result.
```

This structured approach helps LLMs maintain logical consistency across complex multi-step reasoning tasks, ensuring that each step builds appropriately on the previous ones.

---

## 3. Combining RelateLang and Natural Language

RelateLang offers a structured, logic-driven framework that seamlessly complements natural language-based prompting approaches. While natural language excels in conveying nuance and ambiguity, particularly for creative tasks, RelateLang provides clarity, precision, and logical consistency—essential qualities for complex and multi-step interactions with LLMs.

### 3.1 Integration with Natural Language Prompting
RelateLang can be effectively paired with natural language inputs to combine the strengths of both methods:

- **Natural Language**: Sets the context, describes abstract ideas, and initiates creative exploration through flexible phrasing.
- **RelateLang**: Ensures logical rigor by explicitly defining entities, relationships, and conditional rules within a structured template.

For example, a user might begin with a natural language prompt such as:  
*"Help me analyze customer behavior patterns."*  

This context can then be supported by a RelateLang block that precisely defines the analysis parameters.

### 3.2 Complementing LLM Prompting Techniques
RelateLang aligns with advanced prompting techniques for LLMs, such as:
1. **Chain-of-Thought (CoT) Prompting**: By explicitly structuring steps and conditions, RelateLang enhances the LLM's ability to reason through multi-step tasks (Wei et al., 2022).
2. **Decomposed Prompting**: Complex tasks can be broken down into RelateLang components (Khot et al., 2023).
3. **Program of Thoughts**: Separating computation from reasoning using structured formats (Chen et al., 2023).

### 3.3 Applications and Limitations
RelateLang is ideal for tasks requiring:
- Precise execution of logical rules and conditions
- Modeling of structured systems like workflows, decision trees, or knowledge graphs
- Creating reusable prompt templates for consistent LLM interactions
- Maintaining prompts in production codebases

However, natural language remains superior for:
- Creative, open-ended tasks where ambiguity or nuance is a feature
- Rapid prototyping of ideas without requiring formalized structures

---

## 4. Applications

RelateLang's structure is ideal for various domains:

### 4.1 Scientific Research
- Formalizing hypotheses and experimental designs
- Documenting methodological procedures and constraints
- Structuring systematic reviews and meta-analyses
- Modeling complex relationships in data

Example: Modeling physical phenomena
```prolog
define Photon as "A quantum of light".
Photon has energy of E.
define Metal as "A metallic element".
Metal has work_function of Phi.

if Photon.energy > Metal.work_function,
    then ensure Electron is emitted.
```

### 4.2 AI Systems and Automation
- Defining context-aware rules for automated reasoning
- Building knowledge graphs for machine learning
- Specifying training data relationships
- Creating structured prompts for LLMs

### 4.3 Enterprise Software Development
When embedding LLM interactions in production systems, RelateLang provides:

**Standardization Across Teams**: International teams write consistent prompt structures regardless of linguistic background

**Maintainable Business Logic**:
```prolog
define Transaction as "A financial operation".
Transaction has amount of 2500.
Transaction has risk_score of calculated.

if Transaction has amount > 1000 and Transaction occurs_at "unusual_hour",
    then ensure Transaction requires manual_review.
```

**Version Control Benefits**: Structured format produces clean, reviewable diffs

### 4.4 Knowledge Representation
Modeling entities, attributes, and relationships within specific domains for educational or reference purposes.

### 4.5 Decision-Making Systems
Using goals and conditions to dynamically adjust program behavior in complex scenarios.

---

## 5. Enterprise Integration Patterns

### 5.1 Direct LLM Interpretation
RelateLang requires no parser or compiler—LLMs interpret the structure directly. This is crucial for adoption as it requires no additional infrastructure.

### 5.2 Embedding in Production Code

**Java Example:**
```java
public class CustomerSegmentation {
    private final LLMService llmService;

    public CustomerSegmentation(LLMService llmService) {
        this.llmService = llmService;
    }

    private static final String SEGMENTATION_PROMPT = """
        define Customer as "A person who purchases products".
        Customer has total_purchases of %d.
        Customer has account_age_days of %d.
        Customer has support_tickets of %d.
        
        define HighValue as "Customer segment requiring premium support".
        define Standard as "Customer segment with normal support".
        
        if Customer has total_purchases > 10000 and account_age_days > 365,
            then ensure Customer is HighValue.
        
        if Customer has support_tickets > 5 and total_purchases > 5000,
            then ensure Customer is HighValue.
            
        ensure determine Customer segment.
        """;

    public String segmentCustomer(CustomerData data) {
        String prompt = String.format(SEGMENTATION_PROMPT, 
            data.getTotalPurchases(),
            data.getAccountAgeDays(), 
            data.getSupportTickets()
        );
        return llmService.complete(prompt);
    }
}
```

### 5.3 Prompt Versioning and Testing

**RelateLang template:** `customer_segmentation_v2.rl`
```prolog
        define Customer as "A person who purchases products".
        Customer has total_purchases of %d.
        Customer has account_age_days of %d.
        Customer has support_tickets of %d.
        
        define HighValue as "Customer segment requiring premium support".
        define Standard as "Customer segment with normal support".
        
        if Customer has total_purchases > 10000 and account_age_days > 365,
            then ensure Customer is HighValue.
        
        if Customer has support_tickets > 5 and total_purchases > 5000,
            then ensure Customer is HighValue.
            
        ensure determine Customer segment.
```

**Java Example:**
```java
@Test
public void testPremiumCustomerIdentification() {
    String promptTemplate = PromptLoader.load("customer_segmentation_v2.rl");

    Map<String, Object> values = Map.of(
        "totalPurchases", 15000,
        "accountAgeDays", 400,
        "supportTickets", 2
    );

    String formattedPrompt = PromptFormatter.format(promptTemplate, values);

    String result = llmService.complete(formattedPrompt);
    assertTrue(result.contains("HighValue"));
}
```

---

## 6. Comparison with Existing Languages and Approaches

### 6.1 Logic Programming Languages

**Prolog** (Clocksin & Mellish, 1981) and **Datalog** (Ullman, 1988):
- **Similarity**: Declarative structure, relational approach
- **Difference**: RelateLang prioritizes readability and direct LLM interpretation without parsing

### 6.2 Semantic Web Technologies

**SPARQL and RDF** (Berners-Lee et al., 2001):
- **Similarity**: Graph-based knowledge representation
- **Difference**: RelateLang focuses on prompt engineering, not distributed knowledge bases

### 6.3 Recent LLM-Specific Approaches

**LMQL** (Beurer-Kellner et al., 2023):
- SQL-like query language for LLMs
- More complex syntax, requires compilation

**DSPy** (Khattab et al., 2023):
- Declarative LLM programming framework
- Requires Python integration, not standalone

**RelateLang's Unique Position**:
- Direct LLM interpretation (no parsing/compilation)
- Human-readable syntax
- Language-agnostic structure for international teams
- Focus on maintainability in production systems

---

## 7. Related Work

### 7.1 Theoretical Foundations
RelateLang builds on established principles from:
- Declarative programming paradigms (van Roy & Haridi, 2004)
- Modular system design (Parnas, 1972)
- Domain-specific languages (Fowler, 2010)

---

## 8. Future Directions

### 8.1 Empirical Validation
Future work should focus on:
- Comparative studies of RelateLang vs. natural language prompts
- Consistency metrics across different LLMs
- Developer productivity measurements in team settings

### 8.2 Tooling Ecosystem
While not required, potential tooling includes:
- Syntax highlighting for popular IDEs
- Linting for common patterns
- Testing frameworks for prompt validation

### 8.3 Domain-Specific Extensions
Exploring specialized vocabularies for:
- Medical diagnosis protocols
- Legal reasoning frameworks
- Financial compliance rules

---

## 9. Conclusion

RelateLang provides a structured, declarative framework for tasks that require precision and logical consistency, making it a powerful tool in applications ranging from scientific research to production software systems. Its syntax emphasizes readability and ease of understanding, allowing users to convey complex conditions and objectives in a manner that resonates with natural human language.

The language addresses three key challenges in modern LLM usage:
1. **Minimizing ambiguity** when structured input is needed
2. **Guiding reasoning** through chain-of-thought processes
3. **Maintaining consistency** across teams and deployments

By integrating RelateLang with natural language prompting, users can leverage the best of both worlds—combining the intuitive, creative capabilities of natural language with the rigor and repeatability of logical reasoning. This hybrid approach broadens the scope of RelateLang's applications and positions it as an essential tool for enhancing LLM-driven workflows.

Just as SQL standardized database queries across applications and teams, RelateLang offers a path toward standardizing LLM prompt engineering—not by replacing natural language, but by providing structure where structure adds value.

---

## Author
*By Florian Fischer*  
*https://github.com/fischerf/*

## References
1. Clocksin, W.F., & Mellish, C.S. (1981). *Programming in Prolog*. Springer-Verlag.
2. Ullman, J.D. (1988). *Principles of Database and Knowledge-Base Systems*. Computer Science Press.
3. Berners-Lee, T., Hendler, J., & Lassila, O. (2001). "The Semantic Web". *Scientific American*.
4. Baader, F., Calvanese, D., McGuinness, D., Nardi, D., & Patel-Schneider, P.F. (2003). *The Description Logic Handbook*. Cambridge University Press.
5. Fowler, M. (2010). *Domain-Specific Languages*. Addison-Wesley Professional.
6. Fagbohun, O., Harrison, R. M., Dereventsov, A. (2024). "An Empirical Categorization of Prompting Techniques for Large Language Models". *4th International Conference on AI, ML, and Data Science*.
7. Wei, J., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models". *NeurIPS 2022*.
8. Khot, T., et al. (2023). "Decomposed Prompting: A Modular Approach for Solving Complex Tasks". *ICLR 2023*.
9. Chen, M., et al. (2023). "Program of Thoughts Prompting". *TMLR 2023*.
10. Beurer-Kellner, L., et al. (2023). "Prompting Is Programming: A Query Language for Large Language Models". *PLDI 2023*.
11. Khattab, O., et al. (2023). "DSPy: Compiling Declarative Language Model Calls into Pipelines". *arXiv:2310.03714*.
12. Jiang, Z., et al. (2022). "PromptMaker: Prompt-based Prototyping with Large Language Models". *CHI 2022*.
13. White, J., et al. (2023). "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT". *arXiv:2302.11382*.
14. Liu, P., et al. (2022). "PTR: Prompt Tuning with Rules for Text Classification". *ACL 2022*.
15. van Roy, P., & Haridi, S. (2004). *Concepts, Techniques, and Models of Computer Programming*. MIT Press.
16. Parnas, D. L. (1972). "On the Criteria to be Used in Decomposing Systems into Modules". *Communications of the ACM*.
17. Codd, E. F. (1970). "A Relational Model of Data for Large Shared Data Banks". *Communications of the ACM*.
18. Amershi, S., et al. (2019). "Software Engineering for Machine Learning: A Case Study". *ICSE 2019*.
19. Zamfirescu-Pereira, J. D., et al. (2023). "Why Johnny Can't Prompt". *CHI 2023*.
20. ISO/IEC 9075-1:2016. *Information technology — Database languages — SQL*.
