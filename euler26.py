
max_count = 1
max_count_int = 0
for i in range(7,1000):
    if i % 2 and i % 3 and i % 5:
        x = 10
        count = 1
        while x % i != 1:
            x *= 10
            count += 1
        if count > max_count:
            max_count = count
            max_count_int = i

print "Max count int:", max_count_int
print "Repetition:", max_count
