# My Python Pirate Ship Game

The game is played from the command line.

The Game:
‘You are a merchant ship sailing the Caribbean when you are attacked by pirates. Lure
them onto the rocks to escape.’

The user is asked their desired difficulty between 1 and 10. Lower difficulty means more
rocks; higher difficulty means fewer rocks. The game takes place on a 10x10 2D grid
which is displayed at the start of the game, and then after every turn. Rocks are randomly
placed and are represented by asterisks *, the merchant ship (i.e., the user) by “M”, and
the pirate ship by “P”.

Each turn the user is asked which direction they would like to move, and their ship is
moved followed by the enemy ship. The merchant ship may only move one space North,
East, South, or West. The pirate ship always moves one space toward the player and can
move North/East/South/West or diagonally (i.e., like a king in chess).

The pirates are so bloodthirsty that they head towards the player and do not notice any
rocks until it is too late. If the pirates move onto a space that contains a rock, they sink
(their icon is turned to “W”) and the player wins. If the merchant ship moves onto a space
that contains a rock, they sink (their icon is turned to “X”) and the player loses. If the
pirates move onto a space occupied by the merchant ship, or a space adjacent to the
merchant ship, then the merchant ship is captured (their icon is turned to “X”) and the
player loses.
