def solution(s):
    turn=0
    zero_count=0
    
    while s!='1':
        c=len(''.join(s.split("0")))
        turn+=1
        zero_count+=len(s)-c
        s=bin(c)[2:] 
   
    return [turn,zero_count]