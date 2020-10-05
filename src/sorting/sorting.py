# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements= len(arrA) + len(arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    pointer_a = 0
    pointer_b = 0

    for x in range(elements):
        if pointer_a >= len(arrA):
            merged_arr[x] = arrB[pointer_b]
            pointer_b += 1
        elif pointer_b >= len(arrB):
            merged_arr[x] = arrA[pointer_a]
            pointer_a += 1
        elif arrA[pointer_a] > arrB[pointer_b]:
            merged_arr[x] = arrB[pointer_b]
            pointer_b += 1
        elif arrB[pointer_b] > arrA[pointer_a]:
            merged_arr[x] = arrA[pointer_a]
            pointer_a += 1
    



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2 :
        return arr
    mid= len(arr) // 2
    left= arr[0:middle]
    right= arr[middle:len(arr)]
    return merge(merge_sort(left),merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
