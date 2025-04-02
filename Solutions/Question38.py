words = ["apple", "banana", "avocado", "grape", "apricot"]
result=list(filter(lambda word:word.startswith('a'),words))
print(result)