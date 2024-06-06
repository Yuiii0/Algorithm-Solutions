import sys
input=sys.stdin.readline
n=int(input())

status=list(map(int,input().split()))
#print(status) #[0, 1, 0, 1, 0, 0, 0, 1]

x=int(input())
#print(x)

# 학생 스위치 조작
for _ in range(x):
    gender,num=map(int,input().split())
    #print(gender,num)

    #남학생=배수
    if gender==1:
        for i in range(1,n//num+1):
            idx=i*num-1
            #toggle
            status[idx]=1 if status[idx]==0 else 0
    #여학생=좌우대칭
    else:
        # 해당 번호 toggle
        status[num-1]=1 if status[num-1]==0 else 0
        left=num-2
        right=num
        while left>=0 and right<n and status[left]==status[right]:
            # print(status[left],status[right])
            #toggle
            #인덱스 체크
            if left>=0 and right<n:
                status[left]=1 if status[left]==0 else 0
                status[right]=1 if status[right]==0 else 0
                 #한칸씩 이동
                left-=1
                right+=1

            else:
                break


# 한 줄에 20개씩 출력
for i in range(0,len(status),20):
    print(' '.join(map(str,status[i:i+20])))

