from CoinChangeDynamic import dynamicCoinChange
import time as t

# Standard coin change problem
# Enter denomination count -> denominations -> Change - Result


k = input ('Type the number of denominations : ')
deno = []
for i in range(int(k)):
    deno.append(int(input()))
item = input ('Type in the Change amount : ')
item = int(item)

print('Denominations : ', deno)
print('Change : ', item)
print('Result : ', dynamicCoinChange(item,deno))

start = t.perf_counter_ns()
coins = dynamicCoinChange(item,deno)
end = t.perf_counter_ns()

# Write to file operations
output = open('output_dynamic.txt', 'w+')
text = 'User input : ' + str(item) + '\n'
output.write(text)
text = 'Coin Denominations : ' + str(deno).strip('[]') + '\n'
output.write(text)
output.write('\n\nChange\tCoins\tTime Taken\n')
text = str(item) + '\t' + str(coins) + '\t' + str(end-start) + ' ns\n'
output.write(text)

output.close()