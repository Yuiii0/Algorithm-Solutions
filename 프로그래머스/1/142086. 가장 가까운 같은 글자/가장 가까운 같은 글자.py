def solution(s):
    answer = []
    char_dict={}
    for i,char in enumerate(s):
        if char in char_dict:
            answer.append(i-char_dict[char])
        else:
            answer.append(-1)
        char_dict[char]=i




    return answer
