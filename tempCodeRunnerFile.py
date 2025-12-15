    for j in range(i+1,len(arr)):
            if arr[j+1] > arr[max_index]:
                max_index = j
        
        arr[i], arr[max_index] = arr[max_index], arr[i]