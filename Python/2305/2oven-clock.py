# https://www.acmicpc.net/problem/2525

h, m = map(int,input().split())
plus = int(input())

h = (h+((m+plus)//60))%24
m = (m+plus)%60

print(h, m, " ")