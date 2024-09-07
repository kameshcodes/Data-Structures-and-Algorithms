def selection(arr):
    for i in range(len(arr)-1):
        min_ = i
        for j in range(i+1, len(arr)):
            if arr[min_]>arr[j]:
                min_ = j
        arr[min_], arr[i] = arr[i], arr[min_]
        
    return arr
    
    
    
arr = [4, 1, 3, 9, 7]
print(selection(arr))