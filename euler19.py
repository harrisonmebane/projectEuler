

num = 31+28+31+30+31+30+31+31+30+31+30+31
count = 0

for year in range(1,101):
    for month in range(1,13):
        if num % 7 == 6:
            count += 1

        if month in (4,6,9,11):
            num += 30
        elif month == 2:
            if year % 4 == 0:
                num += 29
            else:
                num += 28
        else:
            num += 31

print count
