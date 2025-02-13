Y, W = map(int, input().split())

max_roll = max(Y, W)
min_roll = 7 - max_roll

numerator = min_roll
denominator = 6

from math import gcd
g = gcd(numerator, denominator)

print(f"{numerator // g}/{denominator // g}")
