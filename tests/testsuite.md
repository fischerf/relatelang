The test suite consists of various **instructions and scenarios** that differ in complexity and cover different aspects of the language. Each instruction is formulated to use the structure of RelateScript and provides no additional explanations or interpretation hints.

Each test case contains an instruction, expected behavior or expected response, and an indication of which aspect of the language it tests.

---

## Test Suite for RelateScript

### 1. Basic Definition and Relationship

**Instruction:**
```plaintext
define Book as "An object with pages".
define Author as "A person who writes books".
Book has Author of "J.K. Rowling".
```

**Expected Behavior:**
The LLM should recognize that a "Book" is an object and "J.K. Rowling" is the author of the book.

**Test Objective:** Verify if the LLM recognizes simple entities and attributes and assigns them correctly.


### 2. Simple Query Based on Definitions

**Instruction:**
```plaintext
define Plant as "Living being that performs photosynthesis".
Flower is a Plant.
ask "Is Flower a Plant?".
```

**Expected Behavior:**
The LLM should correctly answer the question "Is Flower a Plant?", ideally with "Yes, Flower is a Plant."

**Test Objective:** Test if the LLM recognizes the relationship between entity and category and can answer simple questions about hierarchy.


### 3. Condition and Evaluation

**Instruction:**
```plaintext
define Animal as "A living being".
Animal has Ability of "walk".
Dog is an Animal.

if Dog has Ability of "walk",
    then ensure Dog is active.
```

**Expected Behavior:**
The LLM should conclude that "Dog" is active because it has the ability to "walk".

**Test Objective:** Verify if the LLM understands conditions and can draw conclusions based on the condition.


### 4. Compound Instructions and Multi-level Logic

**Instruction:**
```plaintext
define City as "A collection of buildings and people".
Berlin is a City.
Berlin has Population of 3_500_000.
define Metropolis as "A city with more than 1_000_000 inhabitants".

if City has Population > 1_000_000,
    then ensure City is a Metropolis.
```

**Expected Behavior:**
The LLM should recognize that Berlin is a "Metropolis" because its population is greater than 1,000,000.

**Test Objective:** Verify the ability to process numerical conditions and derive a classification from them.


### 5. Nested Conditions and Sequences

**Instruction:**
```plaintext
define Human as "An intelligent living being".
define Child as "A young human".
Human has Ability of "think".
Child has Ability of "learn".
Human has Age.
Child has Age < 18.

if Human has Ability of "think" and Child has Ability of "learn",
    then ensure Child is related to Human as "is a young human".
```

**Expected Behavior:**
The LLM should recognize that a "Child" is a "young human" and correctly apply the conditions to both entities.

**Test Objective:** Test if the LLM can evaluate complex and nested conditions.


### 6. Applying Context to a New Instruction

**Instruction:**
```plaintext
define Vehicle as "A means of transportation".
Car is a Vehicle.
Bicycle is a Vehicle.
define Motorized as "has an engine".

if Car has Motorized,
    then ensure Car is faster than Bicycle.
```

**Expected Behavior:**
The LLM should conclude that a "Car" is faster than a "Bicycle" due to its engine.

**Test Objective:** Verify if the LLM correctly interprets the context (motorization and speed) and can derive a conclusion from it.


### 7. Sequential Instructions and Action Sequences

**Instruction:**
```plaintext
define Ingredient as "A component of a dish".
define Dish as "A food that consists of ingredients".

begin Cooking:
    Step 1: Select ingredients.
    Step 2: Mix ingredients.
    Step 3: Cook ingredients.
end Cooking.

if Dish requires Ingredient,
    then ensure Cooking is complete.
```

**Expected Behavior:**
The LLM should understand the "Cooking" process and recognize that the dish is complete when all steps are finished.

**Test Objective:** Test if the LLM can follow a sequential process and derive a condition for "completeness" from it.

---

### Summary and Evaluation Guide

Each test poses different requirements for the LLM and covers various aspects of RelateScript.

- **Successful Interpretation:** If the LLM is able to provide the expected answers or conclusions, this shows that RelateScript is intuitive enough to be used as a prompt language.
- **Misunderstandings or Misinterpretations:** If the LLM does not interpret the instructions as expected, it might help to adjust the structure of RelateScript to reduce ambiguities or define specific terms more clearly.

This test suite provides a foundation for evaluating how effectively RelateScript can control an LLM, and whether the language is suitable as a simple, precise, and "intuitively understandable" prompt language.