"""
This file contains the functions related to the player's merchant ship.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""
import numpy
import common_actions

def get_new_enemy_position(enemy_position, player_position):
    """
    I've filled in this function for you, do not change it.
    This function computes the enemy's next position, based on where the player
    is. This doesn't actually move the enemy ship, just tells you where
    the enemy's next move should be.

    Note that it handles the positions as two integers, (row, column). i.e.
    down then across. If you have handled the coordinates differently in your
    code that's fine, but in your main code you may need to handle how you pass
    the positions to this function, and how you handle the results of this
    function. If you get it wrong you may see the pirates running away from the
    merchant ship :-)

    Also note: this code works whether you use a toroidal ("wraparound") grid
    or a bounded grid, but it may possibly affect the difficulty...

    :param enemy_position: The enemy's position (row, column)
    :param player_position: The player's position (row, column)
    :return: The enemy's updated position (row, column)
    :rtype: tuple
    """
    row = \
        enemy_position[0] + numpy.sign(player_position[0] - enemy_position[0])
    column = \
        enemy_position[1] + numpy.sign(player_position[1] - enemy_position[1])
    new_enemy_position = (row, column)


    return new_enemy_position

def has_caught_player(enemy_position, player_position):
    """Getting the index of enemy and player and putting them together""" 
    new_player_row = player_position[0]
    new_player_col = player_position[1]

    # Getting the coordinates that are adjecent to the player
    adjacent_up = (new_player_row - 1, new_player_col)
    adjacent_down = (new_player_row + 1, new_player_col)
    adjacent_right = (new_player_row, new_player_col + 1)
    adjacent_left = (new_player_row, new_player_col - 1)
    adjacent_topleft = (new_player_row - 1, new_player_col - 1)
    adjacent_topright = (new_player_row - 1, new_player_col + 1)
    adjacent_bottomleft = (new_player_row + 1, new_player_col - 1)
    adjacent_bottomright = (new_player_row + 1, new_player_col + 1)

    # Returning True if the player is caught, returning False if player has not been caught
    if enemy_position == player_position or enemy_position == adjacent_left\
        or enemy_position == adjacent_right\
        or enemy_position == adjacent_down or enemy_position == adjacent_up\
        or enemy_position == adjacent_bottomleft \
        or enemy_position == adjacent_bottomright or enemy_position == adjacent_topleft\
        or enemy_position == adjacent_topright:
        return True
    else:
        return False

def move_enemy(grid, old_enemy_position, new_enemy_position):
    """Putting P in the new enemy position"""
    common_actions.operate_on_ship(grid, old_enemy_position, new_enemy_position, "P")

def kill_enemy(grid, old_enemy_position, new_enemy_position):
    """Putting W in the new enemy position"""
    common_actions.operate_on_ship(grid, old_enemy_position, new_enemy_position, "W")
    print("The Pirate has been killed! You Win!")
