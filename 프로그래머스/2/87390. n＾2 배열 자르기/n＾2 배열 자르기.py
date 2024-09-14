
def solution(n, left, right):
    answer=[]
    for x in range(left,right+1):
        row=x//n
        col=x%n
        answer.append(max(row,col)+1)

    return answer

