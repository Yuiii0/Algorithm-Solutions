def solution(cards1, cards2, goal):
    answer = ''
    
    for card in goal:
        if len(cards1)>0 and card == cards1[0]: #cards가 비어있을때 오류방지
            cards1.pop(0)
        elif len(cards2)>0 and  card == cards2[0]:
            cards2.pop(0)
        
        else :
            return "No"
            
    
    return "Yes"