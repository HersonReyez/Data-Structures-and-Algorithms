
## Heaps ##
# representation of tree like list
# heap the most vaule big/small at the top and 

## Min Heap ##
# Build Min Heap(Heapify) - O(n)
import heapq
minHeap = [-4, 3, 1, 0, 2, 5, 10, 8 ,12, 9]
heapq.heapify(minHeap) 

print("Tree min heap:",minHeap)

# Heap push (insert element) - O(log n)
num = 20
heapq.heappush(minHeap, num)
print("add", num,"to the tree:", minHeap)

# Heap pop (extract min)
vauleMin = heapq.heappop(minHeap)
print("extract", vauleMin, "of the tree:", minHeap)

# Heap push pop - O(log n)
num = 21
vauleMin = heapq.heappushpop(minHeap, num)
print("add", num, "and delete", vauleMin, "to the tree:", minHeap)

## Max Heap ##
# Use the same that Min Heap but the vaules negattives
maxHeap = [-4, 3, 1, 0, 2, 5, 10, 8 ,12, 9]
n = len(maxHeap )

for i in range(n):
    maxHeap [i] = -maxHeap [i]

heapq.heapify(maxHeap )

print("Tree Max Heap:", end=" ")
for i in range(n):
    print(-maxHeap [i],end=" ")
print()

# Heap pop (extract max) 
largest = -heapq.heappop(maxHeap )
n = n-1
print("extract", largest, "of the tree:", end=" ")
for i in range(n):
    print(-maxHeap [i], end=" ")
print()

## Build heap from scratch - Time: O(n log n)
vaules = [-4, 3, 1, 0, 2, 5, 10, 8 ,12, 9]
heap = []

print("Build heap from scratch")
for x in vaules:
    heapq.heappush(heap, x)
    print(heap)

## Putting tuples of items on the heap
# couter repetition of vaules 
from collections import Counter
vaules = [2, 3, 3, 1, 2, 3, 1, 1, 1]
counter = Counter(vaules)

heapTuples = []

for k, v in counter.items():
    heapq.heappush(heapTuples, (v,k))

print("Heap with tuples (frecuency, vaule): ", heapTuples)


## Heap Sort ##
# heap Sort - O(n log n) 
# NOTE: o(1) Space is possible via swapping, but this is complex
def heapsort(array):
    heapq.heapify(array)
    n = len(array)
    newList = [0] * n

    for i in range(n):
        vauleMin = heapq.heappop(array)
        newList[i] = vauleMin
    return newList

unorderedList = [1, 5, 2, 0, 2, 4]
orderedList = heapsort(unorderedList)
print("list ordered with Heap Sort:",orderedList)