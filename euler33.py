for i in range(10,100):
    num = list(str(i))
    if num[0]==num[1]:
        continue
    for j in range(i+1,100):
        num = list(str(i))
        den = list(str(j))
        if num[1]=='0' and den[1]=='0':
            continue
        if den[0]==den[1]:
            continue
        if (den[0] in num and den[1] not in num):
            num.remove(den[0])
            den = float(den[1])
            num = float(num[0])
            if den==0:
                continue
            if num/den == float(i)/float(j):
                print i,"/",j
        elif (den[1] in num and den[0] not in num):
            num.remove(den[1])
            den = float(den[0])
            num = float(num[0])
            if den==0:
                continue
            if num/den == float(i)/float(j):
                print i,"/",j
                
