## The anatomy of a recursive function

- The def statement header is similar to other functions

- Conditional statements check for base cases
`if n < 0`

- Base cases are evaluated without recursive calls
`return n`

- Recursive cases are evaluated with recursive calls
```
else:
    all_but_last, last = split(n)
    return sum_digits(all_but_last) + last
```

## Verify recursive correctness

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

Ask yourself: is factorial implemented correctply? 

1. Verify the base case. 
2. Treat fact as a functional abstraction.
3. Assume that factorial(n-1) is correct. 
4. Verify