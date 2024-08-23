def solution(answers):
    result=[]
    user1= [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3,3,1,1,2,2,4,4,5,5]
    
    correct_dict={1:0,2:0,3:0}
    
    for idx,ans in enumerate(answers):
        user1_idx=idx%len(user1)
        user2_idx=idx%len(user2)
        user3_idx=idx%len(user3)
        
        # 정답 확인
        if ans==user1[user1_idx]:
            correct_dict[1]+=1
        if ans==user2[user2_idx]:
            correct_dict[2]+=1
        if ans==user3[user3_idx]:
            correct_dict[3]+=1
            
            
            
    max_value=max(correct_dict.values())
    print(max_value)

    for key,value in correct_dict.items():
        print(max_value,value)
        if max_value==value:
            result.append(key)
        
        
    return result