l = (1,2,5,10,20,50,100,200)

def num_ways(n,m):

    if n<=1:
        return 1

    coins = filter(lambda x: x<=min(m,n),l)
    ways = 0

    for coin in coins:
        ways += num_ways(n-coin,coin)
    return ways

def num_ways2(n,m):

    if n<=1:
        return 1

    ways = 0

    for i in range(m,-1,-1):
        if n<l[i]:
            continue
        ways += num_ways2(n-l[i],i)
    return ways
    
