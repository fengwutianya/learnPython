def fib(max):
    n, a, b, tmp = 0, 0, 1, 0
    while n < max:
        yield b
        tmp = a + b
        a = b, b = tmp
        n += 1
    return "done"

if __name__ == '__main__':
    print(next(fib(8)))
