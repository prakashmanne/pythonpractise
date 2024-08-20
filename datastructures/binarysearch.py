def binarysearch(arr, target):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 4, 5, 7, 8, 9]
target = 7
result = binarysearch(arr, target)
if result != -1:
    print(f"The index of that element is {result}")
else:
    print("Not found")