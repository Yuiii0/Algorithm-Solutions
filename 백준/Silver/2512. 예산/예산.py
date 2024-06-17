import sys
input=sys.stdin.readline

def binary_search(budgets,target):
    start=0
    end=max(budgets)
    result=0

    while start<=end:
        mid=(start+end)//2

        total_budget=0
        for i in range(len(budgets)):
            total_budget+=min(mid,budgets[i])


        if total_budget<=target:
            result=mid
            start=mid+1
        else:
            end=mid-1

    return result




n=int(input())
budgets=list(map(int,input().rstrip().split()))
target=int(input()) # 총 에산
result=binary_search(budgets,target)
print(result)
