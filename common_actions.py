

"""
This file contains the functions related to both pirate and merchant
Making sure that we do not repeat code. Keeping everything simple
"""

def operate_on_ship(grid, old_ship_position, new_ship_position, character):
    """Changes the character for either pirate or ship from a dot to character passed in."""
    new_ship_row = new_ship_position[0]
    new_ship_col = new_ship_position[1]

    # Putting the passed in character into the grid
    grid[new_ship_row][new_ship_col] = character

    # Putting . in the old ship position
    old_ship_row = old_ship_position[0]
    old_ship_col = old_ship_position[1]

    grid[old_ship_row][old_ship_col] = "."
    