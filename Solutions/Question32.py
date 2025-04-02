input=["apple", "is", "a", "fruit"]
result=[words.upper() if len(words)>3 else words.lower() for words in input]
print(result)