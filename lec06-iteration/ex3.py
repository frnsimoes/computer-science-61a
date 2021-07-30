def print_all(x):
    print(x)
    return print_all

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

if __name__ == '__main__':
    # print_all(1)(3)(4)(5)(6)
    print_sums(1)(2)(5)(1)
    