from collections import Counter
if __name__ == "__main__":
    N = int(input())
    lst = []
    for x in range(N):
        n = input()
        lst.append(n)
    dct = Counter(lst)
    print(len(dct))
    for x in dct.values():
        print(x, end=" ")
    # print(dct)


"""
4
bcdef
abcdefg
bcde
bcdef

"""