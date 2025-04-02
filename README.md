## Python Coding Interview Questions for Begineers.
1.Write a Python program to Reverse a String?
2.Write a Python program to Reverse a String in a List? input=["h","e","l","l","o"]
3.Write a Python program to Reverse a array? input=[1,2,3,4,5]
4.Write a Python program to check Palindrome? input="A man, a plan, a canal, Panama" [Leetcode ques:125]
5.Write a Python program to check Palindrome? input=12321
6.Write a Python program to count Vowels in a string? input="Hello,World!"
7.Write a Python Program to find Factorial with Recursion?
8.Write a Python Program to find the Fibonnaci Sequence?
9.Write a Python Program to find Maximum element in the list?
10.Write a Python Program to find the Anagram check?    [Leetcode ques:242]
11.Write a Python Program to find the Prime number?
12.Two SUM [Leetcode ques:1]  input=[2,7,11,15]
13.Longest substring without Repeating characters [Leetcode ques:3] input="abcabcbb"
14.Longest Palindrome substring [Leetcode ques:5] Input: s = "babad" Output: "bab"
15.Top K elements [Leetcode ques:347] input=[1,1,1,2,2,3], k = 2
16.Merge two sorted list? [Leetcode ques:21]   list1=[1,2,4] list2=[1,3,4]
17.Reverse Integer [Leetcode ques:7]
18.Reverse Linked Lists [Leetcode ques:206]
19.Reverse words [Leetcode ques:151] input="Hello world"
20.Missing Number [Leetcode ques:268] nums=[3,0,1]
21.Write a Python program for First Non Repeating characters in a string? s="aabbcdd"
22.Write a Python Program to Move All Zeroes to the End [Leetcode ques:283] input=[0, 1, 0, 3, 12]
23.Write a Python Program to Longest Common prefix? [Leetcode ques:]  input=["flower","flow","flight"]
24.Write a Python Program to Count the Frequency of Words in a String. input="apple banana apple orange banana apple"
25.Write a Python program to Find the Second Largest Number in a List? input=[10, 20, 4, 45, 99]
26.Write a Python Program to Find All Pairs in a List That Sum to a Target ? target=8 input=[1, 2, 3, 4, 5, 6, 7]
27.Write a Python Program to Remove All Duplicates from a String ? input="leetcode"
28.Write a Python Program to check the Armstrong number? input=153
29.Write a Python Program to title case? input="python test"  output="Python Test"
30.Write a Python Program to swap two elements in the list? input=[24,78,90,45,70]

## List Comprehensions...
31.Generate a list of squares of even numbers from 1 to 20 using list comprehension.
32.Convert a list of words into uppercase if they have more than 3 letters, otherwise keep them lowercase.
   words = ["apple", "is", "a", "fruit"]
33.Create a dictionary with numbers as keys and their cubes as values using dictionary comprehension.
34.Flatten a nested list using list comprehension. nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

## Lambda...
35.Sort a list of tuples based on the second value using lambda. pairs = [(1, 3), (2, 2), (4, 1)]
36.Use lambda to create a function that multiplies two numbers.

## Filter()...
37. Filter out even numbers from a list using filter(). nums = [10, 15, 20, 25, 30, 35]
38.Given a list of words, filter only words that start with 'a' using filter(). words = ["apple", "banana", "avocado", "grape", "apricot"]

## Map()...
39.Convert a list of strings into their lengths using map(). words = ["hello", "python", "AI"]

## Zip()....
40.Merge two lists into a dictionary using zip(). keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

41.Add corresponding elements of two lists using zip(). list1 = [1, 2, 3]
list2 = [4, 5, 6]

42.Find the common elements in the lists list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
43.Generate a list of squares for odd numbers using list comprehension and map().

## Pattern Matching Using Regex(Re):
44.Return the number of times the string "code" appears in the given string, except we'll accept any letter for 'd', so "cope", "coze", and "cooe" count. 
print(countCode("aaacodebbb"))  # → 1
print(countCode("codexxcode"))  # → 2
print(countCode("cozexxcope"))  # → 2   [Interview question: Dehezelabs]

45.'''
2.Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.

bobThere("abcbob") → true
bobThere("b9b") → true
bobThere("bac") → false
''' [interview questions:Dehezelabs]

