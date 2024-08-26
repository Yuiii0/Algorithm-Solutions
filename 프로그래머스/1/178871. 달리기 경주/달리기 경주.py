def solution(players, callings):
    rank_dict={}
    for idx,player in enumerate(players):
        rank_dict[player]=idx

    for calling in callings:
        current_rank = rank_dict[calling]
        rank_dict[calling] -= 1
        rank_dict[players[current_rank-1]] += 1

        players[current_rank-1],players[current_rank]=players[current_rank],players[current_rank-1]

    return players
