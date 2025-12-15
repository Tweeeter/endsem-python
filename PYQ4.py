def sum_item():
    dictionary = {'apple':5,
                  'pineapple': 4,
                  'orange': 3,
                  'banana': 2,
                  'grape':1} 
    total = 0
    for i in dictionary.values():
        total = total + i
    print(total)
sum_item()