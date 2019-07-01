string = input()

result = ""

vowels = ['a','e','i','o','u','y']

for i in string:
    if i.lower() in vowels:
        continue
    else:
        result += '.' + i.lower()
    
print(result)
