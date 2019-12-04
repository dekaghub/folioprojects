import math

# To count the number of comparisons
count = 0

def Merge(A,p,q,r):
    
    global count

    n1 = q - p + 1
    n2 = r - q

    Left = [0] * (n1 + 1)
    Right = [0] * (n2 + 1)

    for i in range(0, n1):
        Left[i] = (A[p+i])
    for i in range(0,n2):
        Right[i] = (A[q+1+i])

    Left[n1]=math.inf
    Right[n2]=math.inf

    i = j = 0
    count = 0

    for k in range (p, r+1):
        if Left[i] <= Right[j]:
            A[k] = Left[i]
            i += 1
            count +=1
        else:
            A[k] = Right[j]
            j += 1
            count +=1

def MergeSort (A,p,r):

    if p<r:
        q = math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)
