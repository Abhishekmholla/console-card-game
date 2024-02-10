import random 

def pick_card(card_deck):
    """
    This function picks a card randomly from the card_deck

    Parameters:
    :param card_deck: List of cards in the deck

    Returns:
    Returns a card selected by the user
    """
    cards = {'player_card': '', 'robot_card': ''}

    # Generate a random number index for the player
    random_player_card_index = random.randint(0, len(card_deck))

    # If the index is found in the deck, 
    # then insert into dictionary and delete it from the existing list
    if random_player_card_index in range(0, len(card_deck)):
        cards['player_card'] = card_deck[random_player_card_index]
        card_deck.pop(random_player_card_index)

    # Generate a random number index for the robot but with a large range
    random_robot_card_index = random.randint(-20, len(card_deck))

    # If the index is found in the deck, 
    # then insert into dictionary and delete it from the existing list
    if random_robot_card_index in range(0, len(card_deck)):
        cards['robot_card'] = card_deck[random_robot_card_index]
        card_deck.pop(random_robot_card_index)

    return cards