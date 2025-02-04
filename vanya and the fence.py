arr = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
o=0
for j in h:
    if j>arr[1]:
        o+=1
count = arr[0] -o
o*=2
count +=o
print(count)
