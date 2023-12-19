'''
CSE 231 Project 8

Algorithm:
    1. Create a board class that will be used to create the board for the game
    2. Create a ship class that will be used to create the ships for the game
    3. Create a player class that will be used to create the players for the game
    4. Create a game class that will be used to create the game and play the game   
    5. Create a main function that will be used to run the game
        i. Create the board size and ship list
        ii. Initialize the board
        iii. Initialize the players
        iv. Initialize the game
        v. Play the game until the user quits or the game is over
'''

from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project


def main():
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]

    # Initialize the board of each player
    player1_board = Board(board_size)
    player2_board = Board(board_size)

    # Initialize the players
    player_1 = Player("Player 1", player1_board, ship_list)
    player_2 = Player("Player 2", player2_board, ship_list)

    # Initialize the game
    game = BattleshipGame(player_1, player_2)

    # Play the game
    game.play()


if __name__ == "__main__":
    main()