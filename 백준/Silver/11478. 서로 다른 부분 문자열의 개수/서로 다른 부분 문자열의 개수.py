s=input()
s_set=set()

#모든 조합을 set에 넣어 중복제거 (i=1~문자열 길이)
for i in range(len(s)): 
    for j in range(i,len(s)):
        s_set.add(s[i:j+1])

print(len(s_set)) #빈 문자열 경우 제거
