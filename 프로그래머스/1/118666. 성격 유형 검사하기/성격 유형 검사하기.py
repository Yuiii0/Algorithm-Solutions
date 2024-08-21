def solution(survey, choices):
    types=[('R','T'),('C','F'),('J','M'),('A','N')]
    type_dict={}
    answer = ''

    for i in range(len(survey)):

        # 동의, 비동의 매칭 타입 구하기
        disagree_type = survey[i][0]
        agree_type = survey[i][1]


        # 점수 구하기
        if choices[i]<4:
            score=4-choices[i]
            score_type=disagree_type
        else:
            score=choices[i]%4
            score_type=agree_type

        # 점수 카운트
        type_dict[score_type]=type_dict.get(score_type,0)+score

    # 성격 유형 구하기
    for type in types:
        print(type[0],type[1])
        type1_score=type_dict.get(type[0],0)
        type2_score=type_dict.get(type[1],0)

        if type1_score<type2_score:
            answer+=type[1]
        elif type1_score==type2_score:
            answer+=sorted(type)[0]
        
        else:
            answer+=type[0]


    return answer