n =int(input())
res=input()
a=res.count('A')
d=res.count('D')
if d>a:
	print('Danik')
elif d==a:
	print('Friendship')
else:
	print('Anton')
