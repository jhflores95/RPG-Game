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
  print('# Welcome to the RPG Game! #')
  print('############################')
  print('          - Play -          ')
  print('          - Help -          ')
  print('          - Quit -          ')
  title_screen_selections()

def help_menu():
  print('############################')
  print('# Welcome to the RPG Game! #')
  print('############################')
  print('- Use left, right, up, down to move')
  print('- Type your commands to do them')
  print('- Use "look" to inspect something')
  print('- Good luck and have fun!')
  title_screen_selections()

## Game Functionality ##
def start_game():


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
        ZONENAME: "Watchtower",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '',
        DOWN = 'b1',
        RIGHT = 'a2',
        LEFT = '',
    },
    'a2': {
        ZONENAME: "Beach",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '',
        DOWN = 'b2',
        RIGHT = 'a3', 
        LEFT = 'a1',
    },
    'a3': {
        ZONENAME: "Dirt Road",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '',
        DOWN = 'b3',
        RIGHT = 'a4',
        LEFT = 'a2',
    },
    'a4': {
        ZONENAME: "Cliff",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = '',
        DOWN = 'b4',
        RIGHT = '',
        LEFT = 'a3',
    },
    'b1': {
        ZONENAME: "Town Market",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
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

          }


