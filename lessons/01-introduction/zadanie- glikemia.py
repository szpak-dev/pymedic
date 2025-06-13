
glycemia = int(input("Jaki jest twój poziom glukozy na czczo?: "))

if glycemia < 70:
    diagnosis = "Hypoglycemia"
elif glycemia >= 70 and glycemia < 100:
    diagnosis = "Normal glycemia"
elif glycemia >= 100 and glycemia <= 125:
    diagnosis = "Prediabetes"
else: diagnosis = "Diabetes"

print(f"Your diagnosis: {diagnosis}.")
