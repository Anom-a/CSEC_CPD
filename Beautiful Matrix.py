import math
row =0
realRow=0
column=0
for i in range(5):
	arr=[int(j) for j in input().split()]
	row+=1
	if arr.count(1)==1:
		column = arr.index(1)+1
		realRow = row
step1= abs(3-realRow)
step2=abs(3-column)
print(step1+step2)
		
