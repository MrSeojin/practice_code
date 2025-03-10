import time
T = int(input("상황(T): "))

for _ in range(T):
    H, W, N = map(int, input("H, W, N: ").split())
    if N%H != 0:
        print( N%H * 100 + N//H + 1)
    else:
        print( H * 100 + N//H )
