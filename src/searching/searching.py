# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    arr.sort()
    middle=(start + end) // 2
    if end >= start:
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            return binary_search(arr,target,start,middle - 1)
        elif arr[middle] < target:
            return binary_search(arr,target,middle + 1,end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    #find the middle point in the array
    #There are 2 scenerios : 1 is that the array is in ascending order
    #The order is that the array will be in descending order
    start= 0
    end = len(arr) - 1
    while end >= start:
        middle=(start + end) // 2
        next_one= middle + 1
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            if arr[next_one] > arr[middle]:
                end= middle - 1
            if arr[next_one] < arr[middle]:
                start= middle + 1
        elif arr[middle] < target:
            if arr[next_one] > arr[middle]:
                start= middle + 1
            if arr[next_one] < arr[middle]:
                end= middle -1
    return -1