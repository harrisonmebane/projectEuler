

def divisor_list(n):

    div_list = [1]
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            if float(n)/i == i:
                div_list.append(i)
            else:
                div_list.append(i)
                div_list.append(n/i)

    return div_list
    
amicable = []
d = {}
for i in range(1,10000):
    tot = sum(divisor_list(i))
    if i<tot:
        d[i]=tot
    elif i>tot:
        if d.get(tot) == i:
            amicable.append(i)
            amicable.append(tot)

print sum(amicable)
