# Lesson 1: Introduction to Python & Medical Data Use Cases

## Lesson Overview

This lesson introduces Python as a foundational tool for working with medical data. By the end of the lesson, you will:

- Understand basic Python syntax and data types.
- Learn how to represent and manipulate medical data using Python.
- Explore three common medical data problems: BMI calculation, glucose level categorization, and patient triage scoring.
- Write Python programs to solve real-world medical scenarios without external libraries.

## Common Medical Problems Modeled with Python

### Body Mass Index (BMI) Classification

BMI is a measure of body fat based on height and weight. It is used widely for basic health assessments.

**BMI Categories:**

- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI < 25
- Overweight: 25 ≤ BMI < 30
- Obesity: BMI ≥ 30

### Blood Glucose Level Categorization

Blood glucose levels help identify conditions such as diabetes or hypoglycemia.

**Fasting Blood Glucose Levels:**

- Hypoglycemia: < 70 mg/dL
- Normal: 70–99 mg/dL
- Prediabetes: 100–125 mg/dL
- Diabetes: ≥ 126 mg/dL

### Patient Triage Scoring

Triage determines the priority of patients’ treatments based on the severity of their condition.

**Simple Scoring Criteria:**

- Respiratory Rate > 30: +2 points
- Heart Rate > 120: +2 points
- Temperature > 39°C: +1 point
- Temperature < 35°C: +1 point
- Age ≥ 65: +1 point


## Homework

### Exercise 1: Body Mass Index (BMI) Classification

**Objective:**
Write a program that calculates the Body Mass Index (BMI) and classifies it according to the given categories.

**Instructions:**

1. Prompt the user to enter their weight in kilograms and height in meters.
2. Calculate the BMI using the formula: BMI = weight (kg) / (height (m)<sup>2</sup>).
3. Classify the BMI according to the following categories:
   - Underweight: BMI < 18.5
   - Normal weight: 18.5 ≤ BMI < 25
   - Overweight: 25 ≤ BMI < 30
   - Obesity: BMI ≥ 30
4. Display the calculated BMI and its classification.

**Example Output:**

```
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is: 22.86
Classification: Normal weight
```

### Exercise 2: Blood Glucose Level Categorization

**Objective:**
Write a program that categorizes blood glucose levels according to the given criteria.

**Instructions:**

1. Prompt the user to enter their fasting blood glucose level in mg/dL.
2. Categorize the blood glucose level according to the following criteria:
   - Hypoglycemia: < 70 mg/dL
   - Normal: 70–99 mg/dL
   - Prediabetes: 100–125 mg/dL
   - Diabetes: ≥ 126 mg/dL
3. Display the blood glucose level and its category.

**Example Output:**

```
Enter your fasting blood glucose level in mg/dL: 85
Your blood glucose level is: 85 mg/dL
Category: Normal
```

### Exercise 3: Patient Triage Scoring

**Objective:**
Write a program that calculates a simple triage score based on the given criteria.

**Instructions:**

1. Prompt the user to enter the following patient information:
   - Respiratory rate
   - Heart rate
   - Temperature in °C
   - Age
2. Calculate the triage score based on the following criteria:
   - Respiratory Rate > 30: +2 points
   - Heart Rate > 120: +2 points
   - Temperature > 39°C: +1 point
   - Temperature < 35°C: +1 point
   - Age ≥ 65: +1 point
3. Display the calculated triage score.

**Example Output:**

```
Enter the patient's respiratory rate: 35
Enter the patient's heart rate: 110
Enter the patient's temperature in °C: 38
Enter the patient's age: 70
Triage Score: 3
```
