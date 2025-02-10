word = input()
up=0
n = len(word)
for i in word:
	if i.isupper():
		up+=1
lo = n-up
if up > lo:
	print(word.upper())
else:
	print(word.lower())
