a = [int(i) for i in input().split()]
s = input()
calories = sum(a[int(c) - 1] for c in s)
print(calories)
