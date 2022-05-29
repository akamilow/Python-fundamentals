def fibonacci(n):
    x = 1
    y = 1
    print(0)
    print(x)
    print(y)
    for _ in range(n - 2):
        total = x + y
        y = x
        x = total
        print(total)

print(fibonacci(10))