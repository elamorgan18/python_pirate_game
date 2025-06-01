"""
This file contains the functions that setup the game: creating a grid, placing
rocks and ships. You will need to finish these functions.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""
import random

def create_grid(size):
    """Creating the grid function"""
    grid = []

    # In this code, i equals the row of the grid, and j is the column of the grid.
    # Both will start at zero as they start from 0 index.
    # I had to use underscore to avoid pylint errors
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(".")
        grid.append(row)

    return grid

def add_rocks(grid, difficulty):
    """Adding the rocks on to the grid"""
    num_of_rocks = 15 - int(difficulty)
    print(f'Number of rocks: {num_of_rocks}')

    for _ in range(num_of_rocks):
        rock_added = False
        # Making sure that we haven't already got a rock, not overlapping our coordinates.
        while not rock_added:
            random_row = random.randint(0, 9)
            random_col = random.randint(0, 9)

            if grid[random_row][random_col] != "*":
                grid[random_row][random_col] = "*"
                rock_added = True

    return grid


def place_player(grid):
    """Adding player on to the grid"""
    player_added = False

    while not player_added:
        random_row = random.randint(0, 9)
        random_col = random.randint(0, 9)
        player_position = (random_row, random_col)

        if grid[random_row][random_col] == ".":
            grid[random_row][random_col] = 'M'
            player_added = True

    return grid, player_position

def place_enemy(grid):
    """Adding the enemy on to the grid"""
    enemy_added = False
    while not enemy_added:
        random_row = random.randint(0, 9)
        random_col = random.randint(0, 9)
        enemy_position = (random_row, random_col)

        if grid[random_row][random_col] == ".":
            grid[random_row][random_col] = 'P'

            enemy_added = True

    return grid, enemy_position

def print_grid(grid):
    """Printing the grid function"""
    for row in grid:
        row_to_print = ""
        for item in row:
            row_to_print = row_to_print + " " + item
        print(row_to_print)

def level_of_difficulty():
    """I have added this function so that the user can input their desired difficulty"""
    # Prompts the user for level of difficulty. Input has to be between 1 and 10 or invalid input
    #  message will display and make them try again.
    user_input = input("Enter Level of Difficulty, from 1 (easy) to 10 (hard): ")
    if user_input.isdigit() and int(user_input) >= 1 and int(user_input) <= 10:
        print("Valid input")
    else:
        print("Invalid input. Please put in number between 1 and 10!")
        level_of_difficulty()

    return user_input
