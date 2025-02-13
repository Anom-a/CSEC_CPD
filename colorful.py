s = input()
t = input()

pos = 1
for i in t:
    if s[pos - 1] == i:
        pos += 1

print(pos)
