def fibonacci(n):
    a, b = 0, 1
    sea = []
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return sea

print(fibonacci(int(input("Počet prvků: "))))
