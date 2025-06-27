# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
pset = set(map(int,input().split()))
t = int(input())
while t>0:
    cmd = input().split()
    tset = set(map(int,input().split()))
    ins = cmd[0]
    if ins == "intersection_update":
        pset.intersection_update(tset)
    if ins == "update":
        pset.update(tset)
    if ins == "symmetric_difference_update":
        pset.symmetric_difference_update(tset)
    if ins == "difference_update":
        pset.difference_update(tset)
    t-=1
print(sum(pset))