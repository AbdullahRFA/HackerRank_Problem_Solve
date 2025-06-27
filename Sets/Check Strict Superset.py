# Enter your code here. Read input from STDIN. Print output to STDOUT
arr = set(map(int, input().split()))
n = int(input())
flag = False
for _ in range(n):
    sets = set(map(int, input().split()))
    if not arr.issuperset(sets):
        flag = True

if flag:
    print("False")
else:
    print("True")

"""
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
"""