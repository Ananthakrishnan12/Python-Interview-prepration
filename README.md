# Python Coding Interview Questions for Beginners

This repository contains a collection of Python coding questions that are commonly asked in interviews. These questions cover various topics such as string manipulation, list comprehensions, lambda functions, filtering, mapping, and data manipulation using Pandas.

## 📌 Topics Covered
- String Manipulation
- List Operations
- Recursion
- Searching & Sorting
- Leetcode Problems
- Lambda Functions
- Functional Programming (Filter, Map, Zip)
- Regular Expressions (Regex)
- Pandas Data Filtering & Manipulation
- String Methods & Aggregation

---

## 🚀 Python Coding Questions

### 🔹 String & List Operations
1. Reverse a string.
2. Reverse a string in a list. (Input: `["h","e","l","l","o"]`)
3. Reverse an array. (Input: `[1,2,3,4,5]`)
4. Check if a string is a palindrome. (Leetcode Q: 125)
5. Check if a number is a palindrome. (Input: `12321`)
6. Count vowels in a string. (Input: `"Hello,World!"`)

### 🔹 Recursion & Factorial
7. Find the factorial of a number using recursion.
8. Generate the Fibonacci sequence.

### 🔹 Searching & Sorting
9. Find the maximum element in a list.
10. Check if two strings are anagrams. (Leetcode Q: 242)
11. Check if a number is prime.

### 🔹 Leetcode Problems
12. Two Sum (Leetcode Q: 1)
13. Longest Substring Without Repeating Characters (Leetcode Q: 3)
14. Longest Palindromic Substring (Leetcode Q: 5)
15. Top K Frequent Elements (Leetcode Q: 347)
16. Merge Two Sorted Lists (Leetcode Q: 21)
17. Reverse Integer (Leetcode Q: 7)
18. Reverse Linked List (Leetcode Q: 206)
19. Reverse Words in a String (Leetcode Q: 151)
20. Missing Number (Leetcode Q: 268)
21. First Non-Repeating Character in a String.
22. Move All Zeroes to the End (Leetcode Q: 283)
23. Longest Common Prefix (Leetcode Q: 14)

### 🔹 Additional Python Problems
24. Count the frequency of words in a string.
25. Find the second largest number in a list.
26. Find all pairs in a list that sum to a target value.
27. Remove duplicates from a string.
28. Check if a number is an Armstrong number.
29. Convert a string to title case.
30. Swap two elements in a list.

---

## 🔥 List Comprehensions
31. Generate a list of squares of even numbers from `1` to `20`.
32. Convert a list of words to uppercase if they have more than `3` letters.
33. Create a dictionary with numbers as keys and their cubes as values.
34. Flatten a nested list using list comprehension.

## 🔥 Lambda Functions
35. Sort a list of tuples based on the second value.
36. Use lambda to create a function that multiplies two numbers.

## 🔥 Functional Programming
### Filter()
37. Filter out even numbers from a list.
38. Filter words that start with 'a'.

### Map()
39. Convert a list of strings into their lengths.

### Zip()
40. Merge two lists into a dictionary.
41. Add corresponding elements of two lists.
42. Find common elements in two lists.
43. Generate a list of squares for odd numbers using list comprehension and `map()`.

---

## 📝 Pattern Matching Using Regex
44. Count occurrences of a pattern like "code" in a string.
45. Check if a string contains the pattern "bob" where the middle character can be anything.
46. Double every character in a string.
47. Transform a string by tripling vowels and doubling consonants.
48. Extract specific words from a large string.
49. Implement Run-Length Encoding (String Compression).

---

## 📊 Data Analysis with Pandas

### 🛠 Data Filtering
Dataset:
```python
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [50000, 60000, 45000, 70000]
}
df = pd.DataFrame(data)
```

#### Easy
50. Filter people older than 30.
51. Filter people living in `New York`.
52. Display people with a salary greater than `60000`.

#### Medium
53. Filter people who live in `London` and are older than `30`.
54. Filter people living in `New York` or `Paris`.
55. Filter names starting with 'A' or 'B'.
56. Filter people aged between `25` and `35`.

