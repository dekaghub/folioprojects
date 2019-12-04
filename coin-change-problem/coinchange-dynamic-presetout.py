from CoinChangeDynamic import dynamicCoinChange
import time as t

# replace values here to test. test: Change list, k: Denomination list
test = [3,4,5,7,8,10,23,25,27,29,35,50,75,78]
k = [25,10,5,1]

if __name__ == '__main__':

    output = open('output_dynamic_preSet.txt', 'w+')
    text = 'Test cases : ' + str(test).strip('[]') + '\n'
    output.write(text)
    text = 'Coin Denominations : ' + str(k).strip('[]') + '\n'
    output.write(text)
    output.write('\n\nChange\tCoins\tTime Taken\n')

    for item in test:
        start = t.perf_counter_ns()
        coins = dynamicCoinChange(item,k)
        end = t.perf_counter_ns()

        text = str(item) + '\t' + str(coins) + '\t' + str(end-start) + ' ns\n'
        output.write(text)

    output.close()