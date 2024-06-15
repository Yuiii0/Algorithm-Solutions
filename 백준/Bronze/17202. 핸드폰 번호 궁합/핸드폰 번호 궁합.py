import sys
input=sys.stdin.readline


nums1=list(map(int,input().rstrip()))
nums2=list(map(int,input().rstrip()))


numbers=[]
for a,b in zip(nums1,nums2):
    numbers.append(a)
    numbers.append(b)

dp = [[(i + j) % 10 for j in range(10)] for i in range(10)]

while len(numbers)>2:
    temp=[]
    for i in range(len(numbers)-1):
        temp.append(dp[numbers[i+1]][numbers[i]]) #dp[i+1][i] 접근으로 두 합 구하기
    numbers=temp

print(''.join(map(str,numbers)))






