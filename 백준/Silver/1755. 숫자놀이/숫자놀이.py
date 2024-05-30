# M과 N사이의 숫자와 문자열을 가진 이중배열 생성
# 문자열기준으로 sort
# 숫자 배열 출력

m,n=input().split()
m = int(m)
n = int(n)

num_dict = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

#이중배열 생성
nums=[]
for num in range(m,n+1):
    num_str=''
    for n in str(num):
        num_str+=num_dict[n]
        
    nums.append([num,num_str])

#sort
nums.sort(key=lambda x:x[1])

#10개씩 출력
c=0
for num in nums:
    c+=1
    print(num[0], end=' ')
    if c>=10:
        print()
        c=0
