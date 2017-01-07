def prime_list(n):
    l = []
    for i in xrange(2,n+1):
        for prime in l:
            if prime>i**.5:
                l.append(i)
                break
            if i%prime==0:
                break
        else:
            l.append(i)

    d = {}
    for prime in l:
        d[prime]=1
        
    return d

def cycles(n):
    num = list(str(n))
    cycles = []
    for i in range(len(num)-1):
        num.insert(0,num.pop())
        cycles.append(int(''.join(num)))
    return cycles

def find_cyclic_primes(n):
    cyclic_primes = []
    primes = prime_list(n)
    for i in primes.keys():
        for j in cycles(i):
            if not primes.get(j):
                break
        else:
            cyclic_primes.append(i)
    return cyclic_primes

print find_cyclic_primes(1000000)
