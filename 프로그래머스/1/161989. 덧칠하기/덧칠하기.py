def solution(n, m, section):
    answer = 0
    target=section[len(section)-1]
    painted=0
    
    for s in section:
        if painted<s:
            painted=s+m-1
            answer+=1   #칠함
            print(painted)
        continue    
    return answer