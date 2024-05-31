import sys
input = sys.stdin.readline

a1, a0 = map(int,input().rstrip().split())
c=int(input())
n=int(input())

#print(a1,a0,c,n)

#O(n)식 정의
# print(a1*n+a0)
# print(c*n)

if a1*n+a0<=c*n and a1<=c:
    print(1)
else:
    print(0)
