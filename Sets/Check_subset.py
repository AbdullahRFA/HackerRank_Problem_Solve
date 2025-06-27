# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
while t > 0:
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))

    t -= 1