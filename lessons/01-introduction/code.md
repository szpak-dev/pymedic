# Lesson 1 Scripts

## BMI Calculator and Classifier

```python
weight_kg: float = 72.0
height_m: float = 1.75
bmi: float = weight_kg / (height_m ** 2) # squared

if bmi < 18.5:
    category: str = "Underweight"
elif bmi < 25.0:
    category = "Normal weight"
elif bmi < 30.0:
    category = "Overweight"
else:
    category = "Obesity"

print(f"BMI: {bmi:.2f}, Category: {category}")
```

## Blood Glucose Level Categorizer

```python
glucose_mg_dl: int = 110

if glucose_mg_dl < 70:
    category: str = "Hypoglycemia"
elif glucose_mg_dl <= 99:
    category = "Normal"
elif glucose_mg_dl <= 125:
    category = "Prediabetes"
else:
    category = "Diabetes"

print(f"Glucose Level: {glucose_mg_dl} mg/dL, Category: {category}")
```

## Patient Triage Score Calculator

```python
resp_rate: int = 32
heart_rate: int = 125
temp_c: float = 39.5
age: int = 70

score: int = 0

if resp_rate > 30:
    score += 2
if heart_rate > 120:
    score += 2
if temp_c > 39.0 or temp_c < 35.0:
    score += 1
if age >= 65:
    score += 1

print(f"Triage Score: {score}")
```
