

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

abundant = []

for i in range(1,28124):
    if sum(divisor_list(i)) > i:
        abundant.append(i)

sums = {}
for i in range(len(abundant)):
    for j in range(i,len(abundant)):
        sums[abundant[i]+abundant[j]]=1
print 28124 in sums

tot = 0
for i in range(28124):
    if not sums.get(i):
        tot+=i

print tot
