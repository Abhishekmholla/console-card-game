from game_rules import game_rules


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
    
    @staticmethod
    def print_outcome_of_game(player_cards, robot_cards, selected_suit, card_values, is_game_started):
        game_rule = game_rules()
        game_result = game_rule.check_result(player_cards, robot_cards, selected_suit, card_values)
        
        if is_game_started:
            if game_result.get('player_won'):
                print("\n\033[1mYou are leading mate!!! Keep picking....\033[0m")
            else:
                print("\n\033[1mYou are trailing mate!!!\033[0m")
        else:            
            if game_result.get('player_won'):
                print("\n\033[1mYippee!!! Congratulations you won.......\033[0m")
            else:
                print("\n\033[1mHard luck mate.....you lost the game\033[0m")
    
    @staticmethod
    def print_message(message):
        print(message)
            