from CoinChangeRecursiveCode import recursiveChange
import time as t
import multiprocessing as m


if __name__ == '__main__':
    k = input ('Type the number of denominations : ')
    deno = []
    for i in range(int(k)):
        deno.append(int(input()))
    item = input ('Type in the Change amount : ')
    item = int(item)

    runFlag = 0


    p = m.Process(target=recursiveChange, args=(item,deno))
    p.start()
    p.join(60)

    if p.is_alive():
        print('This computation has exceeded a minute and will now terminate!')
        Errortext = "Execution terminated before completion!"

        p.terminate()
        p.join()
        runFlag = 3

    if runFlag == 0:
        start = t.perf_counter_ns()
        coins = recursiveChange(item,deno)
        end = t.perf_counter_ns()
        runFlag = 1

    # Write to file operations
    output = open('output_recursion.txt', 'w+')
    if runFlag == 1:
        text = 'User input : ' + str(item) + '\n'
        output.write(text)
        text = 'Coin Denominations : ' + str(deno).strip('[]') + '\n'
        output.write(text)
        output.write('\n\nChange\tCoins\tTime Taken\n')
        text = str(item) + '\t' + str(coins) + '\t' + str(end-start) + ' ns\n'
        output.write(text)
    elif runFlag == 3:
        output.write(Errortext)

    output.close()