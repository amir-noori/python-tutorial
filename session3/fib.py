'''
fibonacci sequence
f(0) = 0
f(1) = 1
...
f(n) = f(n - 1) + f(n - 2)
'''


'''
This implementation has an issue which is: RecursionError: maximum recursion depth exceeded in comparison

    fib(n):
        fib(n - 1) + fib(n - 2):
            (fib(n - 2) + fib(n - 3)) + (fib(n - 3) + fib(n - 4))
                ...

'''
def fib1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)

cache = {}
def print_fib(n):
    if n == 1 or n == 0:
        cache[0] = 0
        cache[1] = 1
        return n

    result = 0
    if len(cache) == n and cache[n - 1]:
        result = cache[n - 1] + cache[n - 2]
        cache[n] = result
        return result

    fn1 = 1
    fn2 = 0
    i = 2
    while i < n + 1:
        fn = fn1 + fn2
        result = fn
        cache[i] = fn
        fn2 = fn1
        fn1 = fn
        i = i+1

    return result

# print(print_fib(0))
# print(print_fib(1))
# print(print_fib(10))
# print(cache)


# print(print_fib(0))
# print(print_fib(1)) 
# print(print_fib(2))
# print(print_fib(10)) 
# print(print_fib(1000))

# print(fib1(0))
# print(fib1(1))
# print(fib1(2))
# print(fib1(10))
# print(fib1(1000)) this line will throw RecursionError 

data = {}
data[0] = 0
data[1] = 1

def fib2(n, fib_data):
    if n < 2:
        return data[n]
    check(n, fib_data, fib2)
    fib_data[n] = fib_data[n - 1] + fib_data[n - 2]
    return fib_data[n]

def check(n, check_data, fn):
    index = 0
    while index < n:
        try:
            if check_data[index]:
                pass
        except KeyError:
            fn(index, check_data)
        index = index + 1


print(fib2(10, data))





