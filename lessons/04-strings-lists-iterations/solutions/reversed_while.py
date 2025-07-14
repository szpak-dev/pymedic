text: str = 'python'
i = len(text) - 1
print(i)
reversed_text = ""

while i >= 0:
    reversed_text = reversed_text + text[i]
    i -= 1

print(reversed_text)