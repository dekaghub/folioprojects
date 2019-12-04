import HeapSort
import MergeSort
import InsertionSort
import random as r


test = []
for i in range(10):
    test.append(r.randint(1,25))

HeapSort.heapSort(test)
print('HeapSort Result : ', test)

test = []
for i in range(10):
    test.append(r.randint(1,25))
print('InsertionSort Result : ', InsertionSort.insertion_sort(test))

test = []
for i in range(10):
    test.append(r.randint(1,25))

MergeSort.MergeSort(test, 0, len(test)-1)
print('MergeSort Result : ', test)