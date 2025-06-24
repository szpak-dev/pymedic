# Chapter 1: Strings

In Python, strings are ordered sequences of characters. Each character in a string has a position index, allowing you to access individual characters or groups of characters.

```python
my_string = "Hello, Python!"
```

## Indexing
You can access individual characters using square brackets `[]` with the character's index.

- Positive indices start from 0 (left to right)
- Negative indices start from -1 (right to left)

```python
print(my_string[0])    # 'H' - first character
print(my_string[7])    # 'P' - 8th character
print(my_string[-1])   # '!' - last character
print(my_string[-3])   # 'o' - third from last
```

## Slicing
Get substrings using slicing syntax: `[start:stop:step]`

- `start`: inclusive beginning index (default 0)
- `stop`: exclusive ending index (default end)
- `step`: increment (default 1)

```python
print(my_string[0:5])     # 'Hello' - chars 0 to 4
print(my_string[7:13])    # 'Python' - chars 7 to 12
print(my_string[:5])      # 'Hello' - start to 4
print(my_string[7:])      # 'Python!' - 7 to end
print(my_string[::2])     # 'Hlo yhn' - every 2nd char
print(my_string[::-1])    # '!nohtyP ,olleH' - reversed
```

## Immutability
Strings are immutable - you cannot change individual characters after creation.

```python
# This will cause an error:
# my_string[0] = 'h'  # TypeError

# Instead, create a new string:
my_string = 'h' + my_string[1:]
print(my_string)  # 'hello, Python!'
```

## Common String Operations

```python
# Length
print(len(my_string))  # 14

# Concatenation
new_string = my_string + " Welcome!"
print(new_string)  # 'hello, Python! Welcome!'

# Repetition
print("Ha" * 3)  # 'HaHaHa'

# Membership
print('Python' in my_string)  # True
print('Java' not in my_string)  # True
```

## Important Notes
- Indexing starts at `0`
- Slicing never raises index errors (returns empty string if out of bounds)
- Original string remains unchanged after operations (new strings are created)


## Homework

### Task 1: Reverse Words in a Sentence

**Description:**
You are given a sentence. Reverse the letters in each word but keep the word order the same.

**Input Example:**

```python
sentence = "Python is powerful"
```

**Expected Output:**

```python
"nohtyP si lufrewop"
```


### Task 2: Remove Duplicated Characters

**Description:**
Given a string, return a version with all duplicated characters removed (only first occurrences kept).

**Input Example:**

```python
text = "programming"
```

**Expected Output:**

```python
"progamin"
```


### Task 3: Count Vowels and Consonants

**Description:**
Count how many vowels and how many consonants are in the given lowercase string (assume no digits or punctuation).

**Input Example:**

```python
line = "artificialintelligence"
```

**Expected Output:**

```python
Vowels: 10  
Consonants: 11
```


### Task 4: Check for Palindrome (Ignore Case and Spaces)

**Description:**
Determine if a given string is a palindrome when ignoring spaces and case.

**Input Example:**

```python
original = "Never Odd Or Even"
```

**Expected Output:**

```python
True
```
