# 뒤에서부터 순회하면서 stack에 있는 숫자들보다 큰 숫자만 stack에 담기
import sys
input=sys.stdin.readline
n=int(input())

bars=[]
for i in range(n):
    num=int(input())
    bars.append(num)

stack=[]

for bar in bars[::-1]:
    if not stack: #first
        stack.append(bar)
    if bar>stack[-1]:
        stack.append(bar)
    
print(len(stack))