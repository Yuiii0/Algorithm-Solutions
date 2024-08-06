def solution(word):
    # 알파벳 모음 리스트
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # 각 자리수에 대한 가중치 계산
    weight = [781, 156, 31, 6, 1]  # 5^4 + 5^3 + 5^2 + 5^1 + 1
    
    # 결과 값 초기화
    result = 0
    
    # 각 자리수에 따른 단어 위치 계산
    for i, char in enumerate(word):
        result += weight[i] * vowels.index(char) + 1
    
    return result

# 테스트 예시
print(solution("AAAAE"))  # 6
print(solution("AAAE"))   # 10
print(solution("I"))      # 1563
print(solution("EIO"))    # 1189
