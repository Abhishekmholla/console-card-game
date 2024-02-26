class CreateDeck():
    
    def __init__(self, card_values, selected_suit) -> None:
        """Creates a deck using values and suit

        Parameters:
        :param selected_suit: suit selected by the player
        :param card_values: Dictionary of card values
        :param card_deck: List of cards in the deck
        """
        self.card_deck = list()
        self.card_values = card_values
        self.selected_suit = selected_suit
        self.create_deck()
    
    def create_deck(self):
        """
        This function creates a deck using the values and suit
        """
        # Generating a deck by mapping each card value to suit value
        for value in self.card_values:
            for suit_value in self.selected_suit:
                self.card_deck.append(value + suit_value)
    
        # return card_deck