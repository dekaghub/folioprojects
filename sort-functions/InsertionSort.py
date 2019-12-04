# Basic insertion sort
def insertion_sort(A):

    for j in range(1, len(A)):
        key = A[j]
        i = j-1

        while (i>=0) and (A[i]>key):
                A[i+1] = A[i]
                i = i-1
        A[i+1] = key

    return A

# Insertion sort that saves the total number of comparisons
count = 0

def insertion_sort_comparison(A):
   
    global count

    for j in range(1, len(A)):
        key = A[j]

        for i in range (j-1, j):
            while(i>=0):
                if key < A[i]:
                    A[i+1]=A[i]
                    i=i-1
                    count+= 1
                else:
                    count+=1
                    i=i-1
            A[i+1]=key
    return count

# Test code to try count
# test = []
# for i in range(100, 0, -1):
#     test.append(i)

# print(insertion_sort_comparison(test))