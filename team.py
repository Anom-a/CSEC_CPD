n=int(input())
count =0
for i in range(n):
	x=[int(j) for j in input().split()]
	if x.count(1) >=2:
		count+=1
print(count)
