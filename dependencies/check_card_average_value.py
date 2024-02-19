from dependencies import get_replaced_character

def check_card_average_value(player_cards, robot_cards):
    """
    This function checks the average value for all cards with
    the player and robot and decides the result of the game.

    Parameters:
    :param robot_cards: List of cards allocated to the robot
    :param player_cards: List of cards allocated to the player

    Returns:
    Prints all the cards that belongs to the player
    """
    player_result = {'player_won': False, 'robot_won': False}
    desired_sum = {'player_sum': 0, 'robot_sum': 0}

    # For each character in player card, check if has any special characters like A,J,Q,K
    # If found replace it with appropriate value
    # check if the character is digit then add it to the dictionary player_sum
    for ply_card in player_cards:
        for character in ply_card:
            if character in ['A', 'J', 'Q', 'K']:
                character = get_replaced_character(character)
            if not character.isdigit():
                continue

            desired_sum.update({'player_sum': desired_sum.get('player_sum') + int(character)})

    # For each character in robot card, check if has any special characters like A,J,Q,K
    # If found replace it with appropriate value
    # check if the character is digit then add it to the dictionary player_sum
    for rbt_card in robot_cards:
        for character in rbt_card:
            if character in ['A', 'J', 'Q', 'K']:
                character = get_replaced_character(character)
            if not character.isdigit():
                continue

            desired_sum.update({'robot_sum': desired_sum.get('robot_sum') + int(character)})

    # Calculate the average
    player_card_average = desired_sum['player_sum'] / len(player_cards)
    robot_card_average = desired_sum['robot_sum'] / len(robot_cards)
    
    # Verifying if the player or the robot won
    if player_card_average > robot_card_average:
        player_result.update({'player_won': True})
    elif player_card_average < robot_card_average:
        player_result.update({'robot_won': True})
    else:
        player_result.update({'robot_won': True})

    return player_result