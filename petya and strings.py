x = input()
y = input()
xlower = x.lower()
ylower =y.lower()
if xlower==ylower:
	print(0)
elif xlower<ylower:
	print(-1)
else:
	print(1)
