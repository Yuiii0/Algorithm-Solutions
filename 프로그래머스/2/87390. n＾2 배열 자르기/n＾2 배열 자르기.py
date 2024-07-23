

def solution(n, left, right):
    answer=[]
    
    for x in range(left,right+1):
        a=x//n
        b=x%n
        answer.append(max(a,b)+1)
        
    return answer