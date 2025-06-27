# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input())
r = abs(z)
angle = cmath.phase(z)
print(r)
print(angle)
