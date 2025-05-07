def fibonacci(n):
    a, b = 0, 1
    sea = []
    while len(sea) < n:
        sea.append(a)
        a, b = b, a + b
    return sea

print(fibonacci(int(input("Počet prvků: "))))
