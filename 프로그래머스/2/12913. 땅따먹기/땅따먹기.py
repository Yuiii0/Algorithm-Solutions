def solution(land):
    scoreSum=[0,0,0,0]

    for line in land:
        newScoreSum=[0,0,0,0]
        for idx in range(4):
            prevScoreSum=scoreSum[:idx]+scoreSum[idx+1:]
            newScoreSum[idx]=line[idx]+max(prevScoreSum)
        scoreSum=newScoreSum
    return max(scoreSum)