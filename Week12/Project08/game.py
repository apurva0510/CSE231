from board import Ship,Board #important for the project

# # Uncomment the following lines when you are ready to do input/output tests!
# # Make sure to uncomment when submitting to Codio.
# import sys
# def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str

class Player(object):
    """
        Construct a player with a given name, board, and list of ships.
    """
    def __init__(self, name, board, ship_list=[]):
        """
            Initialize the player with a given name, board, and list of ships.
        """
        self.name = str(name)
        self.board = board
        self.ship_list = ship_list
        self.guesses = []

    def validate_guess(self, guess):
        """
            Validate the guess and raise appropriate exceptions if the guess is invalid.
        """
        # Check if guess has already been made
        if guess in self.guesses:
            raise RuntimeError("This guess has already been made!")
        # Check if guess is a valid location
        if not self.board.is_valid_location(guess):
            raise RuntimeError("Guess is not a valid location!")

    def get_player_guess(self):
        """
        Reads a guess from the user and returns it as a tuple of two integers.
        """
        while True:
            # Get the guess from the user
            guess_str = input("Enter your guess: ")
            # Convert the guess to a tuple of integers
            guess_parts = guess_str.split(",")
            try:
                row = int(guess_parts[0].strip())
                col = int(guess_parts[1].strip())
                guess = (row, col)
                self.validate_guess(guess)
                return guess
            except ValueError or IndexError or RuntimeError:
                # If the guess is invalid, ask the user to enter another guess
                continue

    def set_all_ships(self):
        # Iterate through the list of ships
        for ships in self.ship_list:
            while True:
                try:
                    # Get the position and orientation of the ship from the user
                    position = input("Enter the coordinates of the ship of size {}: ".format(ships))
                    # Convert the position to a tuple of integers
                    position = tuple(int(coord) for coord in position.split(","))
                    orientation = input("Enter the orientation of the ship of size {}: ".format(ships))
                    ship = Ship(ships, position, orientation)
                    # Validate the ship coordinates and place the ship on the board
                    if self.board.validate_ship_coordinates(ship):
                        self.board.place_ship(ship)
                        break
                except RuntimeError as e:
                    # If the ship coordinates are invalid, ask the user to enter another ship
                    print(e)


class BattleshipGame(object):
    """
        Construct a battleship game with two players.
    """

    def __init__(self, player1, player2):
        """
            Initialize the battleship game with two players.
        """
        self.player1 = player1
        self.player2 = player2

    def check_game_over(self):
        """
            Check if the game has ended and return the name of the winning player.
            If the game is not over, return an empty string.
        """
        for player in [self.player1, self.player2]:
            # Check if all ships of the player have been sunk
            if all(ship.is_sunk == True for ship in player.board.ships):
                # Return the name of the winning player
                return self.player1.name if self.player2.board.ships else self.player2.name
        # If the game is not over, return an empty string
        return ""
    
    def display(self):
        """
            Display the current state of the game.
        """
        # Print player 1's board
        print("{}'s board:".format(self.player1.name))
        print(str(self.player1.board))
        
        # Print player 2's board
        print("{}'s board:".format(self.player2.name))
        print(str(self.player2.board))

    def play(self):
        """
            Run the entire game until one of the players has won.
        """
        # Part One: Place ships on the board
        self.player1.set_all_ships()
        self.player2.set_all_ships()

        # Part Two: Start sinking ships
        while True:
            # Display current state of the game
            self.display()

            # Player 1's turn
            print("{}'s turn.".format(self.player1.name))
            # Get the guess from the user
            guess = self.player1.get_player_guess()
            # Apply the guess to the board and check if the game is over
            self.player2.board.apply_guess(guess)
            if self.check_game_over() != "":
                print("{} wins!".format(self.check_game_over()))
                break

            # Player 2's turn
            print("{}'s turn.".format(self.player2.name))
            # Get the guess from the user
            guess = self.player2.get_player_guess()
            # Apply the guess to the board and check if the game is over
            self.player1.board.apply_guess(guess)
            if self.check_game_over() != "":
                print("{} wins!".format(self.check_game_over()))
                break

            # Ask players if they want to continue playing
            continue_playing = input("Continue playing?: ")
            if continue_playing == 'q':
                break