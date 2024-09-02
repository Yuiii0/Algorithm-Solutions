def solution(k, score):
    answer = []
    winner=[]
    for i in range(len(score)):
        winner.append(score[i])
        answer.append(sorted(winner,reverse=True)[:k][-1])
        
    return answer