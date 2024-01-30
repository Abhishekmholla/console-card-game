def create_deck(card_deck, card_values, selected_suit):
    """
    This function creates a deck using the values and suit

    Parameters:
    :param selected_suit: suit selected by the player
    :param card_values: Dictionary of card values
    :param card_deck: List of cards in the deck

    Returns:
    Doesn't return anything
    """
    # Generating a deck by mapping each card value to suit value
    for value in card_values:
        for suit_value in selected_suit:
            card_deck.append(value + suit_value)