import random
import monologue
from start_module import start
from attack_module import attack
import os

def floorChange(floor, enemies, num):
    if floor == []:
      monologue.words("You have beaten everyone in this arena. Upwards and onwards")
      return num + 1
    monologue.words("There are still" +str(len(floor))+ "enemies left")
    return num
 
def items(itemList):
    print("You have:")
    print((*itemList), sep = ", ")
 
def moves(moveList):
    print("Your moves are: ")
    print((*moveList), sep = ", ")

def roll(timesRolled, dices, diceRolled):
  dices["dice%s" % (timesRolled + 1)] = random.randint(1,6)
  diceDisplay = dices["dice%s" % (timesRolled + 1)]
  print("You rolled a ",diceDisplay,"\n")
  diceRolled += 1
  return diceRolled

def moveInfo(moveList, moveDict):
  moves(moveList)
  moveQuery = "placeholder"
  while moveQuery.title() not in moveList:
    moveQuery = input("Which move do you want to learn about: ")
  a = attack(moveQuery, 1, moveDict)
  if a.status ==  "":
    a.status = "no"
  print(f"{a.name} deals {a.dmg} damage (times dice roll), with a\n"
  +str(a.hitChance)+"percent chance of hitting, and gives""",a.status,"status")

def clearScreen(floor, level, dicer, enemies):
  os.system('clear')
  start(floor, level, dicer, enemies)


