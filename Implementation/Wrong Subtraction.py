myInput = [int(x) for x in input().split(" ")]

value = myInput[0]
diff = myInput[1]

del(myInput)

result = 0

while  diff != 0:
    if(value%10 == 0):
        result = value//10
        value = value // 10
    else:
        result = value - 1
        value = value - 1
    diff -= 1
print(result)