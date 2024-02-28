import random

from game_functionality import GameFunctionality


class CardFunctionality():

    def __init__(self) -> None:
        self.cards = {'player_card': '', 'robot_card': ''}

    def shuffle_deck(self, card_deck, selected_suit):
        """
        This function shuffles the deck with specific cards at
        first,middle and last index of the card_deck list

        Parameters:
        :param selected_suit: suit selected by the player
        :param card_deck: List of cards in the deck

        Returns:
        Doesn't return anything
        """
        GameFunctionality.print_message("\nShuffling deck....")

        GameFunctionality.print_message(
            "Let's have a look at our deck before shuffling!")
        # Randomly shuffling the entire deck
        print(card_deck)
        random.shuffle(card_deck)
        self.__move_deck_item(card_deck, selected_suit)
        GameFunctionality.print_message(
            '\nHere is your deck after shuffling!\n')
        print(card_deck)

    def pick_card(self, card_deck):
        """
        This function picks a card randomly from the card_deck

        Parameters:
        :param card_deck: List of cards in the deck

        Returns:
        Returns a card selected by the user
        """

        # Generate a random number index for the player
        random_player_card_index = random.randint(0, len(card_deck))

        # If the index is found in the deck,
        # then insert into dictionary and delete it from the existing list
        if random_player_card_index in range(0, len(card_deck)):
            self.cards['player_card'] = card_deck[random_player_card_index]
            card_deck.pop(random_player_card_index)

        # Generate a random number index for the robot but with a large range
        random_robot_card_index = random.randint(-20, len(card_deck))

        # If the index is found in the deck,
        # then insert into dictionary and delete it from the existing list
        if random_robot_card_index in range(0, len(card_deck)):
            self.cards['robot_card'] = card_deck[random_robot_card_index]
            card_deck.pop(random_robot_card_index)

        return self.cards

    def __move_deck_item(self, card_deck, selected_suit):
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
