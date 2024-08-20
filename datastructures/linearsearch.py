def linearsearch(arr,target1):
    for i in range(len(arr)):
        if arr[i]==target1:
            return i
    return -1
arr=[1,2,6,8,5]
target=5
target1=6
result=linearsearch(arr,target1)
if result!=-1:
    print(f"element found:{result}")
else:
    print("not found")


