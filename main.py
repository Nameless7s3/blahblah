import time

#COIN SPLIT

def coinSplit(m):
    return coinSplitRec(m,0)

def coinSplitRec(m, i):
    if m == 0:
        return 0
    if i == len(coin)-1:
        return m
    withoutIt = coinSplitRec(m,i+1)
    if coin[i] <= m:
        withIt = 1 + coinSplitRec(m-coin[i],i)
        if withIt < withoutIt:
            return withIt
    return withoutIt





#COIN SPLIT DP

def coinSplitDP(m):
    # memo is a hash map with keys of the form (m,lo)
    memo = {}
    return coinSplitMem(m,0,memo)

def coinSplitMem(m, lo, memo):  # split m using the coin[lo:]
    if (m,lo) in memo:  # have I already calculated the best split for (m,lo)?
        return memo[m,lo]
    if m == 0:
        memo[m,lo] = 0
    elif lo == len(coin)-1:
        memo[m,lo] = m
    else:
        withoutIt = coinSplitMem(m,lo+1,memo)
        memo[m,lo] = withoutIt
        if coin[lo] <= m:
            withIt = 1 + coinSplitMem(m-coin[lo],lo,memo)
            if withIt < withoutIt:
                memo[m,lo] = withIt
    return memo[m,lo]




#COIN SPLIT DP BU

def coinSplitDPBU(mInit):
    memo = {}
    for i in range(len(coin)):
        memo[0,i] = 0
    for m in range(mInit+1):
        memo[m,len(coin)-1] = m
    for m in range(1,mInit+1):
        for i in range(len(coin)-2,-1,-1):
            withoutIt = memo[m,i+1]
            memo[m,i] = withoutIt
            if coin[i] <= m:
                withIt = 1 + memo[m-coin[i],i]
                if withIt < withoutIt:
                    memo[m,i] = withIt
    return memo[mInit,0]



def coinSplitTime(n):
    startTime = time.time()
    res = coinSplit(n)
    return str(time.time() - startTime)

def coinSplitTimeDP(n):
    startTime = time.time()
    res = coinSplitDP(n)
    return str(time.time() - startTime)

def coinSplitTimeDPBU(n):
    startTime = time.time()
    res = coinSplitDPBU(n)
    return str(time.time() - startTime)

def runTests(coins, testN):
    print(coins)
    for k in testN:
        res1 = coinSplitTime(k)
        print("Coin split took: " + res1 + "s for: " + str(k))
        res2 = coinSplitTimeDP(k)
        print("Coin split DP took: " + res2 + "s for: " + str(k))
        res3 = coinSplitTimeDPBU(k)
        print("Coin split DPBU took: " + res3 + "s for: " + str(k))

testArray = [10,100,1000,10000]
#coin = [200,100,50,20,5,2,1]
#runTests(coin, testArray)
coin = [i for i in range(200,0,-1)]
runTests(coin, testArray)
