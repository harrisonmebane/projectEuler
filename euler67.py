

def find_largest_sum(triangle):

    if len(triangle)==1:
        return triangle[0][0]

    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(triangle[-1][i],triangle[-1][i+1])

    return find_largest_sum(triangle[:-1])

with open('euler67.in','rb') as infile:
    starting_tri = map(lambda x: x[:-1].split(" "), list(infile))
    starting_tri = map(lambda x: map(int,x), starting_tri)

print find_largest_sum(starting_tri)
