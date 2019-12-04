from CoinChangeDynamic import dynamicCoinChange
import time as t

# Example input: 4,6,9,15
k = input ('Type in an array of denominations (use comma e.g. 1,2,3) : ')
item = input ('Type in the Change amount : ')
item = int(item)
deno = k.split(',')
deno = [int(i) for i in deno]
print('Denominations : ', deno)
print('Change : ', item)
print('Result : ', dynamicCoinChange(item,deno))

start = t.perf_counter_ns()
coins = dynamicCoinChange(item,deno)
end = t.perf_counter_ns()

# Write to file operations
output = open('output_dynamic_userInput.txt', 'w+')
text = 'User input : ' + str(item) + '\n'
output.write(text)
text = 'Coin Denominations : ' + str(deno).strip('[]') + '\n'
output.write(text)
output.write('\n\nChange\tCoins\tTime Taken\n')
text = str(item) + '\t' + str(coins) + '\t' + str(end-start) + ' ns\n'
output.write(text)

output.close()