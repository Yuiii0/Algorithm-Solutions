import sys
from collections import Counter
words = sorted(list(sys.stdin.readline().strip()))
word_counter=Counter(words)

# words length
# 홀수 -> 홀수 1개까지 가능
# 짝수 -> 홀수 불가능

odd_char=''
odd_cnt=0
p=True #출력 flag

#단어 조합 빈도수/2만큼 
temp=''
result=''
for char,cnt in word_counter.items():
    #홀수 발견
    if cnt%2==1:
        #짝수: 불가능
        if len(words)%2==0:
            print("I'm Sorry Hansoo")
            p=False
            break
        else:
            if odd_cnt>=1:
                print("I'm Sorry Hansoo")
                p=False
                break
            else:
                odd_char+=char
                odd_cnt+=1
                word_counter[char]-=1 #가운데 출력할 글자이기 때문

if p:
    # left 출력
    for word in word_counter.keys():
        temp+=word*(int(word_counter[word])//2)
    result+=temp    
    # 가운데 출력
    result+=odd_char
    #right
    result+=temp[::-1]
    
    print(result)


    

    

        


    
        
# 34184	68