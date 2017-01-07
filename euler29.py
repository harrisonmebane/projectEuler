

def find_distinct(n,m):

    powers = {}
    for i in range(2,int(n**.5)+1):
        p = 2
        while i**p<=n and p<=m:
            if powers.get(i**p):
                p+=1
                continue
            powers[i**p]=(i,p)
            p+=1

    num_distinct = 0
    for i in range(2,n+1):
        if i not in powers.keys():
            num_distinct += m-1
        else:
            base,exp = powers[i]
            for b in range(2,m+1):
                for small_exp in range(1,exp):
                    if b*exp<=small_exp*m and b*exp % small_exp == 0:
                        print base,exp,b
                        break
                else:
                    num_distinct += 1

    print num_distinct
