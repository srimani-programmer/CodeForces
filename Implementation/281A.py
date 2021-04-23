string = input()

result = ""

for i in range(0, len(string)):
    if(i == 0):
        result += string[i].upper()
    else:
        result += string[i]

print(result)
