def solution(t, p):
    answer = 0
    length=len(p)
    for i in range(0,len(t)-length+1):
        # print(i)
        print()
        if int(t[i:i+length])<=int(p):
            answer+=1
        
    return answer