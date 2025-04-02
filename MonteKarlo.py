import numpy.random as rnd

def Pi(N):
    N_circle = 0
    i = 1
    while i <= N:
        x, y = rnd.rand(2)
        if x*x + y*y <= 1:
            N_circle = N_circle + 1
        i = i + 1
    Pi = 4 * N_circle / float(N)
    return Pi
