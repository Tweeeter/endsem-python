def fibonacci():
    terms = int(input("Enter the nth term: "))
    firstterm = 0
    secondterm = 1
    nextterm = 0

    if(terms<=0):
        print("Enter a posotive non negative interger!")
    elif(terms==1):
        print(firstterm)
    else:
        for i in range(1, terms-1):
            nextterm = firstterm + secondterm
            firstterm = secondterm
            secondterm = nextterm
        print(nextterm)
fibonacci()