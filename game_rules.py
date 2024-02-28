class game_rules:

    def __init__(self) -> None:
        self.character_constant = ['a', 'j', 'q', 'k']
        self.numerical_constant = ['1', '11', '12', '13']

    def check_result(self, player_cards, robot_cards, selected_suit, card_value):
        """
        This function applies the rules of the game and decides whether the player or the robot won

        Parameters:
        :param card_value: Dictionary of card values
        :param selected_suit: suit selected by the player
        :param robot_cards: List of cards allocated to the robot
        :param player_cards: List of cards allocated to the player

        Returns:
        Returns the game result i.e. whether the player or robot won
        """

        if len(selected_suit) <= 6:
            print("\nChecking Rule 1.....")
            # Rule 1 - The player holds the same value card
            # for all the defined suits
            game_result = self.__check_suit_value(player_cards, robot_cards,
                                                  selected_suit, card_value)

            # Checking if any value in the dictionary is turned to true
            if any(game_result.values()):
                return game_result
            print("Damn!! This rule did not give me a result")

        print("\nChecking Rule 2.....")
        # Rule 2 - The player has the same values for at least the
        # total defined suits minus one
        game_result = self.__check_minimum_suit_value(player_cards, robot_cards,
                                                      selected_suit, card_value)

        # Checking if any value in the dictionary is turned to true
        if any(game_result.values()):
            return game_result
        print("Damn!! This rule did not give me a result")

        print("\nChecking Rule 3.....")

        # Rule 3 - The player holds more cards from the suit in position 2 than the robot
        game_result = self.__check_card_count(player_cards, robot_cards,
                                              selected_suit)

        # Checking if any value in the dictionary is turned to true
        if any(game_result.values()):
            return game_result

        print("Not again.....moving to the next rule")

        print("\nChecking Rule 4.....")

        # Rule 4 - The player holds a higher average of the card’s value than robot
        game_result = self.__check_card_average_value(
            player_cards, robot_cards)

        # Checking if any value in the dictionary is turned to true
        if any(game_result.values()):
            return game_result

        print("Ah-hh!! All 4 rules did not apply")

        print("\nChecking one last rule.....")
        # Rule 5 - if cards are assigned to a player
        # but not robot has no cards assigned, then the player wins
        if len(robot_cards) == 0 and len(player_cards) != 0:
            return {'player_won': True, 'robot_won': False}

    def __check_card_average_value(self, player_cards, robot_cards):
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
                    character = self.__get_replaced_character(character)
                if not character.isdigit():
                    continue

                desired_sum.update(
                    {'player_sum': desired_sum.get('player_sum') + int(character)})

        # For each character in robot card, check if has any special characters like A,J,Q,K
        # If found replace it with appropriate value
        # check if the character is digit then add it to the dictionary player_sum
        for rbt_card in robot_cards:
            for character in rbt_card:
                if character in ['A', 'J', 'Q', 'K']:
                    character = self.__get_replaced_character(character)
                if not character.isdigit():
                    continue

                desired_sum.update(
                    {'robot_sum': desired_sum.get('robot_sum') + int(character)})

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

    def __check_card_count(self, player_cards, robot_cards, selected_suit):
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

                desired_count.update(
                    {'player_count': desired_count.get('player_count') + 1})

        # For each character in robot card, calculating the total count of entries for a specific suit type
        for rbt_card in robot_cards:
            for character in rbt_card:
                if character != desired_suit:
                    continue

                desired_count.update(
                    {'robot_count': desired_count.get('robot_count') + 1})

        if desired_count.get('player_count') > 0 and \
                desired_count.get('player_count') > desired_count.get('robot_count'):
            player_result.update({'player_won': True})
        elif desired_count.get('robot_count') > 0 and \
                desired_count.get('player_count') < desired_count.get('robot_count'):
            player_result.update({'robot_won': True})
        else:
            return player_result

        return player_result

    def __check_minimum_suit_value(self, player_cards, robot_cards, selected_suit, card_value):
        """
        This function checks if the player or robot have A card with at least the total defined suits minus one.

        Parameters:
        :param card_value: Dictionary of card values
        :param selected_suit: Suit selected by the player
        :param robot_cards: List of cards allocated to the robot
        :param player_cards: List of cards allocated to the player

        Returns:
        Returns the game result i.e. whether the player or robot won
        """
        player_result = {'player_won': False, 'robot_won': False}

        desired_suit = self.__get_desired_suit(selected_suit, card_value)
        desired_count = {'player_count': 0, 'robot_count': 0}

        # For each card in desired suit, count the number of identical value card across suit
        total_player_count = []
        for card in desired_suit:
            count = 0
            for ply_card in player_cards:
                if ply_card in card:
                    count = count + 1
            total_player_count.append(count)

        # select the max value of total_player_count
        desired_count.update({'player_count': max(total_player_count)})

        # For each card in desired suit, count the number of identical value card across suit
        total_robot_card = []
        for card in desired_suit:
            count = 0
            for rbt_card in robot_cards:
                if rbt_card in card:
                    count = count + 1
            total_robot_card.append(count)

        # select the max value of total_player_count
        desired_count.update({'robot_count': max(total_robot_card)})

        # Check if the player count and robot count is equal to length of the suit minus 1
        is_player_count_matched = desired_count.get(
            'player_count') == len(selected_suit) - 1
        is_robot_count_matched = desired_count.get(
            'robot_count') == len(selected_suit) - 1

        if is_player_count_matched and not is_robot_count_matched:
            player_result.update({'player_won': True})
        elif is_robot_count_matched and not is_player_count_matched:
            player_result.update({'robot_won': True})
        else:
            return player_result

        return player_result

    def __get_desired_suit(self, selected_suit, card_value):
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

    def __get_replaced_character(self, character):
        """
            This function replaces the character with a specific value

            Parameters:
            :param character: Refers to a specific character

            Returns:
            Returns the character value
            """
        # If the character is any of A,J,Q and K,
        # then replacing it there corresponding values
        if character.lower() == self.character_constant[0]:
            character = character.replace(
                character, self.numerical_constant[0])
        elif character.lower() == self.character_constant[1]:
            character = character.replace(
                character, self.numerical_constant[1])
        elif character.lower() == self.character_constant[2]:
            character = character.replace(
                character, self.numerical_constant[2])
        elif character.lower() == self.character_constant[3]:
            character = character.replace(
                character, self.numerical_constant[3])
        return character

    def __check_suit_value(self, player_cards, robot_cards, selected_suit, card_value):
        """
        This function checks if the player or robot have 'A' card with all the defined suits.

        Parameters:
        :param card_value: Dictionary of card values
        :param selected_suit: Suit selected by the player
        :param robot_cards: List of cards allocated to the robot
        :param player_cards: List of cards allocated to the player

        Returns:
        Returns the game result i.e. whether the player or robot won
        """
        player_result = {'player_won': False, 'robot_won': False}

        desired_suit = self.__get_desired_suit(selected_suit, card_value)

        # Check if the list of desired cards is a subset of player_cards
        is_player_card_matched = any(set(item) <= set(
            player_cards) for item in desired_suit)

        # Check if the list of desired cards is a subset of robot_cards
        is_robot_card_matched = any(set(item) <= set(
            robot_cards) for item in desired_suit)

        if is_player_card_matched and not is_robot_card_matched:
            player_result.update({'player_won': True})
        elif is_robot_card_matched and not is_player_card_matched:
            player_result.update({'robot_won': True})
        else:
            return player_result

        return player_result
