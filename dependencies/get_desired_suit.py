def get_desired_suit(selected_suit, card_value):
    """
    This function generates the desired suit using the selected suit and card value

    Parameters:
    :param card_value: Dictionary of card values
    :param selected_suit: suit selected by the player

    Returns:
    Returns the desired suit list
    """
    desired_suit = []

    # For each value in card_value, 
    # generating a list of list by appending it with suit
    for value in card_value:
        suit_value = []
        for suit in selected_suit:
            suit_value.append(value + suit)

        desired_suit.append(suit_value)

    return desired_suit