def check_card_count(player_cards, robot_cards, selected_suit):
    """
    This function selects the second suit and checks how many cards
    of the same suit is present with the player and robot

    Parameters:
    :param selected_suit: suit selected by the player
    :param robot_cards: List of cards allocated to the robot
    :param player_cards: List of cards allocated to the player

    Returns:
    Returns the game result i.e. whether the player or robot won
    """
    player_result = {'player_won': False, 'robot_won': False}

    desired_suit = selected_suit[1]
    desired_count = {'player_count': 0, 'robot_count': 0}

    # For each character in player card, calculating the total count of entries for a specific suit type
    for ply_card in player_cards:
        for character in ply_card:
            if character != desired_suit:
                continue

            desired_count.update({'player_count': desired_count.get('player_count') + 1})

    # For each character in robot card, calculating the total count of entries for a specific suit type
    for rbt_card in robot_cards:
        for character in rbt_card:
            if character != desired_suit:
                continue

            desired_count.update({'robot_count': desired_count.get('robot_count') + 1})

    if desired_count.get('player_count') > 0 and \
            desired_count.get('player_count') > desired_count.get('robot_count'):
        player_result.update({'player_won': True})
    elif desired_count.get('robot_count') > 0 and \
            desired_count.get('player_count') < desired_count.get('robot_count'):
        player_result.update({'robot_won': True})
    else:
        return player_result

    return player_result