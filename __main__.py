"""
This file contains the function calls to execute the game.
This should be the only place you have code outside of functions, and the more
code within functions the better. You should call the functions defined in the
other modules (setup_game, player_actions, enemy_actions). You are free to
define additional functions and modules if needed, but these should be in
addition to existing functions, rather than replacements.

Note: to call functions from other modules, you need to
include the module name; e.g. setup_game.create_grid()
"""

import setup_game
import player_actions
import enemy_actions
import beach_actions
import common_actions

if __name__ == "__main__":
    print("You are a merchant ship sailing the Caribbean when you are attacked by pirates.")
    print("Lure them onto the rocks to escape or get to the beach to win!")

    # START OF SETUP GAME

    # Calling the level_of_difficulty function
    game_difficulty = setup_game.level_of_difficulty()
    print(f'Level of difficulty: {game_difficulty}')

    # Defining the grid size
    grid_size = 10

    # Creating the inital grid with dots
    grid = setup_game.create_grid(grid_size)

    # Calling adding rocks to grid function - Grid now contains dots, rocks
    grid_with_rocks = setup_game.add_rocks(grid, game_difficulty)

    # Calling place_beach function - Grid now coontains dots, rocks, beach
    grid_with_beach, beach_pos = beach_actions.place_beach(grid_with_rocks)

    # Calling the adding player to grid function - Grid now contains dots,
    # rocks, beach, player
    grid_with_player, player_pos = setup_game.place_player(grid_with_beach)

    # Calling the adding enemy to grid function - Grid now contains dots,
    # rocks, player, enemy- Grid complete
    grid_with_enemy, enemy_pos = setup_game.place_enemy(grid_with_player)
    setup_game.print_grid(grid_with_enemy)

    # Not sure if this bit is needed, but it checks to see if pirate has already
    # caught merchant at the start of the game.
    if enemy_actions.has_caught_player(player_pos, enemy_pos) is True:
        print("Pirate has already caught merchant. Please try again!")
        should_game_continue = False
    else:
        should_game_continue = True

    # END OF SETUP_GAME FUNCTIONS

    # START OF PLAYER ACTIONS FUNCTIONS

    while should_game_continue is True:
        # Getting the user input for their move, N, E, S, W
        user_input_direction = player_actions.get_user_direction()
        new_player_position = player_actions.get_new_player_position(
            player_pos, user_input_direction)

        # If new player position and player position are the same, do it again
        # so that they are different.
        while new_player_position == player_pos:
            user_input_direction = player_actions.get_user_direction()
            new_player_position = player_actions.get_new_player_position(player_pos,
                                                                         user_input_direction)

        # If the new player postion is safe, they will be able to move (move_player()),
        #  otherwise they are dead (kill_player())
        is_position_safe = player_actions.is_position_safe(grid_with_enemy, new_player_position)
        if is_position_safe is True:
            # PART 1C- my additional feature
            # If the player position has landed on the beach, the player has won
            # and the game finishes
            is_position_beach = player_actions.is_position_beach(grid_with_enemy,
                                                                 new_player_position)
            if is_position_beach is True:
                print("You have landed on the Beach! You are safe! You win!")
                # Here I am turning the Merchant into W for win and game finishes
                common_actions.operate_on_ship(grid_with_enemy, player_pos,
                                               new_player_position, "W")
                should_game_continue = False
            else:
                # If not a beach, the player will continue to move
                should_game_continue = True
                player_actions.move_player(grid_with_enemy, player_pos, new_player_position)
        else:
            # If position is not safe, the player will die!
            player_actions.kill_player(grid_with_enemy, player_pos, new_player_position)
            should_game_continue = False

    # END OF PLAYER_ACTIONS FUNCITONS

    # START OF ENEMY_ACTIONS FUNCTIONS

        if should_game_continue is True:
            # Moving the enemy to a new posisiton
            new_enemy_position = enemy_actions.get_new_enemy_position(enemy_pos,
                                                                      new_player_position)

            # See if enemy goes on rock
            # Enemy is on a rock
            if player_actions.is_position_safe(grid_with_enemy, new_enemy_position) is False:
                enemy_actions.kill_enemy(grid_with_enemy, enemy_pos, new_enemy_position)
                should_game_continue = False

            # Not on a rock
            else:
                # Caught player- kill player
                if enemy_actions.has_caught_player(new_enemy_position, new_player_position) is True:
                    player_actions.kill_player(grid_with_enemy, player_pos, new_player_position)
                    enemy_actions.move_enemy(grid_with_enemy, enemy_pos, new_enemy_position)
                    # player_actions.kill_player(grid_with_enemy, player_pos, new_player_position)
                    should_game_continue = False
                else:
                    # Haven't caught player
                    enemy_actions.move_enemy(grid_with_enemy, enemy_pos, new_enemy_position)
                    enemy_pos = new_enemy_position


        # The new player position becomes the old player position so
        # that the game can loop and continue.
        player_pos = new_player_position
        setup_game.print_grid(grid_with_enemy)

     # END OF ENEMY_ACTIONS FUNCTIONS
