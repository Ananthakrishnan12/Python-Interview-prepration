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
## Data Aggregation

### **Dataset**
```python
import pandas as pd

data_aggregation_data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 12, 35, 22, 18, 40],
    'Group': ['X', 'Y', 'X', 'Y', 'Z', 'X', 'Z', 'Y', 'X', 'Z']
}

df_aggregation = pd.DataFrame(data_aggregation_data)
```

### **Easy Tasks**
80. Calculate the mean of the 'Value' column.
81. Count the number of rows for each category.
82. Find the maximum value for each category.

### **Medium Tasks**
83. Calculate the sum of 'Value' for each 'Category' and 'Group' combination.
84. Find the median of 'Value' for each 'Category'.
85. Find the standard deviation of 'Value' for each 'Group'.
86. Find the minimum value within each group.

### **Hard Tasks**
87. Calculate the percentage of each category's total value relative to the overall total value.
88. Find the category with the highest average 'Value'.
89. Calculate the rolling average of the 'Value' column grouped by category.

---
## Data Integration

### **Datasets**
```python
import pandas as pd

data_integration_data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Product': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Price': [1.0, 0.5, 2.0, 1.5, 2.5]
}

df_integration1 = pd.DataFrame(data_integration_data1)

data_integration_data2 = {
    'ID': [3, 4, 5, 6, 7],
    'Quantity': [10, 20, 30, 40, 50],
    'Location': ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
}

df_integration2 = pd.DataFrame(data_integration_data2)
```

### **Easy Tasks**
90. Merge `df_integration1` and `df_integration2` based on the 'ID' column using an inner join.
91. Concatenate `df_integration1` and `df_integration2` vertically (stack them on top of each other).
92. Merge `df_integration1` and `df_integration2` using a left join.

### **Medium Tasks**
93. Merge `df_integration1` and `df_integration2` using an outer join and fill missing values with 0.
94. Merge the DataFrames based on 'ID', but only include the 'Price' and 'Quantity' columns in the result.
95. Merge the DataFrames and create a new column 'Total Cost' which is `Price * Quantity`.
96. Merge the DataFrames using the right join.

### **Hard Tasks**
97. Merge the DataFrames and handle duplicate column names by renaming them.
98. Perform a merge with a custom condition (e.g., merge rows where 'Price' is less than 2).
99. Merge the DataFrames and calculate the average quantity for each product.

---
## Statistics

### **Dataset**
```python
import pandas as pd
import numpy as np

statistics_data = {
    'Values': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A']
}

df_statistics = pd.DataFrame(statistics_data)
```

### **Easy Tasks**
100. Calculate the mean and median of the 'Values' column.
101. Find the standard deviation of the 'Values' column.
102. Find the maximum and minimum of the 'Values' column.

### **Medium Tasks**
103. Calculate the variance of the 'Values' column.
104. Calculate the interquartile range (IQR) of the 'Values' column.
105. Calculate the correlation between 'Values' and a new column created by squaring 'Values'.
106. Calculate the skewness of the ‘Values’ column.

### **Hard Tasks**
107. Calculate the z-scores for each value in the 'Values' column.
108. Perform a t-test to compare the mean of 'Values' for group 'A' versus group 'B'.
109. Calculate the covariance between the 'Values' column and a new column that represents the cumulative sum of the 'Values' column.

## 💡 Resources
- [Python Docs](https://docs.python.org/3/)
- [Leetcode](https://leetcode.com/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/)

Happy Coding! 🚀


