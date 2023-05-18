# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())
lstPrice = []

for _ in range(m):
    price = tuple(map(int, input().split()))
    lstPrice.append(price)

min_six = sorted(lstPrice, key=lambda x : x[0])[0][0]
min_one = sorted(lstPrice, key=lambda x : x[1])[0][1]

if min_six >= min_one*6 :
    print(n*min_one)
else :
    if n == 6 :
        print(min_six)
    elif n < 6 :
        if min_six >= min_one*n :
            print(n*min_one)
        else :
            print(min_six)
    else :
        rtnVal = min_six*(n//6)
        if min_six < min_one*(n%6) :
            rtnVal += min_six
        else :
            rtnVal += min_one*(n%6)
        print(rtnVal)