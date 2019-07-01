n = int(input())

while n != 0:

    string = input()

    if(len(string) <= 10):
        print(string)
    else:
        print(string[0] + str(len(string)-2) + string[-1])
    
    n = n - 1