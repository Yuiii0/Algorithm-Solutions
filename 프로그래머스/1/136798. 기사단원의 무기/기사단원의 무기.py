def solution(number, limit, power):
    answer = 0
    #약수 개수 배열 만들기
    # num_list=[x for x in range(1,number+1)]
    for num in range(1,number+1):
        count=0
        for i in range(1,int(num ** 0.5)+1):
            if num%i==0:
                if num/i==i:
                    count+=1
                else:
                    count+=2
        #limit 넘으면 power로 변경
        if count>limit:
            count=power
        answer+=count
        
    #limit 
    #answer=list(map(lambda x: power if x>limit else x,num_list))
    
    return answer