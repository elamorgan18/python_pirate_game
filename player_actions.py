"""
This file contains the functions related to the player's merchant ship.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""
import common_actions

def get_user_direction():
    """ Getting the user direction"""
    direction = input("North, East, South or West? Type in N, E, S or W: ").upper()
    if direction == "N" or direction == "E" or direction == "S" or direction == "W":
        print(f"Your move was {direction}!")
    else:
        print("Invalid input! Please input either N, E, S, or W: ")
        direction = get_user_direction()

    return direction

def get_new_player_position(player_position, direction):
    """Getting the new player position"""

    old_player_position = player_position
    new_player_position = player_position

    first_position_row = old_player_position[0]
    first_position_column = old_player_position[1]

    # First index of row is 0 so we don't want it to go to -1 as it does not exist- hit boundry
    if direction == "N":
        if first_position_row != 0:
            new_player_position = (first_position_row - 1, first_position_column)
        else:
            new_player_position = (first_position_row, first_position_column)
            print("You did not move North because you hit the boundry!!")

    # Last index of column is 9 so we don't want it to go over to 10 as it does not exist-
    # hit boundry
    elif direction == "E":
        if first_position_column != 9:
            new_player_position = (first_position_row, first_position_column + 1)
        else:
            new_player_position = (first_position_row, first_position_column)
            print("You did not move East because you hit the boundry!!")

    # Last index of row is 9 so we don't want it to go over to 10 as it does not exist- hit boundry
    elif direction == "S":
        if first_position_row != 9:
            new_player_position = (first_position_row + 1, first_position_column)
        else:
            new_player_position = (first_position_row, first_position_column)
            print("You did not move South because you hit the boundry!!")

    # First index of column is 0 so we don't want it to go to -1 as it does not exist- hit boundry
    elif direction == "W":
        if first_position_column != 0:
            new_player_position = (first_position_row, first_position_column - 1)
        else:
            new_player_position = (first_position_row, first_position_column)
            print("You did not move West because you hit the boundry!!")

    return new_player_position


def is_position_safe(grid, new_position):
    """This function determines if the players new position is something other than a dot. 
    This return value will determine in the main.py if the player will either move or be killed."""

    row = new_position[0]
    col = new_position[1]
    if grid[row][col] == "." or grid[row][col] == "B":
        return True
    else:
        return False

def is_position_beach(grid, new_position):
    """This function chacks if the new_player_position has landed on the beach. 
    The return value will be used in main.py to see if the player has won or the 
    game should continue."""
    row = new_position[0]
    col = new_position[1]
    if grid[row][col] == "B":
        return True
    else:
        return False

def move_player(grid, old_player_position, new_player_position):
    """Passing in character M to be changed"""
    common_actions.operate_on_ship(grid, old_player_position, new_player_position, "M")

def kill_player(grid, old_player_position, new_player_position):
    """Passing in character X to be changed"""
    common_actions.operate_on_ship(grid, old_player_position, new_player_position, "X")
    print("The Merchant has been killed! You lose!")
