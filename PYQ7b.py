#using bubble sort
list = [10, 2, 0, 50, 4]
length = len(list)
for i in range(length):
    for j in range(i+1,length):
        if list[i]<list[j]:
            list[i], list[j] = list[j], list[i]

print(list)
