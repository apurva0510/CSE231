class Ship(object):
    """
        Construct a ship with a given length, position and orientation with the ability to apply hits to the ship.
    """
    def __init__(self, length, position, orientation):
        """
            Initialize the length, position and orientation of the ship.
        """
        self.length = int(length)
        self.orientation = orientation
        # Create a list of positions that the ship occupies based on the orientation
        if self.orientation == "h":
            self.position = [(position[0], position[1] + i) for i in range(self.length)]
        else:
            self.position = [(position[0] + i, position[1]) for i in range(self.length)]
        self.hit_count = 0
        self.is_sunk = False

    def get_positions(self):
        """
            Return a list of positions that the ship occupies.
        """
        return self.position

    def get_orientation(self):
        """
            Return the orientation of the ship.
        """
        return self.orientation

    def apply_hit(self):
        """
            Increment the hit count of the ship.
        """
        self.hit_count += 1
        # Check if the ship is sunk
        if self.hit_count == self.length:
            self.is_sunk = True


class Board(object):
    """
        Construct a board with a given size and the ability to place ships on the board and apply guesses to the board.
    """
    def __init__(self, size):
        """
            Initialize the board with a given size and an empty list of ships.
        """
        self.size = size
        # Create an empty board
        self.board = [[" " for i in range(self.size)] for j in range(self.size)]
        self.ships = []

    def place_ship(self, ship):
        """
            Place a ship on the board and add it to the list of ships.
        """
        self.ships.append(ship)
        positions = ship.get_positions()
        # Place the ship on the board
        for position in positions:
            self.board[position[0]][position[1]] = "S"

    def apply_guess(self, guess):
        """
            Check if the guess has hit any ship and update the board accordingly.
        """
        # Get the row and column of the guess
        row, column = guess

        # Check if the guess has hit any ship
        for ship in self.ships:
            positions = ship.get_positions()
            if (row, column) in positions:
                ship.apply_hit()
                self.board[row][column] = "H"
                print("Hit!")
                return
    
        # If the guess has not hit any ship, update the board accordingly
        self.board[row][column] = "M"
        print("Miss!")

    def validate_ship_coordinates(self, ship):
        """
            Check if the coordinates of the ship are valid.
        """
        if ship.get_orientation() == "h":
            # Iterate through the positions of the ship
            for position in ship.get_positions():
                try:
                    # Check if the position is already occupied
                    if self.board[position[0]][position[1]] != " ":
                        raise RuntimeError("Ship coordinates are already taken!")
                except IndexError:
                    # Check if the position is out of bounds
                    raise RuntimeError("Ship coordinates are out of bounds!")
        elif ship.get_orientation() == "v":
            # Iterate through the positions of the ship
            for position in ship.get_positions():
                try:
                    # Check if the position is already occupied
                    if self.board[position[0]][position[1]] != " ":
                        raise RuntimeError("Ship coordinates are already taken!")
                except IndexError:
                    # Check if the position is out of bounds
                    raise RuntimeError("Ship coordinates are out of bounds!")
        return True

    def is_valid_location(self, guess):
        """
            Check if the guess is a valid location on the board.
        """
        # Get the row and column of the guess
        row, column = guess
        # Check if the guess is out of bounds and return False if it is
        if row < 0 or row >= self.size or column < 0 or column >= self.size:
            return False
        return True

    def __str__(self):
        """
            Return a string representation of the board.
        """
        # Create a string representation of the board
        return "\n".join(["".join(["[" + j + "]" for j in i]) for i in self.board]) + "\n"