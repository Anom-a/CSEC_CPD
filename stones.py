n = int(input())
color = input()
n= len(color)
count =0
for i in range(n-1):
	if color[i] == color[i+1]:
		count+=1
print(count)
