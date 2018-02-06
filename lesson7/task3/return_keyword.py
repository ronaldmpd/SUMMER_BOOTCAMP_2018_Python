def sum_two_numbers(a, b):
    return a + b
c = sum_two_numbers(3, 12)


def fib(n):
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = a + b
        a = tmp_var
    return result
print(fib(10))
