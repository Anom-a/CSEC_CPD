n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    xi, yi = map(int, input().split())
    index = xi - 1
    original = a[index]
    left = yi - 1
    right = original - yi
    a[index] = 0
    if index > 0:
        a[index - 1] += left
    if index < n - 1:
        a[index + 1] += right

print('\n'.join(map(str, a)))
