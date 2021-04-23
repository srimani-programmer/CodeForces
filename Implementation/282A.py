t = int(input())

X = 0

for i in range(t):
    string = input()
    if('++' in string):
        X += 1
    elif('--' in string):
        X -= 1

print(X)
