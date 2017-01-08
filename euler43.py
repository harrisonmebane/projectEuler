# Notes:
# Too many 10-digit numbers to iterate through
# Too many 10-digit permutations to generate all pandigitals
# Need to check for conditions as the numbers are built.

def gen_list(s = ''):
    nums_left = set('0123456789') - set(s)
    l = []
    for n in nums_left:
        new_s = s + n
        if len(new_s) == 1 and new_s == '0':
            continue
        elif len(new_s) == 4 and int(new_s[1:]) % 2 != 0:
            continue
        elif len(new_s) == 5 and int(new_s[2:]) % 3 != 0:
            continue
        elif len(new_s) == 6 and int(new_s[3:]) % 5 != 0:
            continue
        elif len(new_s) == 7 and int(new_s[4:]) % 7 != 0:
            continue
        elif len(new_s) == 8 and int(new_s[5:]) % 11 != 0:
            continue
        elif len(new_s) == 9 and int(new_s[6:]) % 13 != 0:
            continue
        elif len(new_s) == 10:
            if int(new_s[7:]) % 17 == 0:
                return [int(new_s)]
        else:
            l += gen_list(new_s)
    return l

print(sum(gen_list()))
