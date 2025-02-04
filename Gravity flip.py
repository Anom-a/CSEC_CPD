n= int(input())
x=[int(j) for j in input().split()]
x.sort()
print(" ".join(str(i) for i in x))
