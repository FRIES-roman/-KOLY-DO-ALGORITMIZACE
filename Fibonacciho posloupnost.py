def fibonacci_pocet(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def fibonacci_limit(limit):
    fib = [0, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > limit:
            break
        fib.append(next_fib)
    return fib

print("Vyber režim:")
print("1 - Zadání počtu prvků")
print("2 - Zadání horní meze")

volba = input("Zadej volbu (1/2): ")

if volba == "1":
    n = int(input("Zadej počet prvků Fibonacciho posloupnosti: "))
    print(fibonacci_pocet(n))
elif volba == "2":
    limit = int(input("Zadej horní mez Fibonacciho posloupnosti: "))
    print(fibonacci_limit(limit))
else:
    print("Neplatná volba!")