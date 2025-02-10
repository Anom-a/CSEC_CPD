n = int(input())
cards = [int(i) for i in input().split()]
sereja = 0
dima =0
for i in range(n):
	if i%2==0:
		sereja+=max(cards)
		cards.remove(max(cards))
	else:
		dima+=max(cards)
		cards.remove(max(cards))
print(sereja, dima)
