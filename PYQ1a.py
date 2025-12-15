#0, 1, 1, 2, 3, 5, 8, 13, 21
#itterative


def fibinacci():
    terms = int(input("Enter number of terms you want: "))
    firstTerm = 0
    secondTerm = 1
    next = 0
    if(terms <= 0):
        print("Enter a positive integer value")
    elif(terms == 1):
        print(firstTerm)
    else:
        print(firstTerm)
        print(secondTerm)
        for i in range(1,terms-1):
            next = firstTerm + secondTerm
            print(next)
            firstTerm = secondTerm
            secondTerm = next


fibinacci()