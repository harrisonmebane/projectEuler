def hex_nums(init):
    i = init
    while True:
        yield i*(2*i-1)
        i += 1

def nearest_pent_num(x):
    # n(3n-1)/2 = x
    # 3n^2 - n - 2x = 0
    # n = 1/6(1 + sqrt(1 + 24x)) 
    return int((1 + (1+24*x)**.5)/6.)

def nearest_tri_num(x):
    # n(n+1)/2 = x
    # n^2 + n - 2x = 0
    # n = 1/2(-1 + sqrt(1 + 8x))
    return int((-1 + (1+8*x)**.5)/2.)

def pent_num(n):
    return int(n*(3*n-1)/2.)

def tri_num(n):
    return int(n*(n+1)/2.)

def find_tri_pent_hex_num(init = 144):
    hex_gen = hex_nums(init)
    while True:
        hex_num = hex_gen.next()
        if (pent_num(nearest_pent_num(hex_num))==hex_num and
            tri_num(nearest_tri_num(hex_num))==hex_num):
            print hex_num
            return

find_tri_pent_hex_num()
