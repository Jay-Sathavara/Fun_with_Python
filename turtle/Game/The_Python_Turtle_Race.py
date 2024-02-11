# J_P_0030

import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

def roll_die(player):
    input("Press Enter to roll the die for {}...".format(player))
    die_outcome = random.choice(die)
    print("The result of the die roll is: ", die_outcome)
    print("The number of steps will be: ", 20 * die_outcome)
    player.forward(20 * die_outcome)

def check_victory(player, winning_position):
    if player.pos() >= winning_position:
        input("{} Wins! Press Enter to exit...".format(player))
        turtle.done()  # End the game if someone wins

def player_one_turn(player, winning_position):
    roll_die(player)
    check_victory(player, winning_position)

def player_two_turn(player, winning_position):
    roll_die(player)
    check_victory(player, winning_position)

# Game loop
for i in range(20):
    player_one_turn(player_one, (300, 60))  # Adjust winning positions as needed
    player_two_turn(player_two, (300, -140))

# Keep the window open even if no one wins
turtle.done()
