
d = {}
d[(1,1)] = 2

def num_paths(m,n):

    if m==0 or n==0:
        return 1
    elif d.get((m,n)):
        return d[(m,n)]
    first = num_paths(m-1,n)
    d[(m-1,n)] = first
    second = num_paths(m,n-1)
    d[(m,n-1)] = second
    return first+second

def get_all_paths(n):

    for i in range(1,n+1):
        print "%i: %i" % (i,num_paths(i,i))
        
