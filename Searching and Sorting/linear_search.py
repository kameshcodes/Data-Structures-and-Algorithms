def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


arr = [33, 16, 23, 45, 65, 35, 54]
target = 65

result = linear_search(arr, target)

if result:
    print("Element Found")
else:
    print("Element not found")