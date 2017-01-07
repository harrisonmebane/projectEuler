def palindrome(s):
    for i in range(len(s)/2):
        if not s[i]==s[-i-1]:
            break
    else:
        return True

pal_list = []

for i in range(1000000):
    if i % 2:
        dec = str(i)
        bi = bin(i)[2:]
        if palindrome(dec) and palindrome(bi):
            pal_list.append(i)

print sum(pal_list)
