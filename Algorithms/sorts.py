## Merge Sort ##
# O(n long n ) - NOTE: can ve log n, but this is harder to write
def merge_sort(array):
    n = len(array)

    if n == 1:
        return array
    
    m = len(array) // 2
    left = array[:m]
    right = array[m:]

    left = merge_sort(left)
    right = merge_sort(right)

    l, r = 0, 0
    L_len = len(left)
    R_len = len(right)
    sortedArray = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if left[l] < right[r]:
            sortedArray[i] = left[l]
            l += 1
        else:
            sortedArray[i] = right[r]
            r += 1
        i += 1

    while l < L_len:
        sortedArray[i] = left[l]
        l += 1
        i += 1

    while r < R_len:
        sortedArray[i] = right[r]
        r += 1
        i += 1

    return sortedArray

unorderedList = [1, 5, 2, 0, 2, 4]
orderedList = merge_sort(unorderedList)
print("list ordered with Merge Sort:", orderedList)


## Quick Sort ##
# O(n log n) - NOTE: Average case, technically Worst case is O(n^2)
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivote = array[-1]
    left = [x for x in array[:-1] if x <= pivote]
    rigth = [x for x in array[:-1] if x > pivote]

    left = quick_sort(left)
    rigth = quick_sort(rigth)

    return left + [pivote] + rigth

unorderedList = [1, 5, 2, 0, 2, 4]
orderedList = quick_sort(unorderedList)
print("list ordered with Quick Sort:", orderedList)


## Couting sort ##
#O(n + k) where k is the range of data
#NOTE: this can be written negative arrays,
# but we'll stick to positive arrays,
# so k is the max of the array

def couting_sort(array):
    n = len(array)
    maxValue = max(array)
    counts = [0] * (maxValue + 1)
    newArray = [0] * n

    for x in array:
        counts[x] += 1

    i = 0
    for c in range(maxValue + 1):
        while counts[c] > 0:
            newArray[i] = c
            i += 1
            counts[c] -= 1

    return newArray

unorderedList = [1, 5, 2, 0, 2, 4]
orderedList = couting_sort(unorderedList)
print("list ordered with Countig Sort:", orderedList)