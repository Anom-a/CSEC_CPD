l, b =[int(i) for i in input().split()]
count=0
while l<=b:
	count+=1
	l*=3
	b*=2	
print(count)
