def date_to_days(year, month, day):
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    
    # today를 연, 월, 일로 분리하고 일수로 변환
    today_year, today_month, today_day = map(int, today.split('.'))
    today_days = date_to_days(today_year, today_month, today_day)
    
    # term 딕셔너리 정의
    terms_dict = {}
    for term in terms:
        t_type, t_term = term.split(' ')
        terms_dict[t_type] = int(t_term)
    
    # 개인정보를 처리
    for i, privacy in enumerate(privacies):
        p_date, p_type = privacy.split(' ')
        year, month, day = map(int, p_date.split('.'))
        
        # 유효기간 더한 후, 일수로 변환
        month += terms_dict[p_type]
        while month > 12:
            month -= 12
            year += 1
        
        expiry_days = date_to_days(year, month, day) - 1  
        
        # 파기해야 할 개인정보인지 확인 (일수로 확인)
        if expiry_days < today_days:
            answer.append(i + 1)
    
    return answer
