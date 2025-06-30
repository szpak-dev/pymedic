
# Początkowo próbowałem zrobić wersje z podawaniem wartości zmiennych w konsoli -> niemożliwe bo wartości z konsoli to zawsze str

a ="121"
b = 3.5
c = True

# isinstance int dla bool to też True (kiedyś nie było bool) -> musiałem odwrócić kolejność warunków if, elif

if isinstance(a, bool):
    print(f"Original A: {a} (bool) → Transformed: {a * 2} (int)")
    a = a * 2
elif isinstance(a, str):
    a = int(a)
    print(f"Original A: '{a}' (str) → Transformed: {a + 10} (int)")
    a +=  10
elif isinstance(a, (int, float)):
    print(f"Original A: '{a}' (int or float) → No-transformation")




if isinstance(b, bool):
    print(f"Original B: {b} (bool) → Transformed: {b * 2} (int)")
    b = b * 2
elif isinstance(a, str):
    b = int(a)
    print(f"Original B: '{b}' (str) → Transformed: {b + 10} (int)")
    b +=  10
elif isinstance(b, (int, float)):
    print(f"Original B: '{b}' (int or float) → No-transformation")




if isinstance(c, bool):
    print(f"Original C: {c} (bool) → Transformed: {c * 2} (int)")
    c = c * 2
elif isinstance(a, str):
    c = int(a)
    print(f"Original C: '{c}' (str) → Transformed: {c + 10} (int)")
    c +=  10
elif isinstance(b, (int, float)):
    print(f"Original C: '{c}' (int or float) → No-transformation")


