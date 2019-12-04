from CoinChangeGreedyCode import greedyChange
import time as t


k = input ('Type the number of denominations : ')
deno = []
for i in range(int(k)):
    deno.append(int(input()))
item = input ('Type in the Change amount : ')
item = int(item)

print('Denominations : ', deno)
print('Change : ', item)
print('Result : ', greedyChange(item,deno))

start = t.perf_counter_ns()
coins = greedyChange(item,deno)
end = t.perf_counter_ns()

# Write to file operations
output = open('output_greedy.txt', 'w+')
text = 'User input : ' + str(item) + '\n'
output.write(text)
text = 'Coin Denominations : ' + str(deno).strip('[]') + '\n'
output.write(text)
output.write('\n\nChange\tCoins\tTime Taken\n')
text = str(item) + '\t' + str(coins) + '\t' + str(end-start) + ' ns\n'
output.write(text)

output.close()