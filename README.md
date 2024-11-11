
# RelateScript: A Declarative Language to streamline the generation of consistent prompts for large language models (LLMs)


## Abstract
RelateScript is a proposed declarative language designed to allow flexible, readable, and context-sensitive programming based on relational and predicate logic. This paper presents RelateScript's syntax, purpose, and a comparison with existing languages. By focusing on relationships, conditions, and context, RelateScript aims to bridge the gap between natural language expression and computational logic, making it particularly suited for applications in knowledge representation, AI, and decision-making systems.

---

## 1. Introduction
In computing, imperative languages often impose strict structures, demanding exact instructions to achieve desired outcomes. This rigidity contrasts with natural human reasoning, which relies on relationships, conditions, and context. For applications in knowledge representation, artificial intelligence, and decision-making, a more flexible, declarative approach can be beneficial. RelateScript is a language designed to meet these needs, inspired by predicate logic and relational models, while remaining as readable as natural language.

### 1.1 Motivation
RelateScript seeks to provide an accessible and intuitive way of describing relationships and dependencies between entities. With a syntax that focuses on readability and ease of understanding, it aims to enable developers to express complex conditions and goals in a way that aligns closely with human reasoning.

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
Below is an example prompt that defines a customer, a product, and conditions for purchase.

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
string           ::= '"' { character } '"' ;
number           ::= digit { digit } ;
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

3 **Expression rules**:
- **condition expressions** (`condition_expr`): Check relationships or properties between entities.
- **Goal expressions** (`goal_expr`): Describe what is to be achieved.
- **Actions** (`action`): Relate to the goal that is to be fulfilled.

4 **Basic structures**:
- `entity`, `predicate_value`, `attribute_name`, `attribute_value` and `relation_type` are basic components represented by identifiers (e.g. names) or values (such as numbers).

5 **Operators**:
- `predicate_operator`, `attribute_operator`, and `relation_operator` define the type of relationships or conditions, e.g. “is”, “has”, “relates to”.

6 **Terminals**:
- `identifier` represents names and must begin with a letter.
- `string` stands for text and is enclosed in quotation marks.

---

## 3. Comparison with Existing Languages

Several languages and frameworks offer relational, declarative, or context-sensitive capabilities. Here, we compare RelateScript to similar systems.

### 3.1 Prolog
**Prolog** is a logic programming language commonly used in AI. It uses facts and rules to derive new information.
- **Similarity**: Both languages use declarative structures to represent relations.
- **Difference**: Prolog's syntax and predicate logic make it less readable for non-technical users.

### 3.2 Datalog
**Datalog** is a simplified version of Prolog, used for database queries and logical reasoning.
- **Similarity**: Datalog’s focus on facts and rules aligns with RelateScript's relational approach.
- **Difference**: Datalog lacks natural language readability and context-sensitive features.

### 3.3 SPARQL and RDF
**SPARQL** and **RDF** model data as a graph of subject-predicate-object relationships, often for the semantic web.
- **Similarity**: Both use declarative syntax to express relationships.
- **Difference**: SPARQL and RDF are tailored for distributed knowledge bases, not flexible programming.

### 3.4 Description Logic (DL)
**Description Logic** is a formal language for knowledge representation in ontologies.
- **Similarity**: Both use logical relations to define entities and their attributes.
- **Difference**: Description Logic's formalism is more complex and less natural for general programming.

### 3.5 Rules Engines (e.g., Drools)
**Rules Engines** use declarative rules for automated decision-making in business applications.
- **Similarity**: They support `if-then` logic, like RelateScript’s conditions and goals.
- **Difference**: Rules engines are often restricted to business applications and lack RelateScript’s flexible syntax.

---

## 4. Applications

RelateScript’s structure is ideal for:
- **AI Systems**: Defining context-aware rules for automated reasoning.
- **Knowledge Representation**: Modeling entities, attributes, and relationships within a specific domain.
- **Decision-Making Systems**: Using goals and conditions to dynamically adjust program behavior.

### 4.1 Advantages of RelateScript for an LLM
1. **Clarity and Precision**: RelateScript is clearly structured, with defined rules and terms. This reduces the ambiguity often found in natural language and ensures that the LLM correctly interprets the intended meaning.
  
2. **Clear Relationships and Conditions**: The declarative structure of RelateScript is particularly suited to explicitly formulate connections and conditions. This can help an LLM draw conclusions or coordinate sequential steps.

3. **Reduced Interpretation**: Since RelateScript is based on a logical grammar, the "interpretation work" for an LLM is often easier. It requires less contextual understanding of the language itself and can focus on the instructions.

### 4.2 Limitations of RelateScript Compared to Natural Language
1. **Comprehensibility and Accessibility**: For many users, natural language is more intuitive and easier to use, as it requires no specific structure or defined syntax. This is an advantage when the instructions for the LLM are created by non-programmers.

2. **Flexibility and Expressiveness**: Natural language is much more flexible and can convey complex, nuanced instructions that are harder to express in a highly structured system like RelateScript. Examples include metaphors, vague terms, or context descriptions common in human communication.

3. **Processing Capability of LLMs**: Modern LLMs like GPT-4 are designed to understand natural language and process it contextually. They are often already capable of interpreting complex instructions without requiring a formalized language. In many cases, LLMs understand natural language accurately enough, so RelateScript offers fewer advantages.

### 4.3 Recommendation: Combining RelateScript and Natural Language
One approach could be to use RelateScript as a *supplement* to natural language, especially for instructions that contain logical sequences, conditions, and relationships. For example, you might formulate instructions in natural language and use RelateScript for precise, logical parts.

---

## 5. Conclusion

RelateScript provides a human-readable, declarative approach to programming that emphasizes relationships, conditions, and context. By drawing on relational models and predicate logic, RelateScript offers a middle ground between natural language and computational logic, making it suitable for applications where readability and flexibility are crucial.

RelateScript is designed as a tool to streamline the generation of consistent prompts for large language models (LLMs). By leveraging syntax that emphasizes readability and ease of understanding, RelateScript allows users to convey complex conditions and objectives in a manner that resonates with natural human language. Unlike traditional programming languages that require explicit definitions of loops, types, and other constructs, RelateScript presumes that LLMs inherently recognize these contextual cues. This approach prioritizes natural language principles over rigid programming paradigms, making it easier for humans to communicate nuanced instructions that align with an LLM's contextual understanding capabilities.

Future work could involve testing the language in real-world AI and knowledge management systems.
 
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
