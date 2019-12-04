# Heapsort, Heapify, BuildHeap
# Use heapsort to sort any random list

# Count the number of comparisons
count = 0

def left(i):
    return (2*i)+1

def right(i):
    return (2*i) + 2

def heapify(A, i, heapsize = None):

    global count

    if heapsize is None:
        heapsize = len(A)
    l = left(i)
    r = right(i)
    
    if l < heapsize and A[l] > A[i]:
        largest = l
        count += 1
    else:
        largest = i
        count += 1
    if r < heapsize and A[r] > A[largest]:
        largest = r
        count += 1
    if  largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heapsize)

def build_Heap(A):
    for i in range(len(A)//2, -1, -1):
        heapify(A, i)

def heapSort(A):

    build_Heap(A)
    heapsize = len(A)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        heapify(A, 0, heapsize)
