#해결과정
#1. 1/1부터 target일자까지 총 일수를 계산
#2. 총 일수에서 요일 구하기


month,day=map(int,input().split())

date_list = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#1.
total_days=sum(days_list[:month-1])+day #n-1월까지 일수+day

#2.7로 나눈 나머지=인덱스가 되도록 date_list
index=total_days%7
print(date_list[index])








