from collections import Counter
K = int(input())
arr = list(map(int,input().split()))
dct = Counter(arr)
print(dct)
for k,v in dct.items():
    if v < K:
        print(k)
        break

"""
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
"""