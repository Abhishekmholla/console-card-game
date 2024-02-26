from card_functionality import CardFunctionality
from create_deck import CreateDeck
from game_functionality import GameFunctionality


def play_game():
    """
    This function manages the entire workflow of the game

    """

    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    suits = {1: ["♥", "♦", "♣", "♠"], 2: ["😃", "😈", "😵", "🤢", "😨"], 
             3: ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]}

    selected_suit = []
    deck = []
    player_cards = []
    robot_cards = []
    is_game_started = False

    print("Hello my fellow challenger!!\n"
          "Welcome to Monash-Card Game")
    while len(player_cards) <= 6:

        GameFunctionality.get_game_menu()

        if not is_game_started:
            print(f"Here are the suits you can choose from: \n"
                  f"Suit 1 : {suits.get(1)}\n"
                  f"Suit 2 : {suits.get(2)}\n"
                  f"Suit 3 : {suits.get(3)}\n"
                  )

            print("You can choose your option and suit together by providing an input like 1 2. If nothing is provided then by default the first suit will be chosen")

            player_options = input("Please opt your option and suit: ").split()

        else:
            player_options = input("Please opt your option : ").split()

        # If the player enters a non digit value for game option, show error
        if len(player_options) > 0 and not player_options[0].isdigit():
            print(f"The input provided {player_options[0]} is invalid!!!")
            continue

        # If the player enters a non digit value for suit option, show error
        if len(player_options) > 1 and not player_options[1].isdigit():
            print(f"The input provided {player_options[1]} is invalid!!!")
            continue

        # If the player doesn't give any options, show error
        if len(player_options) == 0:
            print(f"The input provided is invalid. Please provide a valid input")
            continue

        # If the player chooses a value more than 6 for game options, show error
        if int(player_options[0]) > 6:
            print(f"The input provided {player_options[0]} is invalid!!!")
            continue

        # If the player chooses a value more than 3 for suit options, show error
        if len(player_options) > 1 and int(player_options[1]) > 3:
            print(f"The input provided {player_options[1]} is invalid. Please enter a value between 1 and 3")
            continue

        if not is_game_started and int(player_options[0]) == 1:

            is_game_started = True

            # If the player doesn't give any input for the second option, 
            #then by default selecting the suit 1
            if (len(player_options)) == 1 or player_options[1] == "":
                player_options.append('1')

            player_suit_option = input("Please enter the number of items you want in the suit? ")
            
            # If the player enters a non digit value for suit option, show error
            if not player_suit_option.isdigit():
                print(f"The input provided {player_suit_option} is invalid!!!")
                is_game_started = False
                continue

            suit_selected = suits.get(int(player_options[1]))

            # If the length of the suit requested by the player 
            # is greater than that of main suit, throw exception
            if int(player_suit_option) > len(suit_selected):
                print(f"The input provided {int(player_suit_option)} is more than the suit length. "
                      f"Please enter a value between 2 and {len(suit_selected)}")
                is_game_started = False
                continue

            # If the length of the suit requested by the player 
            # is lesser than 2, throw exception
            elif int(player_suit_option) < 2:
                print(f"The input provided {int(player_suit_option)} is less than the permissible limit "
                      f"Please enter a higher value!!!")
                is_game_started = False
                continue
            
            # Appending to the selected suit list
            selected_suit.extend(suit_selected[:int(player_suit_option)])
            
            print("\n\033[1mTHE GAME HAS BEGUN!!\033[0m\n"
                  "\nGenerating your deck......\n")
            
            deck = CreateDeck(values, selected_suit) 

            card_functions = CardFunctionality()
            card_functions.shuffle_deck(deck.card_deck, selected_suit)
            continue

        elif is_game_started and int(player_options[0]) == 2:

            # The player can give only multi-input when he 
            # starts the game, blocking it in all other options
            if len(player_options) != 1 and player_options[1] != "":
                print(f"The input provided {player_options[1]} is invalid!!!")
                continue

            cards = card_functions.pick_card(deck.card_deck)
            
            print(f"\nThis is your {len(player_cards) + 1} move\n")
            print(f"You picked {cards.get('player_card')} card")
            
            player_cards.append(cards.get('player_card'))
            robot_cards.append(cards.get('robot_card'))

            if len(player_cards) == 6:
                break

        elif is_game_started and int(player_options[0]) == 3:

            # The player can give only multi-input when 
            # he starts the game, blocking it in all other options
            if len(player_options) != 1 and player_options[1] != "":
                print(f"The input provided {player_options[1]} is invalid!!!")
                continue

            card_functions.shuffle_deck(deck, selected_suit)

        elif is_game_started and int(player_options[0]) == 4:

            # The player can give only multi-input when 
            # he starts the game, blocking it in all other options
            if len(player_options) != 1 and player_options[1] != "":
                print(f"The input provided {player_options[1]} is invalid!!!")
                continue
            
            # The player doesn't have any cards, then show message to pick cards
            if len(player_cards) == 0:
                print("You need to pick few cards to show")
                continue

            GameFunctionality.show_card(player_cards)

        elif is_game_started and int(player_options[0]) == 5:

            # The player can give only multi-input when 
            # he starts the game, blocking it in all other options
            if len(player_options) != 1 and player_options[1] != "":
                print(f"The input provided {player_options[1]} is invalid!!!")
                continue

            if len(player_cards) == 0:
                print("Please pick cards before checking result")
                continue

            GameFunctionality.print_outcome_of_game(player_cards, robot_cards, 
                                  selected_suit, values,is_game_started)

        elif int(player_options[0]) == 6:
            print("It is been a pleasure competing with you!! See you soon......")
            break

        elif is_game_started:
            print("The game has already started. Please proceed to pick few cards")
        else:
            print("Please start the game to proceed")

    is_game_started = False

    if len(player_cards) == 6:
        print("You have exhausted your picks.Evaluating the result.....")
        GameFunctionality.show_card(player_cards)
        GameFunctionality.print_outcome_of_game(player_cards, robot_cards, selected_suit, values,is_game_started)
        print("Thanks for playing this game.\n")

    if int(player_options[0]) != 6:
        play_game()

play_game()