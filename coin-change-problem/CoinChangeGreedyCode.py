# A: Change amount, k: Denomination List/Array
def greedyChange(A,k):

    coins = 0

    if A == 0:
        return coins
    elif A in k:
        coins = A
        return coins
    
    Deno = k
    Deno.sort(reverse = True)

    for i in Deno:
        while(A//i > 0):
            coins += 1
            A -= i

    return coins