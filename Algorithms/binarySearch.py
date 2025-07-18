listA = list()
for i in range(100):
    listA.append(i)

#Looking up if number is in list - O(log n)
def binarySearch(orderedList, value):
    N = len(orderedList)
    L = 0
    R = N - 1
    while L <= R:
        M = L + ((R - L) // 2)

        if orderedList[M] == value:
            return True
        elif orderedList[M] > value:
            R = M - 1
        else: 
            L = M + 1

    return False

print(binarySearch(listA, 99))

# Condition based
# Find the change
listB = [False, False, False, True, True]

def binarySearchCondition(booleanList):
    N = len(booleanList)
    L = 0
    R = N - 1
    while L < R:
        M = L + ((R - L) // 2)

        if booleanList[M]:
            R = M
        else:
            L = M + 1

    return L
