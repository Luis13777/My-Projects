def climbingLeaderboard(ranked, player):
    rank = []
    for score in player:
        i = 0
        position = 1
        while (i < len(ranked) and score < ranked[i]):
            if i > 0 and ranked[i-1] > ranked [i]:
                position += 1
            if i == 0 and ranked[0] > score:
                position += 1
            i += 1
        rank.append(position)
    return rank

print(climbingLeaderboard([100],[90]))

