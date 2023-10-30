def substitute_cards(card):
    card_dict = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    
    if card in card_dict:
        return card_dict[card]
    else:
        return int(card)

def play_game(player1_cards, player2_cards):
    if player1_cards == player2_cards[::-1]:
        return "draw"
    c = 0
    while player1_cards and player2_cards:
        
        
        # print("player1_cards", player1_cards)
        # print("player2_cards", player2_cards)
        card1 = substitute_cards(player1_cards.pop(0))
        card2 = substitute_cards(player2_cards.pop(0))
        

        if card1 == card2:
            player1_cards.append(card1)
            player2_cards.append(card2)
        elif card1 > card2:
            player1_cards.append(card2)
        else:
            player2_cards.append(card1)

        
        
        # if set(player1_cards) == set(player2_cards) and len(set(player1_cards)) == 1:
        #     return "draw"
        # elif player1_cards == player2_cards:
        #     return "draw"
        
        if c > 1000000:
            return "draw"
        c += 1

    if not player1_cards:
        return "player 2"
    elif not player2_cards:
        return "player 1"
    else:
        return "draw"


n = int(input())
for _ in range(n):
    player1_cards = list(input().split())
    player2_cards = list(input().split())
    result = play_game(player1_cards, player2_cards)
    print(result)

