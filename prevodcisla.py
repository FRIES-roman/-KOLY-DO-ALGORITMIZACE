def d(a): return bin(int(a))[2:]
def b(a): return int(a,2)
def s(a): return sum(map(int,a.split()))
def sb(a): return bin(sum(int(x,2) for x in a.split()))[2:]

while True:
    v = int(input("1=10→2 2=2→10 3=s10 4=s2 0=konec: "))
    if v == 0: break
    a = input()
    print(d(a) if v==1 else b(a) if v==2 else s(a) if v==3 else sb(a))