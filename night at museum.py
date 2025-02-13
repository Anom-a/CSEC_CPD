s = input()

current = 'a'
rotations = 0

for c in s:
    diff = abs(ord(c) - ord(current))
    rotations += min(diff, 26 - diff)
    current = c

print(rotations)
