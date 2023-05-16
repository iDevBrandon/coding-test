# https://www.acmicpc.net/problem/2525

#풀이1
'''
m에 일단 t를 더해준 후, m은 60미만의 정수이며 h는 24미만의 정수라는 점을 이용함
'''
h,m=map(int,input().split())
t=int(input())
m+=t
print((h+m//60)%24,m%60)

#풀이2
'''
open(0)을 이용한 간결한 풀이
'''
h,m,t=map(int,open(0).read().split())
m+=t
print((h+m//60)%24,m%60)

#풀이3
'''
숏코딩. int에 넣을때 strip이 자동으로 되는 점을 이용
ex)
int('1 ')==1
int('12')==12
'''
p,t=open(0)
m=int(p[2:])+int(t)
print((int(p[:2])+m//60)%24,m%60)
