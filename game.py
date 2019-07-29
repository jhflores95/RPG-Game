# RPG Game
# Jorge Flores Garza

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

## Player setup ##
class player:
  def __init__(self):
    self.name = ''
    self.hp = 0
    self.mp = 0
    self.status_effects = []
    self.location = 'start'
myPlayer = player()

## Title Screen ##
def title_screen_selections():
  option = input("> ")
  if option.lower() == ("play"):
    start_game()
  elif option.lower() == ("help"):
    help_menu()
  elif option.lower() == ("quit"):
    sys.exit()
  while option.lower() not in ['play', 'help', 'quit']:
    print ("Please enter a valid command.")
    option = input("> ")
    if option.lower() == ("play"):
      start_game()
    elif option.lower() == ("help"):
      help_menu()
    elif option.lower() == ("quit"):
      sys.exit()
  
def title_screen():
  os.system('clear')    # clear command prompt
  print('############################')
  print('#   Welcome to the game!   #')
  print('############################')
  print('          - Play -          ')
  print('          - Help -          ')
  print('          - Quit -          ')
  title_screen_selections()

def help_menu():
  print('############################')
  print('#   Welcome to the game!   #')
  print('############################')
  print('- Use left, right, up, down to move.')
  print('- Type & enter your commands to use them.')
  print('- Use "look" to inspect something.')
  print('- Good luck and have fun!')
  title_screen_selections()

# MAP #
"""
 a1 a2... 
-------------
|  |  |  |  | 
-------------
|  | X|  |  | 
------------- 
|  |  |  |  | c4...
-------------
|  |  |  |  | d4
-------------
"""

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
RIGHT = 'right', 'east'
LEFT = 'left', 'west'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False
                 'b1': False, 'b2': False, 'b3': False, 'b4': False
                 'c1': False, 'c2': False, 'c3': False, 'c4': False
                 'd1': False, 'd2': False, 'd3': False, 'd4': False               
                }

zonemap = {
    'a1': {
        ZONENAME: "Abandonded Watchtower",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b1',
        RIGHT = 'a2',
        LEFT = '',
    },
    'a2': {
        ZONENAME: "Beach",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b2',
        RIGHT = 'a3', 
        LEFT = 'a1',
    },
    'a3': {
        ZONENAME: "Dirt Road",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b3',
        RIGHT = 'a4',
        LEFT = 'a2',
    },
    'a4': {
        ZONENAME: "Cliff",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = '',
        DOWN = 'b4',
        RIGHT = '',
        LEFT = 'a3',
    },
    'b1': {
        ZONENAME: "Town Market",
        DESCRIPTION = 'description',
        EXAMINATION = 'examine',
        SOLVED = False,
        UP = 'a1', 
        DOWN = 'c1',
        RIGHT = 'b2'
        LEFT = '',
    },
    'b2': {
        ZONENAME: 'Home'
        DESCRIPTION = 'This is your home!'
        EXAMINATION = 'Some of the furniture is old... I ought to look into refurbishing.'
        SOLVED = False
        UP = 'a2',
        DOWN = 'c2',
        RIGHT = 'b3',
        LEFT = 'b1',
    },
    'b3': {
        ZONENAME: 'Forester Square',
        DESCRIPTION = 'Large town square filled with all kinds of specimens from eager salesmen to shameless politicians.',
        EXAMINATION = 'Salesmen cry sales and offers into the air around you. You see an impassioned man at the edge of the square, speaking to a curious crowd.',
        SOLVED = False,
        UP = 'a2',
        DOWN = 'c2',
        RIGHT = 'b3',
        LEFT = 'b1',
    },
    'b4': {
        ZONENAME: 'City Gates',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED = False,
        UP = 'a4',
        DOWN = 'c4',
        RIGHT = '',
        LEFT = 'b3',
    },

}

## Game Interactivity ##
def print_location():
  print('\n' + ('#' * (4 + len(myPlayer.location))))
  print('# ' + myPlayer.location.upper() + ' #')
  print('# ' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
  print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print('\n' + '==================================')
    print('What would you like to do?')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
      print('Unknown action, try again.\n')
      action = input('> ')
    if action.lower() == 'quit':
      sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
      player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
      player_examine(action.lower())




## Game Functionality ##
def start_game():
