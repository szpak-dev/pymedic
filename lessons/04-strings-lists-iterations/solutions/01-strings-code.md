## Task 1: Reverse Words in a Sentence

```python
sentence = "Python is powerful"
words = sentence.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)
print(result)
```

## Task 2: Remove Duplicated Characters

```python
text = "programming"
result = ""

for char in text:
    if char not in result:
        result += char

print(result)
```

## Task 3: Count Vowels and Consonants

```python
line = "artificialintelligence"
vowels = "aeiou"
v_count = 0
c_count = 0

for char in line:
    if char in vowels:
        v_count += 1
    else:
        c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
```

## Task 4: Check for Palindrome (Ignore Case and Spaces)

```python
original = "Never Odd Or Even"
normalized = original.replace(" ", "").lower()
is_palindrome = normalized == normalized[::-1]

print(is_palindrome)
```
