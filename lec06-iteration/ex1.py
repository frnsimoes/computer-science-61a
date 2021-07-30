def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x = x + 1

def is_three(x):
    return x == 3

"""
f == is_three. 
f, na verdade, é 'evaluated' como boolean.
f está sendo executado apenas dentro do frame de 'search'.
"""

if __name__ == '__main__':
    r = search(is_three)
    print(r)
    