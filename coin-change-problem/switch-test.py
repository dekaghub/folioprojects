from CoinChangeDynamic import dynamicCoinChange

def predefined():
	test = [3,4,5,7,8,10,23,25,27,29,35,50,75,78]
	k = [25,10,5,1]
	print('Test array : ', test)
	print('Denomination array : ', k)

	for item in test:
		print(dynamicCoinChange(item, k))

def userInput():
	x = input ('Type in an array of denominations (use comma e.g. 1,2,3) : ')
	y = input ('Type in the Change : ')
	y = int(y)
	t = x.split(',')
	t = [int(i) for i in t]
	print('Denominations : ', t)
	print('Change : ', y)
	print('Result : ', dynamicCoinChange(y,t))

def switch(x):
	switcher = {
		1: predefined,
		2: userInput,
		3: exit()
	}

x = input('Type 1 to use predefined test cases or 2 to enter custom values or 3 to exit: ')
x = int(x)
print(switch(x))

