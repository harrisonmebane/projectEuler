## This problem is in progress! ##

"""Statement: Starting with $1, if you bet some fraction f
of your money that a coin will land heads, and do this
1000 times in a row (with the same f), what are the odds 
you'll make at least a billion dollars?"""

import sys

def n_flips(frac,n,thresh):
    
    over_thresh = 0
    heads = 0
    for bits in range(2**n):
        money = 1.
        for flip in range(n):
            if (1<<flip)&bits:
                money += frac*money
                heads += 1
            else:
                money -= frac*money
        if money >= thresh:
            over_thresh += 1
            
    print heads/float(2**n)
    return over_thresh/float(2**n)

#frac = float(sys.argv[1])
#n = int(sys.argv[2])
#thresh = int(sys.argv[3])
#print n_flips(frac,n,thresh)
