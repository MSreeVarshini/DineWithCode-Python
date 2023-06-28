# Emotional Proximity_CodeChef
# cook your dish here
test = int(input())

for _ in range(test):
    P, X, Y, Z = map(int, input().split())
    if Z==1:
        prox = P*(1+(Y/100))
    else:
        prox = P*(1-(X/100))
    print("{:.10f}".format(prox))