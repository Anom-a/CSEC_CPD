n = int(input())
events =[int(i) for i in input().split()]
overAll = sum(events)
j=len(events) -1
count=0
while events[j] !=-1:
	count+=1
	j-=1
result = -1*(overAll-count)
print(result)
	
