from random import choice
from os import system, path


def setup():
    '''Sets up the game.'''
    ans = input(
        "\nWould you like to play a game of Blackjack? Type 'y' to play, 'n' to exit.\n")
    if ans == "y":
        system("clear")
        read_art_file()
        start_game()
        return
    elif ans == "n":
        print("Thank you for playing Blackjack.\n")
        return
    else:
        print("Invalid input\n")
        setup()


def start_game():
    '''Main game function, containing the game loop'''
    # 4 different card types
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

    # Lists to store cards of players
    dealer_cards = []
    player_cards = []

    # Drawing initial cards
    for _ in range(2):
        draw_card(player_cards, cards)
        draw_card(dealer_cards, cards)

    print(
        f"\tYour cards: {player_cards} | Your current score: {sum(player_cards)}")
    print(f"\tDealer's first card: {dealer_cards[0]}\n")

    while True:
        ans = input("Type 'd' to draw another card, 'r' to reveal cards.\n")

        if ans == "d":
            draw_card(player_cards, cards)  # Player draws card
            draw_card(dealer_cards, cards)  # Dealer draws card

            # Ace can be 1 or 11, and sum cannot exceed 21 because of Ace
            if 11 in player_cards and sum(player_cards) > 21:
                player_cards.remove(11)
                player_cards.append(1)

            if 11 in dealer_cards and sum(dealer_cards) > 21:
                dealer_cards.remove(11)
                dealer_cards.append(1)

            # Sum of either can't exceed 21
            if sum(player_cards) > 21 or sum(dealer_cards) > 21:
                print("Total score went over 21!")
                print(
                    f"\tYour final cards: {player_cards} | Your final score: {sum(player_cards)}")
                print(
                    f"\tDealer's final cards: {dealer_cards} | Dealer's final score: {sum(dealer_cards)}")

                score_checker(player_cards, dealer_cards)
                setup()

                break

            else:
                print(
                    f"\tYour cards: {player_cards} | Your current score: {sum(player_cards)}")
                print(f"\tDealer's first card: {dealer_cards[0]}\n")

        elif ans == "r":
            print(
                f"\tYour final cards: {player_cards} | Your final score: {sum(player_cards)}")
            draw_dealer_cards(dealer_cards, cards)
            print(
                f"\tDealer's final cards: {dealer_cards} | Dealer's final score: {sum(dealer_cards)}")

            score_checker(player_cards, dealer_cards)
            setup()
            break

        else:
            print("Invalid input")


def draw_card(cards_in_hand, all_cards):
    '''Draws and adds card to the hand, while removing the card from all cards'''
    card = choice(all_cards)
    all_cards.remove(card)
    cards_in_hand.append(card)


def draw_dealer_cards(dealer_cards, all_cards):
    '''Gives dealer extra cards if total is less than 17'''
    while sum(dealer_cards) < 17:
        draw_card(dealer_cards, all_cards)

        # Sum cannot exceed 21 because of ace
        if 11 in dealer_cards and sum(dealer_cards) > 21:
            dealer_cards.remove(11)
            dealer_cards.append(1)


def score_checker(player_cards, dealer_cards):
    '''Checks for winner/loser/draw'''
    if sum(player_cards) > 21 and sum(dealer_cards) > 21:
        print("Its a draw!")

    elif sum(player_cards) > 21:
        print("You lose!")

    elif sum(dealer_cards) > 21:
        print("You win!")

    elif sum(player_cards) > sum(dealer_cards):
        print("You win!")

    elif sum(player_cards) < sum(dealer_cards):
        print("You lose!")

    else:
        print("Its a draw!")


def read_art_file():
    '''Prints Blackjack ASCII art to the terminal'''
    # Get the directory of the script
    file_directory = path.dirname(__file__)

    # Combine with the file's name
    file_path = path.join(file_directory, 'art.txt')

    with open(file_path, "r") as art_file:
        print(art_file.read() + "\n")


setup()
