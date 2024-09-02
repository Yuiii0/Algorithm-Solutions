def solution(s):
    count=0
    binary_num=s
    zero_count=0
    
    while binary_num!='1':
        c=len(''.join(binary_num.split("0")))
        temp=len(binary_num)-c
        zero_count+=temp
        binary_num=bin(c)[2:] 
        count+=1
        
    
    print(binary_num)
    
    
    answer = []
    return [count,zero_count]