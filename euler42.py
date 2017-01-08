

def char_val(c):
    return ord(c.upper())-64

def word_val(w):
    return sum(map(char_val, w))

def triangle_num(n):
    return int(.5*n*(n+1))

def triangle_nums_less_than(m):
    t = 0
    d = {}
    i = 1
    while (t<m):
        t = triangle_num(i)
        d[t] = 1
        i += 1
    return d

words = eval('[' + open('resources/p042_words.txt','r').readline() + ']')
max_word_val = max(map(word_val, words))
triangle_nums = triangle_nums_less_than(max_word_val)
print("There are {} triangle words.".format(len(filter(lambda w: word_val(w) in triangle_nums, words))))
