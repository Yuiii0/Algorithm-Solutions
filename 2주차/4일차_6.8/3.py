import sys

def cal_final_score(scores):
    max_run=max(scores[:2])
    tricks=scores[2:]
    tricks.sort(reverse=True)
    sum_tricks=sum(tricks[:2])
    return max_run+sum_tricks

def find_best_score(final_scores):
    return max(final_scores)

def read_input():
    input = sys.stdin.readline
    n = int(input().strip())
    score_list=[list(map(int,input().rstrip().split()))  for _ in range(n)]
    return score_list

def main():
    score_list=read_input()
    final_scores=[]
    for scores in score_list:
        final_score = cal_final_score(scores)
        final_scores.append(final_score)
    result=find_best_score(final_scores)
    print(result)




if __name__ == "__main__":
    main()

    #45996	296