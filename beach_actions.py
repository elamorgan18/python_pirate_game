"""
This is used for part 1C of my project.
This file contains the functions related to the beach. 
This is an additional feature to the game. I thought that the merchant might
want to have a safe place to get to before either getting captured or killed,
or killing the pirate. If the merchant lands on the beach, the merchant wins!
"""
import random

def place_beach(grid):
    """Adding a beach onto the grid"""
    beach_added = False

    while not beach_added:
        random_row = random.randint(0, 9)
        random_col = random.randint(0, 9)
        beach_position = (random_row, random_col)

        if grid[random_row][random_col] == ".":
            grid[random_row][random_col] = 'B'
            beach_added = True

    return grid, beach_position
