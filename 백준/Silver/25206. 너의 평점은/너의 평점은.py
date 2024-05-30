#(학점*평점)/총 수강학점
#P는 제외=> 제외

grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
scores = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
p_credit=0
total_score=0
total_credit=0
for i in range(20):
    subject,credit,grade=input().split()
    credit=float(credit)

    #P일때
    if grade=='P':
        continue
        
    #total구하기
    score = scores[grades.index(grade)]
    total_score += credit * score
    total_credit+=credit

print(total_score/total_credit)






        
    
    
