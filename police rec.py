n = int(input())
e = [int(i) for i in input().split()]

o = 0
u = 0

for x in e:
    if x > 0:
        o += x
    elif o > 0:
        o -= 1
    else:
        u += 1

print(u)
