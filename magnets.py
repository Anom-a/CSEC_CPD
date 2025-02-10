n = int(input())
count =0
first = input()
last = first[1]
for i in range(1, n):
	normal = input()
	last2 = normal[1]
	if  last != last2:
		count+=1
	last = last2
print(count+1)
