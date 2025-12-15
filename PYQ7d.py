#using insertion sort
#      i

lst=[10,2,0,4,50]

#       j

length = len(lst)   #5

for i in range (1,length):
    key = lst[i] 
    j = i-1

    while j>= 0 and lst[j]<key:
        lst[j+1] = lst[j]
        j-=1

        lst[j+1] = key
        print(lst)

print(lst)