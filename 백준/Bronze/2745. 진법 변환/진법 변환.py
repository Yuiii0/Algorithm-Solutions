import sys
n,b=sys.stdin.readline().split()

nums="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result=0

for i,num in enumerate(n[::-1]):
    result+=int(b)**i*nums.index(num)

print(result)
