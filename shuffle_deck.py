import random

def shuffle_deck(card_deck, selected_suit):
    """
    This function shuffles the deck with specific cards at
    first,middle and last index of the card_deck list

    Parameters:
    :param selected_suit: suit selected by the player
    :param card_deck: List of cards in the deck

    Returns:
    Doesn't return anything
    """
    print('\nShuffling deck....')
    # Randomly shuffling the entire deck
    random.shuffle(card_deck)
    __move_deck_item(card_deck, selected_suit)
    print('\nHere is your deck....\n')
    print(card_deck)
    

def __move_deck_item(card_deck, selected_suit):
    # The items to be replaced are collected in a dictionary along 
    # with the position at which they need to be inserted
    replacement_items = {0: 'A' + selected_suit[0],
                         int(round((len(card_deck) + 1) / 2, 0)): 'Q' + selected_suit[1],
                         len(card_deck) - 1: 'K' + selected_suit[-1]}

    for key, value in replacement_items.items():

        # Check if the card is removed, 
        # if removed just ignore the value in card_deck
        if value not in card_deck:
            continue

        # Remove the value at the specific position 
        # and insert it back at a given position
        card_deck.pop(card_deck.index(value))
        card_deck.insert(key, value)