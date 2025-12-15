def palindrome():
    sequence = input("Enter a String: ")
    sequence = sequence.lower()
    sequence = sequence.replace(" ","")
    reversed_string = ""
    for i in range(len(sequence)-1,-1,-1):
            reversed_string = reversed_string + sequence[i]
    print(reversed_string)
    if sequence == reversed_string:
          print("Palindrome")
    else:
        print("Not Palindrome") 

palindrome()