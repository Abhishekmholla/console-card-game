class GameFunctionality():

    @staticmethod
    def get_game_menu():
        """
        This function displays all the valid options in the game

        Returns:
        Prints the various options in the game
        """
        print("\n-------------------------------------------------------------------------")
        print("Please select one of the following options\n"
            "1.Start game\n"
            "2.Pick a card\n"
            "3.Shuffle Deck\n"
            "4.Show my cards\n"
            "5.Check win or lose\n"
            "6.Exit\n")
    
    @staticmethod
    def show_card(player_cards):
        """
        This function displays all the cards with the player

        Parameters:
        :param player_cards: List of cards allocated to the player

        Returns:
        Prints all the cards that belongs to the player
        """
        print("Here is your set of cards mate!!!")
        print(",".join(player_cards))
        