#!/usr/bin/python3

import os

import random

class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

name = ''

def get_name():
    global name

    name = raw_input( tcolors.HEADER + "Hello, stranger! Name yourself: " + tcolors.ENDC )
    confirm = raw_input( tcolors.HEADER + "So, your name is " + name + ", right? [y/n] " + tcolors.ENDC ).lower()

    if confirm == "y":
        return name
    else:
        return get_name()

def show_rules():
    global level, tries, max_number, name

    if level == 1:
        print( tcolors.HEADER + "So," + name + " I wish to play a game with you." )

    print( tcolors.OKGREEN + "\n--- LEVEL " + str(level) + " ---" )

    print( tcolors.HEADER + "The rules are following:\nI'm gonna make a number between 1 and " + str(max_number) + "\nYou will have up to " + str(tries) + " tries to guess it" )

    print( tcolors.OKGREEN + "---" )

def make_a_number():
    global level, tries, max_number, name

    secret_number = random.randint(1, max_number)

    print( tcolors.HEADER + "Now I'm ready! You will never guess it right, ha!" )

    return secret_number

def guess_a_number( secret_number ):
    global level, tries, max_number, name

    message = tcolors.HEADER + "What's the number? " + tcolors.WARNING + "[" + str(tries) + " tries left] " + tcolors.HEADER + "[1-" + str(max_number) + ", q]: " + tcolors.ENDC

    guess = raw_input( message )
    if guess == 'q':
        game_over()

    guess = int(guess)

    if guess != secret_number:
        print(tcolors.FAIL + "Wrong! ")
        tries -= 1
        if tries == 0:
            print( tcolors.FAIL + "You lost!" )
            return False
        else:
            if guess < secret_number:
                print( tcolors.OKBLUE + "My number is greater" )
            else:
                print( tcolors.OKBLUE + "My number is less" )
            return guess_a_number( secret_number )
    else:
        print( tcolors.OKGREEN + "Agrrh! That's right. Welcome to the next level. Now I will try harder." )
        return True

def game():
    global level, tries, max_number, name

    max_number = 10 * level ** 2
    tries = int( max_number / level ** 1.5 )
    if tries >= max_number:
        tries = int(max_number * 0.7)

    if( level == 1 ):
        get_name()

    while tries > 0:
        show_rules()
        secret_number = make_a_number()
        result = guess_a_number( secret_number )
        if result == True:
            level += 1
            game()
        else:
            game_over()
            return True

def game_over():
    global level, tries, max_number, name

    print( tcolors.OKGREEN + "\n--- Game over, " + name + "! ---" )
    print( tcolors.WARNING + "Your zen level was " + str(level) )
    print( tcolors.OKGREEN + "---" )

    # reset color before exit
    print( tcolors.ENDC )
    quit()


name = None
level = 1
max_number = 10
tries = 5

game()