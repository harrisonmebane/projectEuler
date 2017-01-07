def pandigital(a,b,c):
    l = [0]*9
    all_nums = list(str(a)+str(b)+str(c))
    for digit in all_nums:
        digit = int(digit)
        if digit==0 or l[digit-1]==1:
            return False
        else:
            l[digit-1]=1
    return True

def get_unique_digit_nums(a,b):
    unique_nums = []
    for i in range(a,b):
        l = [0]*9
        digits = list(str(i))
        for digit in digits:
            digit = int(digit)
            if digit==0 or l[digit-1]==1:
                break
            else:
                l[digit-1]=1
        else:
            unique_nums.append(i)
    return unique_nums

d = {}

for i in range(1,10):
    for j in get_unique_digit_nums(1234,9877):
        if i*j>9999:
            break
        if pandigital(i,j,i*j):
            d[i*j]=1

for i in get_unique_digit_nums(11,100):
    for j in get_unique_digit_nums(123,988):
        if i*j>99999:
            break
        if pandigital(i,j,i*j):
            d[i*j]=1
print d.keys()
print sum(d.keys())
