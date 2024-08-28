
answer=0

def dfs(numbers,target,cur_idx,cur_total):
    global  answer

    # 탈출 조건
    if cur_idx==len(numbers):
        if cur_total==target:
            answer+=1
        return

    else:
        dfs(numbers,target,cur_idx+1,cur_total+numbers[cur_idx])
        dfs(numbers,target,cur_idx+1,cur_total-numbers[cur_idx])


def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0)

    return answer

