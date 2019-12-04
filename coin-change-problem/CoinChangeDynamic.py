def dynamicCoinChange( A, k=[25,10,5,1] ):

	DPStack = [0 for i in range(0, A+1)]
	
	n = len(k)
	for i in range(1, A+1):
		smallest = float("inf")
		for j in range(0, n):
			if (k[j] <= i):
				smallest = min(smallest, DPStack[i - k[j]]) 
		DPStack[i] = 1 + smallest 
	return DPStack[A]