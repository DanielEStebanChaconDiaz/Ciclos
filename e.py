import math
denominator=2
difference=1
e = 2
previous_fraction = 1
fraction = 1
while difference>0.0001:
    previous_fraction = fraction
    fraction= 1/math.factorial(denominator)
    denominator += 1
    e += fraction
    difference= previous_fraction-fraction
print(e)