#### Hard
57. Show people whose salary is within one standard deviation of the mean.
58. Show people who have the same age as at least one other person.
59. Show people with the highest salary within their city.

---

## 🏆 String Methods & Aggregation
Dataset:
```python
string_data = {
    'Email': ['alice@example.com', 'bob@test.co.uk'],
    'Name': ['Alice Smith', 'Bob Smith'],
    'Address': ['123 Main St', '456 Oak Ave']
}
df = pd.DataFrame(string_data)
```

#### Easy
60. Extract the domain name from `Email`.
61. Convert `Name` column to lowercase.
62. Check if an email contains the word `example`.

#### Medium
63. Extract first names from the `Name` column.
64. Count occurrences of 'a' in addresses.
65. Replace spaces in `Address` with underscores.
66. Create a new column with the length of each email address.

#### Hard
67. Extract usernames from `Email`, handling underscores.
68. Find the longest name in the `Name` column.
69. Create initials for each name.

---

## 📊 Data Manipulation
Dataset:
```python
data_manipulation = {
    'ID': [1, 2, 3],
    'Value1': [10, 20, 30],
    'Value2': [100, 90, 80]
}
df = pd.DataFrame(data_manipulation)
```

#### Easy
70. Create a new column `Total` = `Value1` + `Value2`.
71. Rename `ID` to `RecordID`.
72. Delete the `Value2` column.

#### Medium
73. Create a `Difference` column = `abs(Value1 - Value2)`.
74. Shift `Value1` column down by one row.
75. Create a column for cumulative sum of `Value1`.
76. Sort DataFrame by `Value1` in descending order.

#### Hard
77. Pivot the DataFrame with `ID` as index.
78. Create a rolling mean column for `Value1` with a window of `3`.
79. Apply a custom function: double even values, triple odd values.

---
# Python Coding Interview Questions for Beginners

This repository contains a collection of Python coding questions that are commonly asked in interviews. These questions cover various topics such as string manipulation, list comprehensions, lambda functions, filtering, mapping, and data manipulation using Pandas.

## 📌 Topics Covered
- String Manipulation
- List Operations
- Recursion
- Searching & Sorting
- Leetcode Problems
- Lambda Functions
- Functional Programming (Filter, Map, Zip)
- Regular Expressions (Regex)
- Pandas Data Filtering & Manipulation
- String Methods & Aggregation

---

## 🚀 Python Coding Questions

