
# Pixel Damage - CodeChef(PIXDAM)
import math

test = int(input())
for _ in range(test):
    H, W, X, Y, K = map(int, input().split())
    dist = math.sqrt((W-X)**2 + (H-Y)**2)
    if dist < K:
        print(1)
    else:
        print(0)