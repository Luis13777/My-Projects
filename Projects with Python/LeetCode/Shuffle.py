def shuffle(cards):
    if len(cards) == 0:
        return []
    pile = [cards[0]]
    i = 1 
    while i < len(cards):
        pile.append(cards[i])
        i += 1
        if i < len(cards):
            pile = [cards[i]] + pile
            i += 1

    return pile


print(shuffle([1,2,3,4,5,6,7,8,9]))