### 🔹 String & List Operations
1. Reverse a string.(https://github.com/Ananthakrishnan12/Python-Interview-prepration/blob/main/Solutions/Question1.py)
2. Reverse a string in a list. (Input: `["h","e","l","l","o"]`)
3. Reverse an array. (Input: `[1,2,3,4,5]`)
4. Check if a string is a palindrome. (Leetcode Q: 125)
5. Check if a number is a palindrome. (Input: `12321`)
6. Count vowels in a string. (Input: `"Hello,World!"`)

### 🔹 Recursion & Factorial
7. Find the factorial of a number using recursion.
8. Generate the Fibonacci sequence.

### 🔹 Searching & Sorting
9. Find the maximum element in a list.
10. Check if two strings are anagrams. (Leetcode Q: 242)
11. Check if a number is prime.

### 🔹 Leetcode Problems
12. Two Sum (Leetcode Q: 1)
13. Longest Substring Without Repeating Characters (Leetcode Q: 3)
14. Longest Palindromic Substring (Leetcode Q: 5)
15. Top K Frequent Elements (Leetcode Q: 347)
16. Merge Two Sorted Lists (Leetcode Q: 21)
17. Reverse Integer (Leetcode Q: 7)
18. Reverse Linked List (Leetcode Q: 206)
19. Reverse Words in a String (Leetcode Q: 151)
20. Missing Number (Leetcode Q: 268)
21. First Non-Repeating Character in a String.
22. Move All Zeroes to the End (Leetcode Q: 283)
23. Longest Common Prefix (Leetcode Q: 14)

### 🔹 Additional Python Problems
24. Count the frequency of words in a string.
25. Find the second largest number in a list.
26. Find all pairs in a list that sum to a target value.
27. Remove duplicates from a string.
28. Check if a number is an Armstrong number.
29. Convert a string to title case.
30. Swap two elements in a list.

---

## 🔥 List Comprehensions
31. Generate a list of squares of even numbers from `1` to `20`.
32. Convert a list of words to uppercase if they have more than `3` letters.
33. Create a dictionary with numbers as keys and their cubes as values.
34. Flatten a nested list using list comprehension.

## 🔥 Lambda Functions
35. Sort a list of tuples based on the second value.
36. Use lambda to create a function that multiplies two numbers.

## 🔥 Functional Programming
### Filter()
37. Filter out even numbers from a list.
38. Filter words that start with 'a'.

### Map()
39. Convert a list of strings into their lengths.

### Zip()
40. Merge two lists into a dictionary.
41. Add corresponding elements of two lists.
42. Find common elements in two lists.
43. Generate a list of squares for odd numbers using list comprehension and `map()`.

---

## 📝 Pattern Matching Using Regex
44. Count occurrences of a pattern like "code" in a string.
45. Check if a string contains the pattern "bob" where the middle character can be anything.
46. Double every character in a string.
47. Transform a string by tripling vowels and doubling consonants.
48. Extract specific words from a large string.
49. Implement Run-Length Encoding (String Compression).

---

## 📊 Data Analysis with Pandas

### 🛠 Data Filtering
Dataset:
```python
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [50000, 60000, 45000, 70000]
}
df = pd.DataFrame(data)
```

#### Easy
50. Filter people older than 30.
51. Filter people living in `New York`.
52. Display people with a salary greater than `60000`.

#### Medium
53. Filter people who live in `London` and are older than `30`.
54. Filter people living in `New York` or `Paris`.
55. Filter names starting with 'A' or 'B'.
56. Filter people aged between `25` and `35`.

#### Hard
57. Show people whose salary is within one standard deviation of the mean.
58. Show people who have the same age as at least one other person.
59. Show people with the highest salary within their city.

---

## 🏆 String Methods & Aggregation
Dataset:
```python
string_data = {
    'Email': ['alice@example.com', 'bob@test.co.uk'],
    'Name': ['Alice Smith', 'Bob Smith'],
    'Address': ['123 Main St', '456 Oak Ave']
}
df = pd.DataFrame(string_data)
```

#### Easy
60. Extract the domain name from `Email`.
61. Convert `Name` column to lowercase.
62. Check if an email contains the word `example`.

#### Medium
63. Extract first names from the `Name` column.
64. Count occurrences of 'a' in addresses.
65. Replace spaces in `Address` with underscores.
66. Create a new column with the length of each email address.

#### Hard
67. Extract usernames from `Email`, handling underscores.
68. Find the longest name in the `Name` column.
69. Create initials for each name.

---

## 📊 Data Manipulation
Dataset:
```python
data_manipulation = {
    'ID': [1, 2, 3],
    'Value1': [10, 20, 30],
    'Value2': [100, 90, 80]
}
df = pd.DataFrame(data_manipulation)
```

#### Easy
70. Create a new column `Total` = `Value1` + `Value2`.
71. Rename `ID` to `RecordID`.
72. Delete the `Value2` column.

#### Medium
73. Create a `Difference` column = `abs(Value1 - Value2)`.
74. Shift `Value1` column down by one row.
75. Create a column for cumulative sum of `Value1`.
76. Sort DataFrame by `Value1` in descending order.

#### Hard
77. Pivot the DataFrame with `ID` as index.
78. Create a rolling mean column for `Value1` with a window of `3`.
79. Apply a custom function: double even values, triple odd values.

---
## 💡 Resources
- [Python Docs](https://docs.python.org/3/)
- [Leetcode](https://leetcode.com/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/)

Happy Coding! 🚀


