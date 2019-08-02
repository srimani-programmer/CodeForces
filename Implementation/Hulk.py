n = int(input())

result = ""
odd_text = 'I hate'
even_text = 'I love'
special_text1 = 'that'
special_text2 = 'it'

for i in range(1,n+1):
    if(i%2 == 1 and i != n):
        result += odd_text + " " + special_text1
    elif(i%2 == 0 and i != n):
        result += even_text + " " + special_text1
    else:
        if(i%2 == 0):
            result += even_text + " " + special_text2
        else:
            result += odd_text + " " + special_text2
    
    result += " "

    

print(result.strip())
