
respiratory = int(input("Respiratory rate: "))
hr = int(input("Heart rate: "))
temperature = int(input("Temperature: "))
age = int(input("Age: "))

triage_score = 0

if respiratory > 30:
    triage_score += 2

if hr > 120:
    triage_score += 2

if temperature > 39 or temperature < 35:
    triage_score += 1

if age >= 65:
    triage_score += 1


print(f"Triage Score: {triage_score}.")
