n = int(input())
birds = [int(i) for i in input().split()]
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if x > 0:
        birds[x - 1] += y
    if x < n - 1:
        birds[x + 1] += birds[x] - y
    
    birds[x] = 0

for b in birds:
    print(b)