46.'''Given a string, return a string where for every char in the original, there are two chars.

doubleChar("The") → "TThhee"
doubleChar("AAbb") → "AAAAbbbb"
doubleChar("Hi-There") → "HHii--TThheerree"
[interview questions:dehezelabs]

47.Given a string, return a new string where each vowel (a, e, i, o, u, both uppercase and lowercase) is tripled, and each consonant is doubled. Special characters remain unchanged.

transformString("Hello!") → "HHHeellloo!"  
transformString("Python3") →"PPPyyyttthhhoonnn3"  
transformString("AI-Model") →"AAII--Moodddeelll"  

48. input="hgsvhsvhsvsujithhsgvhsvsh hsvhsvshAnanthakrishnansvhssgsv ssvhsvsvReshmasvshvsghvs"

check=["sujith","Ananthakrishnan","Reshma"]

output=["sujith","Ananthakrishnan","Reshma"]

49.Implement Run-Length Encoding

Input: "aaabbc"

Output: "a3b2c1" [string compresion] [Leetcode ques]

## Pandas...
## Data Filtering...
Dataset..
data_filtering_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 30, 22, 35, 28, 40, 27, 32, 29, 31],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'New York', 'London', 'Tokyo', 'Paris', 'New York', 'London'],
    'Salary': [50000, 60000, 45000, 70000, 55000, 80000, 52000, 65000, 58000, 72000]
}
Easy...
50.Filter the DataFrame to show only people older than 30.
51.Filter the DataFrame to show only people living in 'New York'.
52.Filter the DataFrame to display people with a salary greater than 60000.

Meduim:
53.Filter the DataFrame to show people who live in 'London' and are older than 30.
54.Filter the DataFrame to show people who live in either 'New York' or 'Paris'.
55.Filter the DataFrame to show people whose names start with 'A' or 'B'.
56.Filter the dataframe to show the people whose age is between 25 and 35 inclusive.

Hard:
57.Filter the DataFrame to show people whose salary is within one standard deviation of the mean salary.
58.Filter the DataFrame to show people who have the same age as at least one other person in the DataFrame.
59.Filter the DataFrame to show people who have the highest salary within their respective cities.

## String Methods....
Dataset..
string_methods_data = {
    'Email': ['alice@example.com', 'bob.smith@test.co.uk', 'charlie123@domain.net', 'david_jones@mail.org', 'eve.green@sample.io', 'frank.white@web.com', 'grace.black@data.gov', 'hannah.brown@code.ai', 'ivy.gray@info.edu', 'jack.king@network.biz'],
    'Name': ['Alice Smith', 'Bob Smith', 'Charlie Brown', 'David Jones', 'Eve Green', 'Frank White', 'Grace Black', 'Hannah Brown', 'Ivy Gray', 'Jack King'],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm Rd', '202 Maple Dr', '303 Birch Ct', '404 Cedar Pl', '505 Willow Way', '606 Aspen Blvd', '707 Redwood St']
}
Easy..
60.Extract the domain name from the 'Email' column.
61.Convert all names in the 'Name' column to lowercase.
62.Check if each email address contains the word 'example'.

Medium..
63.Extract the first name from the 'Name' column.
64.Count the number of times the letter 'a' appears in each address.
65.Replace all spaces in the 'Address' column with underscores.
66.Create a new column that contain the length of the email address.

Hard:
67.Extract the username from the 'Email' column, handling cases with underscores.
68.Find the longest name in the 'Name' column.
69.Create a new column that contains the initials of the name (e.g., 'Alice Smith' becomes 'AS').

## Data manipulation..
Dataset...
data_manipulation_data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Value1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Value2': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
}

Easy:
70.Create a new column 'Total' that is the sum of 'Value1' and 'Value2'.
71.Rename the 'ID' column to 'RecordID'.
72.Delete the 'Value2' column.
Medium:
73.Create a new column 'Difference' that is the absolute difference between 'Value1' and 'Value2'.
74.Shift the 'Value1' column down by one row.
75.Create a new column that contains the cumulative sum of 'Value1'.
76.Sort the DataFrame by 'Value1' in descending order.

Hard:
77.Pivot the DataFrame to create a new DataFrame where 'ID' is the index, and 'Value1' and 'Value2' are columns.
78.Create a new column that contains the rolling mean of 'Value1' with a window size of 3.
79.Apply a custom function to each element in 'Value1' that doubles the value if it's even and triples it if it's odd.

## Data Aggregration:
Dataset:
data_aggregation_data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 12, 35, 22, 18, 40],
    'Group': ['X', 'Y', 'X', 'Y', 'Z', 'X', 'Z', 'Y', 'X', 'Z']
}
Easy:
80.Calculate the mean of the 'Value' column.
81.Count the number of rows for each category.
82.Find the maximum value for each category.

Meduim:
83.Calculate the sum of 'Value' for each 'Category' and 'Group' combination.
84.Find the median of 'Value' for each 'Category'.
85.Find the standard deviation of 'Value' for each 'Group'.
86.Find the minimum value within each group.

Hard:
87.Calculate the percentage of each category's total value relative to the overall total value.
88.Find the category with the highest average 'Value'.
89.Calculate the rolling average of the 'Value' column grouped by category.
 
## Data Integration:   
axis=0 --> rows axis=1 ---> columns 
Dataset...
data_integration_data1 = {
    'ID': [1, 2, 3, 4, 5],
    'Product': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Price': [1.0, 0.5, 2.0, 1.5, 2.5]
}
data_integration_data2 = {
    'ID': [3, 4, 5, 6, 7],
    'Quantity': [10, 20, 30, 40, 50],
    'Location': ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
}

Easy:
90.Merge df_integration1 and df_integration2 based on the 'ID' column using an inner join.
91.Concatenate df_integration1 and df_integration2 vertically (stack them on top of each other).
92.Merge df_integration1 and df_integration2 using a left join.

Medium:
93.Merge df_integration1 and df_integration2 using an outer join and fill missing values with 0.
94.Merge the DataFrames based on 'ID', but only include the 'Price' and 'Quantity' columns in the result.
95.Merge the DataFrames and create a new column 'Total Cost' which is Price * Quantity.
96.Merge the DataFrames using the right join.

Hard:
97.Merge the DataFrames and handle duplicate column names by renaming them.
98.Perform a merge with a custom condition (e.g., merge rows where 'Price' is less than 2).
99.Merge the DataFrames and calculate the average quantity for each product.

## Statistics..
Dataset...
statistics_data = {
    'Values': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Group': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'A']
}

Easy:
100.Calculate the mean and median of the 'Values' column.
101.Find the standard deviation of the 'Values' column.
102.Find the maximum and minimum of the 'Values' column.

Medium:
103.Calculate the variance of the 'Values' column.
104.Calculate the interquartile range (IQR) of the 'Values' column.
Formulae is IQR=Q3-Q1
105.Calculate the correlation between 'Values' and a new column created by squaring 'Values'.
106.Calculate the skewness of the ‘Values’ column.

Hard:
107.Calculate the z-scores for each value in the 'Values' column.
108.Calculate the covariance between the 'Values' column and a new column that represents the cumulative sum of the 'Values' column.
