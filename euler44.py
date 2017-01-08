# Need to generate one pentagonal number at a time, and check
# difference with all of the existing ones. Keep track of the
# difference pairs, and each time you find a new difference, check if
# the corresponding sum is already a difference pair. Then keep going
# until the difference is smaller than consecutive numbers.
#
# Notes: Used dict for quick lookup, list for ordering.
# 
# Time: 126ms


def pent_num(n):
    return int(n*(3*n-1)*.5)

def smallest_diff():
    pent_num_dict = {pent_num(1):1}
    pent_nums = [pent_num(1)]
    diffs = {}
    diff = 0
    i = 2
    # The second condition would guarantee minimum diff, but takes too long
    while ((not diff)): # or (pent_nums[-1]-pent_nums[-2]<diff)):
        new_num = pent_num(i)
        # Go through backwards since there are fewer nums > new_num/2 than <
        for n in pent_nums[::-1]:
            # Will find all diff pairs by going through half the range
            if n < new_num/2: break
            if new_num-n in pent_num_dict:
                if (new_num-n, n) in diffs:
                    diff = diffs[(new_num-n, n)]
                diffs[(n, new_num)] = new_num-n
                diffs[(new_num-n, new_num)] = n
        pent_num_dict[new_num] = 1
        pent_nums.append(new_num)
        i += 1
    return diff

print smallest_diff()
