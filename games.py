n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]

count = 0

for home in teams:
    for guest in teams:
        if home[0] == guest[1]:  
            count += 1

print(count)
