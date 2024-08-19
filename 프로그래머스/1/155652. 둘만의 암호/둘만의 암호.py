def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    filtered_alphabet = list(filter(lambda x: x not in skip, alphabet))
    
    for char in s:
        current_idx = filtered_alphabet.index(char)
        new_idx = current_idx + index

        if new_idx >= len(filtered_alphabet):
            new_idx %= len(filtered_alphabet)

        new_char = filtered_alphabet[new_idx]
        answer += new_char

    return answer
