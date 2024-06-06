import sys
input = sys.stdin.readline

n,m =map(int,input().split())

sounds_dict={}
for _ in range(n):
    length,name,*sounds=input().split()
    # 3개의 음이름만 저장
    key=''.join(sounds[:3])
    if key in sounds_dict:
        sounds_dict[key].append(name)
    else:
        sounds_dict[key]=[name]

# 음이름 찾기
for _ in range(m):
    s="".join(input().strip().split())
    if not s in sounds_dict.keys():
        print('!')
    else:
        target=sounds_dict[s]
        print('?' if len(target)>1 else target[0])

            


 
        
