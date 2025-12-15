#0, 1, 1, 2, 3, 5, 8, 13, 21
#Recuesive

def fibonacci(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return (fibonacci(i-1) + fibonacci(i-2))

terms = int(input("Enter number of terms: "))
if terms <= 0:
    print("enter a positive non zero integer")
else:
    for i in range (1, terms+1):
        print(fibonacci(i))