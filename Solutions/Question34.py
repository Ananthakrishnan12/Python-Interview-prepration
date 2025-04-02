nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flatten_list=[num for sublist in nested_list for num in sublist]
print(flatten_list)