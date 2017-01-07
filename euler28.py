
tot = 1
size = 1
inc = 2
num = 1
while size < 1001:
    for i in range(4):
        num += inc
        tot += num
    size += 2
    inc += 2

print tot
