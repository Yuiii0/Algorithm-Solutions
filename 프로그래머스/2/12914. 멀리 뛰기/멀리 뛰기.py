def solution(n):
    answer=0
    dp1, dp2=1,1
    for i in range(2,n+1):
        dp1,dp2=dp1+dp2,dp1

    return dp1%1234567