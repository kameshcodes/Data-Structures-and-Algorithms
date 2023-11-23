def binary_search(arr, target, low, high):
    if high >= low:
        mid = low + (high-low) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
            return binary_search(arr, target, low, high)
        else:
            high = mid - 1 
            return binary_search(arr, target, low, high)
    else:
        return False     
        
arr = [33, 16, 23, 45, 65, 35, 54, 4]
arr = sorted(arr)
target = 54

result = binary_search(arr, target, 0, len(arr)-1)

if result == True:
    print("Element Found")
else:
    print("Element not found")