# CSE 231 Project 7
#
# Algorithm:
#   Define the board and the players.
#   Display the banner, rules, and menu.
#   Start the game in phase 1.
#   Loop until a player has less than 3 pieces on the board: 
#       a. Get the current player. 
#       b. If the player has less than 3 pieces, end the game. 
#       c. If the player has more than 3 pieces, ask the player to make a move: 
#           i. If it's phase 1, ask the player to place a piece on the board. 
#           ii. If it's phase 2, ask the player to move a piece on the board. 
#       d. If the move is valid, update the board and check if a mill was formed. 
#           i. If a mill was formed, remove an opponent's piece. 
#       e. If the move is not valid, ask the player to make another move. 
#       f. If the move is valid and no mill was formed, switch to the other player.
#   Display the winner and end the game.
#   Except:
#       If the player asks for help, display the menu.
#       If the player quits, end the game.
#       If the player restarts, start the game over.


import sys
import NMM  # This is necessary for the project

BANNER = """
    __      _(_)_ __  _ __   ___ _ __| | |
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| | |
     \ V  V /| | | | | | | |  __/ |  |_|_|
      \_/\_/ |_|_| |_|_| |_|\___|_|  (_|_)
"""

RULES = """                                                                                       
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    The game is ends when a player (the loser) has less than three 
    pieces on the board.
"""

MENU = """
    Game commands (first character is a letter, second is a digit):
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game

"""


# # Uncomment the following lines when you are ready to do input/output tests!
# # Make sure to uncomment when submitting to Codio.
# def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str


def count_mills(board, player):
    """
    Count how many mills are held by the player.

    Args:
        board (list): The current state of the board.
        player (str): The player to count mills for.

    Returns:
        int: The number of mills held by the player.
    """
    #initialize mill count
    mill_count = 0
    #loop through each mill
    for mill in board.MILLS:
        #if all three points in the mill are the same as the player, increment mill count
        if all([board.points[mill[0]] == player, board.points[mill[1]] == player, board.points[mill[2]] == player]):
            mill_count += 1
    return mill_count


def place_piece_and_remove_opponents(board, player, destination):
    """
    Place a piece at the destination and remove an opponent's piece if a mill was created.
    
    Args:
        board (list): The current state of the board.
        player (str): The player to place a piece for.
        destination (str): The point to place the piece at.
    
    Returns:
        None
    """
    # Check if the destination is a valid spot to place a piece
    if destination not in board.points.keys():
        raise RuntimeError("Invalid placement")

    # Check the number of existing mills
    mills_before = count_mills(board, player)

    # Place the piece at the destination
    board.assign_piece(player, destination)

    # Check if a new mill was created
    mills_after = count_mills(board, player)

    if mills_after > mills_before:
        print("A mill was formed!")
        print(board)
        # Remove an opponent's piece
        remove_piece(board, get_other_player(player))


def move_piece(board, player, origin, destination):
    """
    Move a piece from the origin point to the destination point.

    Args:
        board (list): The current state of the board.
        player (str): The player making the move.
        origin (str): The point where the piece is currently located.
        destination (str): The point where the piece will be moved to.

    Returns:
        None
    """
    # Check if the origin and destination are valid spots
    if origin not in board.points.keys() or destination not in board.points.keys():
        raise RuntimeError("Invalid command: Not a valid point")
    elif board.points[origin] == " ":
        raise RuntimeError("Invalid command: Not a valid point")
    # Check if the origin point is occupied by the player who is moving
    elif board.points[origin] != player:
        raise RuntimeError("Invalid command: Origin point does not belong to player")
    # If phase 2, check for adjacency
    elif destination not in board.ADJACENCY[origin]:
        raise RuntimeError("Invalid movement")
    else:
        # Clear the origin point
        board.clear_place(origin)
        # Place the piece at the destination and remove an opponent's piece if a mill was created
        place_piece_and_remove_opponents(board, player, destination)


def points_not_in_mills(board, player):
    """
    Get a list of all points occupied by the player that are not in mills.

    Args:   
        board (list): The current state of the board.
        player (str): The player to get points for.
    
    Returns:
        player_points (list): A list of all points occupied by the player that are not in mills.
    """
    # initialize list of all points occupied by player
    player_points = []

    # add all points occupied by player to list
    for point in board.points:
        if board.points[point] == player:
            player_points.append(point)
    
    # remove points in mills from list
    for mill in board.MILLS:
        if all([board.points[mill[0]] == player, board.points[mill[1]] == player, board.points[mill[2]] == player]):
            for point in mill:
                if point in player_points:
                    player_points.remove(point)
    
    return player_points
        


def placed(board, player):
    """
    Get the list of pieces placed by the player.

    Args:
        board (list): The current state of the board.
        player (str): The player to get pieces for.

    Returns:
        player_points (list): A list of all points occupied by the player.
    """
    # initialize list of all points occupied by player
    player_points = []

    # add all points occupied by player to list
    for point in board.points:
        if board.points[point] == player:
            player_points.append(point)
    
    return player_points


def remove_piece(board, player):
    """
    Remove a piece belonging to player from board.

    Args:
        board (Board): The current state of the board.
        player (str): The player whose piece will be removed.

    Returns:
        None
    """
    # get list of all points occupied by player
    valid_points = points_not_in_mills(board, player)
    player_points = placed(board, player)
    if len(valid_points) == 0:
        valid_points = player_points
    
    while True:
        # prompt for point to remove
        point = input("Remove a piece at :> ")
        try:
            # check if point is valid
            if board.points[point] != player or board.points[point] == " ":
                print("Invalid command: Point does not belong to player\nTry again.")
                continue
            if point not in valid_points:
                print("Invalid command: Point is in a mill\nTry again.")
                continue
            board.clear_place(point)
        except KeyError:
            print("Invalid command: Not a valid point\nTry again.")
            continue
        break


def is_winner(board, player):
    """
    Determine if the player has won the game.

    Args:
        board (list): The current state of the board.
        player (str): The player to check for a win.
    
    Returns:
        bool: True if the player has won the game, False otherwise.
    """
    # check if player has less than 3 pieces
    return len(placed(board, get_other_player(player))) < 3


def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"


def main():
    # Loop so that we can start over on reset
    while True:
        # Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0  # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent

        # PHASE 1
        phase = 1
        print(player + "'s turn!")
        # placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        # Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            if command == 'h': # Display menu
                print(MENU)
                command = input("Place a piece at :> ").strip().lower()
            elif command == 'r': # Restart game
                break

            try:
                # Place the piece
                place_piece_and_remove_opponents(board, player, command)
                # Increment the number of pieces placed
                placed_count += 1
                # Switch players
                player = get_other_player(player)

            # Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            # Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

        # Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        phase = 2
        while command != 'q':
            if command == 'h': # Display menu
                print(MENU)
                command = input("Place a piece at :> ").strip().lower()
            elif command == 'r': # Restart game
                break

            # commands should have two points
            command = command.split()
            try:
                # Move the piece
                try:
                    move_piece(board, player, command[0], command[1])
                except IndexError:
                    raise RuntimeError("Invalid number of points")
                # Check for a winner
                if is_winner(board, player):
                    print(BANNER)
                    return
                # Switch players
                player = get_other_player(player)

            # Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                # Display and reprompt
            print(board)
            # display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

        # If we ever quit we need to return
        if command == 'q':
            return


if __name__ == "__main__":
    main()