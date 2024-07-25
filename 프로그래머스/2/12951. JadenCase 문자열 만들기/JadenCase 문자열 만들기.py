def solution(s):
    words=s.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    
    # 수정된 리스트 반환
    return ' '.join(capitalized_words)
    
    