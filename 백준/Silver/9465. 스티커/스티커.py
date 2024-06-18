import sys
input=sys.stdin.readline

tc=int(input())

for _ in range(tc):
    n=int(input())
    stickers = [list(map(int, input().rstrip().split())) for _ in range(2)]

    dp=[[0]*n for _ in range(2)]

    # 길이 1
    dp[0][0]=stickers[0][0]
    dp[1][0]=stickers[1][0]

    if n==1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # 길이 2
    dp[0][1]=stickers[1][0]+stickers[0][1]
    dp[1][1]=stickers[0][0]+stickers[1][1]

    if n==2:
        print(max(dp[0][1],dp[1][1]))
        continue

    # 길이 3
    for i in range(2,n):
        dp[0][i]=max(dp[1][i-2],dp[1][i-1])+stickers[0][i]
        dp[1][i]=max(dp[0][i-2],dp[0][i-1])+stickers[1][i]

    print(max(dp[0][-1],dp[1][-1]))

