

import time
import os
import random
import gc
from stolen_code import printf
from attack_module import attack
from inventory_module import shop, shopCalc, backpackDisplay
from short_funcs_module import items, roll, floorChange, moves, moveInfo, clearScreen
from start_module import start
from dataclasses import dataclass
import monologue

""
for each in reversed(range(5)):
  letter = random.choice(["w", "s", "d"])
  num1 = time.time()
  print(f"Press {letter} now", end="")
  guess = input(":")
  num2 = time.time()
  timer = num2 - num1
  print(timer)
  if timer > each or guess != letter:
    print("you failed")
  else:
    print("you got it")



#RPreeeeeeee

#############
#To-do list
#Un hard code damage values for enemies
#Add threads and run code whilst input is being taken
#program enemies dropping items/ weapons
#############


##if floor == 69:
##    floorName = bartenderFight
##
##if floorName == bartenderFight:
##    print("""Hahaahah, so youre approaching me
##          Fear my might little one, and I
##          just might make your death... less painful
##          **ALMIGHTY BARTENDER HAS BEEN AWAKENED**""")

opening = input("Have you played this game before: ")
if opening.lower()[0] != "y":
  monologue.words()

class placeholder:
  def __init__(self, placeholder):
    self.placeholder = placeholder

class Item:
  def __init__(self, name, dicerEffect, battleItem, diceEffect):
    self.name = name
    self.dicerEffect = dicerEffect
    self.battleItem = battleItem
    self.diceEffect = diceEffect 
  

pI = Item("placeholder", "none", False, 1)
#health related items
i1 = Item("Health Potion", "Heal", False, 1)
i2 = Item("Smoke Bomb", "", True, 1)
i3 = Item("Lasso", "", True, 1)
i4 = Item("Elixir", "", True, 2)
i5 = Item("Calculator", "", True, 1)
i6 = Item("Stash", "", True, 1)


@dataclass
class Move:
  name : str
  dmg : int
  status : str
  hitChance : int
  attackCheck : bool = 0
  totalDice : int = 0
  


#fight() related
p = Move("placeholder", 0, "", 0)
#cowboy moves
amC1 = Move("Quick Draw", (random.randrange(2,14,2)), "", 80)
amC2 = Move("Whiplash", 5, "Tied up", 33)
amC3 = Move("Deadeye", 5, "", 100)
amC4 = Move("Glare", 0, "Fear", 75)
#ninja moves
amN1 = Move("Dash Attack", 8, "", 75)
amN2 = Move("Sword Whirl", (random.randrange(2,8,2)), "", 80)
amN3 = Move("Poison Cloud", 3, "Poison", 50)
amN4 = Move("Misdirection", 0, "Dazed", 75)
#wizard moves
amW1 = Move("Whirlwind", 6, "Dazed", 50)
amW2 = Move("Flamethrower", 4, "Burn", 50)
amW3 = Move("Earthquake", 6, "", 75)
amW4 = Move("Waterfall", 4, "Wet", 50)
#robot moves
amR1 = Move("Charge", 0, "", 0)
amR2 = Move("Overclock", 0, "", 0)
amR3 = Move("Laserbeam", 0, "", 0)
amR4 = Move("Electrocute", (random.randint(1,4)), "Shock", 66)
#thief moves
amT1 = Move("Sucker Punch", 0, "", 0)
amT2 = Move("Stab", 0, "", 0)

#enemy moves
em0 = Move("Struggle", 0, "", 0)
em1 = Move("Punch", 10, "", 75)
em2 = Move("Whip", random.randrange(6, 16, 2), "", 75)
#em4 = Move("Arrest", 0, "Arrested", 50)
em3 = Move("Mine", 8, "", 80)
em4 = Move("Molotov Cocktail", 5, "Burn", 50)
em5 = Move("Gold Rush", random.randrange(0, 20, 2), "", 100)
em6 = Move("Misfire", 1000, "", 0)
em7 = Move("Shotgun Blast", random.randint(1,20), "", 100)
em8 = Move("Rocket Barrage", 6, "", 50)
em9 = Move("Jet Blast", 7, "", 75)
em10 = Move("Concotion", 1, "3Random", 100)
em11 = Move("Flame Breath", 10, "Burn", 75)
em12 = Move("", 10, "", 75)
em13 = Move("Punch", 10, "", 75)
em14 = Move("Punch", 10, "", 75)
em15 = Move("Punch", 10, "", 75)

@dataclass
class Enemy:
  name : str
  health : int
  move : Move

e1f1 = Enemy("Crook", 100, em1)
e2f1 = Enemy("Sheriff", 100, em2)
e3f1 = Enemy("Miner", 100, em3)
e4f1 = Enemy("Bartender", 100, em4)
e5f1 = Enemy("Gold Digger", 100, em5)
e1f2 = Enemy("Storm Trooper", 100, em6)
e2f2 = Enemy("Terminator", 100, em7)
e3f2 = Enemy("Mech", 100, em8)
e4f2 = Enemy("Jetpack Pilot", 100, em9)
e5f2 = Enemy("Mad Scientist", 100, em10)
e1f3 = Enemy("Dragon", 100, em1)
e2f3 = Enemy("Knight", 100, em1)
e3f3 = Enemy("Archer", 100, em1)
e4f3 = Enemy("Paladin", 100, em1)
e5f3 = Enemy("Druid", 100, em1)
e1f4 = Enemy("Zeus", 100, em1)
e2f4 = Enemy("Hermes", 100, em1)
e3f4 = Enemy("Aphrodite", 100, em1)
e4f4 = Enemy("Poseidon", 100, em1)
e5f4 = Enemy("Ares", 100, em1)
e1f5 = Enemy("Satan", 10000, [obj for obj in gc.get_objects() if isinstance(obj, Move)])

enemyRef = [e1f1, e2f1, e3f1, e4f1, e5f1, e1f2, e2f2, e3f2, e4f2, e5f2, e1f3, e2f3, e3f3, e4f3, e5f3, e1f4, e2f4, e3f4, e4f4, e5f4, e1f5]


moveDict = {
"Quick Draw" : amC1, "Whiplash" : amC2, "Deadeye" : amC3, "Glare" : amC4,
"Dash Attack" : amN1, "Sword Whirl" : amN2, "Misdirection" : amN3, "Poison Cloud" : amN4,
"Whirlwind" : amW1, "Flamethrower" : amW2,  "Earthquake" : amW3,  "Waterfall" : amW4,  
"Charge" : amR1, "Overclock" : amR1, "Laserbeam" : amR1, "Electrocute" : amR1,
"Sucker Punch" : amT1, "Stab" : amT2,
"Struggle" : em1, "Punch" : em2, "placeholder" : p
}

attacksUsed = {"attackMove1" : p, "attackMove2" : p, "attackMove3" : p}

itemDict = {
"Health Potion" : i1,
"Smoke Bomb" : i2,
"Lasso" : i3,
"Elixir" : i4,
"Calculator" : i5,
"Stash" : i6,
"placeholder" : pI
}

floors = [[e1f1, e2f1, e3f1, e4f1, e5f1], [e1f2, e2f2, e3f2, e4f2, e5f2], [e1f3, e2f3, e3f3, e4f3, e5f3], [e1f4, e2f4, e3f4, e4f4, e5f4], [e1f5]]
specialMoveMeter = 0

#def fightInfo():
  #global dices, moveDict, level, dicer, exp, floor, battlesFought, enemiesDefeated, hitCheck, enemies, dmgMultiplier, moveList, itemList, diceRolled, randomizer, activeEffectDuration, activeEffect, statusCheck, attacker, attackerHealth, specialMoveMeter, lastMove, moveFatigue, fatigueCooldown, total, maxHealth, health, attackMove1, attackMove2, attackMove3, statsList, deaths
  #return dices, moveDict, level, dicer, exp, floor, battlesFought, enemiesDefeated, hitCheck, enemies, dmgMultiplier, moveList, itemList, diceRolled, randomizer, activeEffectDuration, activeEffect, statusCheck, attacker, attackerHealth, specialMoveMeter, lastMove, moveFatigue, fatigueCooldown, total, maxHealth, health, attackMove1, attackMove2, attackMove3, statsList, deaths

def useItem(itemDict, itemList, inBattle=False):
  global health
  global maxHealth
  items(itemList)
  usedItem = "placeholder"
  while usedItem not in itemList:
    usedItem = input("What item would you like to use: ").title()
  if usedItem == "Health Potion":
    health = maxHealth
    print("Your health has been refilled to", health)
  if usedItem == "Smokebomb" and inBattle:
    return 0
  if usedItem == "Lasso" and inBattle:
    return 1
  if usedItem == "Elixir" and inBattle:
    return 2
  if usedItem == "Calculator" and inBattle:
    return 3
  if usedItem == "Stash" and inBattle:
    return 4
  
  

def fight(deaths):
    global dices, moveDict, level, dicer, exp, floor, battlesFought, enemiesDefeated, hitCheck, enemies, dmgMultiplier, moveList, itemList, diceRolled, randomizer, activeEffectDuration, activeEffect, statusCheck, attacker, attackerHealth, specialMoveMeter, lastMove, moveFatigue, fatigueCooldown, total, maxHealth, health, attackMove1, attackMove2, attackMove3, statsList
    global moveDict, move1, move2, move3, hitCheck, movesUsed, statusUsed, activeEffectDuration, statusCheck, activeEffect, dmgMultiplier, lastMove, moveFatigue, fatigueCooldown, health, attackerHealth, attacker, impendingDoom, turns, floors, attackerRef
    maxRolls = level + 1
    moveRolls = 0
    whatever = False
    statusUsed = False
    statusCheck = False
    moveFatigue = 1
    fatigueCooldown = 0
    lastMove = "placeholder"
    activeEffectDuration = 0
    activeEffect = "nothing"
    randomizer = random.randint(0,4)
    ##enemiesf1 = [e1f1, e2f1, e3f1, e4f1, e5f1] #wild west town
    ##enemiesf2 = [e1f2, e2f2, e3f2, e4f2, e5f2] #sci fi futuristic
    ##enemiesf3 = [e1f3, e2f3, e3f3, e4f3, e5f3] #mythical, wizard floor
    ##enemiesf4 = [e1f4, e2f4, e3f4, e4f4, e5f4] #olympus
    ##enemiesf5 = [e1f5] #Arena
    ##bartenderFight = ["Bartender the Almighty"] #Secret


    attackerRef = random.choice(floors[floor-1])
    attacker = attackerRef.name
    attackerHealth = attackerRef.health

    if floor == 1 or floor == 2 or floor == 3:
        print("""Battle start!
A""",attacker,"""blocked your way!
"""+str(attacker)+""" has""",attackerHealth,"""health
You have""",health,"""health
look at your moves (Moves),
see what your moves do (Info),
look at your items (Items),
end the turn (End Turn)
or attack (Attack)
""")
    elif floor == 4:
        print("""Battle start!"""
,attacker,"""blocked your way!
look at your moves (Moves),
see what your moves do (Info),
look at your items (Items),
or attack (Attack)
""")
    moveValid = False
    diceRolled = 0
    timesRolled = 0
    turns = 0 
    while attackerHealth > 0 and health > 0:
      endTurn = False
      diceRolled = 0
      timesRolled = 0
      movesUsed = 0
      attacks = 0
      turnRolls = maxRolls
      attacksUsed = {"attackMove1" : p, "attackMove2" : p, "attackMove3" : p}
      while not endTurn:
            if not whatever:
                battleMove = input("What will you do? (f): ")
            #runs the "roll" function to set a dice to a random value  between 1 and 6

            if battleMove.title() == "Attack" or battleMove == "a":
                fightMove = "placeholder"
                fighttCheck = False
                pMoveDict = ["1", "2", "3", "4"]
                chicketyChack = False
                if turnRolls <= 0:
                  print("You've used all of your attacks! End the turn")
                else:
                    while not chicketyChack:
                        invalidNumCheck = False
                        print("You have",turnRolls,"dice left")
                        try:
                          diceUsed = int(input("How many dice will you use on this move?: "))
                        except ValueError:
                          print("That's not a number..\n")
                          invalidNumCheck = True
                      
                        if invalidNumCheck is True:
                          pass;
                        elif diceUsed > turnRolls:
                          print("You only have",turnRolls,"left")
                        else:
                          chicketyChack = True
    
                    for each in range(diceUsed):
                          diceRolled = roll(timesRolled, dices, diceRolled)
                          turnRolls -= 1
                    while not fighttCheck:
                          moves(moveList)
                          fightMove = input("Make your move: ")
                          #checks if the move used is in your list of moves
                          if fightMove.title() in moveList or fightMove in pMoveDict:
                              attacks += 1
                              movesUsed += 1
                              moveValid = True
                              if fightMove in pMoveDict:
                                fightMove = moveList[pMoveDict.index(fightMove)]
                              attacksUsed["attackMove%s" % (attacks)] = attack(fightMove, attacks, moveDict, attacksUsed)
                              #print(vars(attacksUsed["attackMove%s" % (attacks)]))
                              #print(attacksUsed["attackMove1"].name)
                                                      
                              #print(attacksUsed["attackMove2"].name)
                                                  
                              #print(attacksUsed["attackMove3"].name)
                              if diceRolled <= maxRolls:
                                  endTurnCheckCheck = False
                                  while not endTurnCheckCheck:
                                      boop = True
                                      endTurnCheck = input("Would you like to end the turn?: ")
                                      if endTurnCheck == "Yes" or endTurnCheck == "yes":
      
                                        movehitChance = (
                                        attacksUsed["attackMove1"].hitChance +
attacksUsed["attackMove2"].hitChance +
attacksUsed["attackMove3"].hitChance
                                        ) / attacks
                                        if random.randint(1,100) <= movehitChance:
                                              hitCheck = True
                                        else:
                                              hitCheck = False
      
                                        values = dices.values()
                                        total = 0
                                        for dic in values:
                                          if dic > 0:
                                            total += dic
                                        attacksUsed["attackMove%s" % (attacks)].totalDice = total
                                        endTurn = True
                                        specialMoveMeter += 1
                                        fighttCheck = 1
                                        endTurnCheckCheck = True
                                      elif endTurnCheck == "No" or endTurnCheck == "no":                  
                                        whatever = False
                                        endTurnCheckCheck = True
                                        fighttCheck = 1
                                      else:
                                        print("""Say "yes" or "no" """)
                                        #print(attacksUsed["attackMove1"].name)
                                        #print(attacksUsed["attackMove2"].name)
                                        #print(attacksUsed["attackMove3"].name)
                                        
                              else:
                                  movehitChance = (
                                  attacksUsed["attackMove1"].hitChance +
                                  attacksUsed["attackMove2"].hitChance +
                                  attacksUsed["attackMove3"].hitChance
                                  ) / attacks
                                  if random.randint(1,100) <= movehitChance:
                                        hitCheck = True
                                  else:
                                        hitCheck = False
      
                                  values = dices.values()
                                  total = 0
                                  for dic in values:
                                    if dic > 0:
                                      total += dic
                                  attacksUsed["attackMove%s" % (attacks)].totalDice = total
                                  fighttCheck = 1
                                
                                  #print(attacksUsed["attackMove1"].name)
                                  #print(attacksUsed["attackMove2"].name)
                                  #print(attacksUsed["attackMove3"].name)
                              ''' elif attackerHealth >= 0:
                          youwonwow = 1
                          moveValid = False
                          print("You won! Yay woo") '''

            #else:
                  #battleMove = input("""You need to roll a dice to     charge your attack first
                #Type (Roll) to roll a dice: """)
                #whatever = True
            elif battleMove == "Moves" or battleMove == "moves" or battleMove == "m":
                moves(moveList)
                whatever = False
                ##elif battleMove == "Block" or battleMove == "block":
            elif battleMove == "Items" or battleMove == "items" or battleMove == "i":
                items(itemList)
                whatever = False
            elif battleMove == "Info" or battleMove == "info" or battleMove == "ii":
                moveInfo(moveList, moveDict)
                whatever = False
            elif battleMove.title() == "End Turn" or battleMove == "e":
               if attacks > 0:
                    movehitChance = (                                                      attacksUsed["attackMove1"].hitChance +
                    attacksUsed["attackMove2"].hitChance +
                    attacksUsed["attackMove3"].hitChance
                    ) / attacks
                    if random.randint(1,100) <= movehitChance:
                          hitCheck = True
                    else:
                          hitCheck = False
  
                    values = dices.values()
                    total = 0
                    for dic in values:
                      if dic > 0:
                        total += dic
                    attacksUsed["attackMove%s" % (attacks)].totalDice = total
                    endTurn = True
               else:
                 print("You haven't used an attack yet. Use one (or more), before you end the turn")
      attackMove1 = attacksUsed["attackMove1"]
      attackMove2 = attacksUsed["attackMove2"]
      attackMove3 = attacksUsed["attackMove3"]

      
      move1 = attacksUsed["attackMove1"]
      move2 = attacksUsed["attackMove2"]
      move3 = attacksUsed["attackMove3"]
      #print(move1.name,move2.name,move3.name)
      
    
      #print(attackMove1.dmg)
      
      moveDisplay()
      turns += 1
      whatever = False
    
    maxHealth = (level + 4) * 20
    health = maxHealth // 2
    enemiesDefeated += 1
    enemies -= 1
    exp += attackerHealth * 4
    coins += attackerHealth


    if exp >= 100:
      exp = 0
      dmgMultiplier += 0.2
    if attackerHealth == 0:
      print("You won!! There are",enemies,"enemies remaining")
      enemiesDefeated += 1
      enemies -= 1
      return 
    if health == 0:
      print("You were defeated. Stay strong, dont stop.")
      
      os.system('clear')
      if deaths == 0:
        time.sleep(10)
        with open("save_file_1.txt", "w", "utf-8") as writer:
          statsList[0] = deaths + 1
          deaths += 1
          writer.writeLines(statsList)
        return 
      else:
        time.sleep(5)
        with open("save_file_1.txt", "w", "utf-8") as writer:
          statsList[0] = int(deaths) + 1
          deaths = str(int(deaths + 1))
          writer.writeLines(statsList)
      return 

def moveDisplay():
    global moveDict, move1, move2, move3, hitCheck, movesUsed, statusUsed, activeEffectDuration, statusCheck, activeEffect, dmgMultiplier, lastMove, moveFatigue, fatigueCooldown, health, attackerHealth, attacker, impendingDoom, turns, attackerRef, dmgMultiplier

    if turns == 0:
      impendingDoom = 32768
    attackerMoveName = attackerRef.move.name
    attackerHitCheck = (lambda a : "hit" if a > random.randint(1,100) else "miss")(attackerRef.move.hitChance)
    attackerMoveDamage = (lambda a : a if attackerHitCheck else 0)(attackerRef.move.dmg)
    moveName1 = move1.name
    moveDamage1 = move1.dmg
    moveStatus1 = move1.status
    diceSum1 = move1.totalDice
    moveName2 = move2.name
    moveDamage2 = move2.dmg
    moveStatus2 = move2.status
    diceSum2 = move2.totalDice
    moveName3 = move3.name
    moveDamage3 = move3.dmg
    moveStatus3 = move3.status
    diceSum3 = move3.totalDice
    moveNames = "placeholder"
    statusUsed = True
    moveDamage = (moveDamage1 * diceSum1) + (moveDamage2 * diceSum2) + (moveDamage3 * diceSum3)
    moveDamage *= dmgMultiplier
    if movesUsed == 1:
      moveNames = moveName1
    elif movesUsed == 2:
      moveNames = ""+str(moveName1)+" and "+str(moveName2)+""
    elif movesUsed == 3:
      moveNames = ""+str(moveName1)+" and "+str(moveName2)+""+str(moveName3)+""
    else:
      print("Uh oh, glitch")
      moveNames = moveName1

    if lastMove == moveNames:
      moveFatigue -= 0.1
      fatigueCooldown = 3
      if moveFatigue < 0.5:
        moveFatigue = 0.5
    else:
      fatigueCooldown -= 1
    
    if fatigueCooldown <= 0:
      moveFatigue = 1

    lastMove = moveNames

    if not hitCheck:
        moveDamage = 0

    print("\n")
  
    a_dict = {"move1" : moveStatus1, "move2" : moveStatus2, "move3" : moveStatus3}
    moveStatuses = ""
    #print(statusCheck)

    statusDict = {
    "Tied up" : 1,  #stops enemy from moving next turn
    "Burn": 3, #flat damage based on lvl 
    "Poison" : 2, #percentage of enemy hp
    "Wet" : 3, #lowers accuracy
    "Fear" : 1, #enemy cant move for 2 turns, no dmg and low acc
    "Dazed" : 3, #chance of self dmg
    "Shock" : 2 } #interrupts enemy in 2 turns for 2 turns

    for i in range(movesUsed):
      ii = i + 1
      statuses = 0
      if a_dict["move%s" % str(ii)] != "" and activeEffect == "nothing" and hitCheck == True:
        moveStatuses += str(a_dict["move%s" % str(ii)])
        statuses += 1
        if statusCheck == False:
            activeEffect = a_dict["move%s" % str(ii)]
            activeEffectDuration = statusDict[a_dict["move%s" % str(ii)]]
    ''' elif a_dict["move%s" % str(ii)] != "":
        moveStatuses += str(" and" + a_dict["move%s" % str(ii)])
        statuses += 1
        someCheck = False
        if not someCheck:
          activeEffect = a_dict["move%s" % str(ii)]
          activeEffectDuration = statusDict[a_dict["move%s" % str(ii)]] '''

    if activeEffectDuration == 0 and statusUsed == True:
              statusCheck = False
              activeEffect = "nothing"
    elif activeEffectDuration == 0:
              pass;
    else:
              activeEffectDuration -= 1
      

    if moveStatuses != "":
      moveStatuses = ", inflicting " +str(moveStatuses)
    
    attackerHealth -= moveDamage
    health -= attackerMoveDamage

    if activeEffect == "Tied up":
      attackerMoveDamage = 0
      attackerMoveName = "Struggle"

    if activeEffect == "Burn":
      attackerHealth -= (level * 10)
      print(attacker,"was burned, dealing",str(level * 10),"damage")

    if activeEffect == "Poison":
      diff = attackerHealth
      attackerHealth *= 0.6
      attackerHealth = attackerHealth // 1
      print(attacker,"was poisoned, dealing",str((diff - attackerHealth) // 1),"damage")

    if activeEffect == "Wet":
      attackerHitCheck = 50

    if activeEffect == "Fear":
      attackerMoveDamage = 0
      attackerMoveName = "Petrified"

    if activeEffect == "Dazed":
      chance = random.randint(0,1)
      if chance == 1:
        attackerHealth -= (attackerMoveDamage * 0.6)
        attackerHitCheck = 0
        print(attacker,"hit themselves in their confusion")
        
    if activeEffect == "Shock":
      impendingDoom = 2
      
    impendingDoom -= 1
    if impendingDoom == 0:
      attackerMoveDamage = 0
      attackerMoveName = "Jolted"
      attackerHealth -= 20 * level
      print(attacker,"was shocked")
      




    if health < 0:
      health = 0
    if attackerHealth < 0:
      attackerHealth = 0

   ## moveStatuses = " ".join([str(item) for item in moveStatuses])

    if hitCheck:
      hitCheck = "hit"
    else:
      hitCheck = "missed"

    #print(activeEffectDuration)
    #print(activeEffect)
    #print(statusCheck)

    moveDamage *= moveFatigue

    moveDamage = moveDamage // 1
    moveDamage = int(moveDamage)
    attackerHealth = int(attackerHealth)

    print(f"You {hitCheck} {attacker} with {moveNames} for {moveDamage} dmg{moveStatuses} \n {attacker} {attackerHitCheck} you with {attackerMoveName} for {attackerMoveDamage} dmg \n")
    if moveFatigue < 0.6:
      print("You will lose effectiveness if you keep using the same move! \nTry another")
    print(f"{attacker} has {attackerHealth} health left")
    if activeEffect != "nothing":
      print(f"{attacker} has {activeEffect}")
    print("You have " + str(health)+" health left")
  
    return statusUsed

def main(deaths):
    global dices, moveDict, level, dicer, exp, floor, battlesFought, enemiesDefeated, hitCheck, enemies, dmgMultiplier, moveList, itemList, diceRolled, randomizer, activeEffectDuration, activeEffect, statusCheck, attacker, attackerHealth, specialMoveMeter, lastMove, moveFatigue, fatigueCooldown, total, maxHealth, health, attackMove1, attackMove2, attackMove3, statsList, floors
    
    printf(f"Remember, dont die \n")
    time.sleep(1)
    dicer = input("Choose your character: Wizard, Ninja, Thief, Cowboy, Robot\n(Dont pick Thief or Robot): ")
 


    dmgMultiplier = 1 + (deaths / 3)
    enemiesDefeated = 0
    impendingDoom = 0
    battles = 0
    battlesFought = 0 
    dicerCheck = 0
    while dicerCheck == 0:
        if dicer.title() == "Wizard":
            dicer = dicer.title()
            print("You chose.. Wizard. Interested in the elements, arent ya")
            dicerCheck = 1
        elif dicer.title() == "Ninja":
            dicer = dicer.title()
            print("You choose.. Ninja. Ambushing type, I guess.")
            dicerCheck = 1
        elif dicer.title() == "Thief":
            dicer = dicer.title()
            print("You choose.. Thief. Stealing your way to the top.")
            dicerCheck = 1
        elif dicer.title() == "Cowboy":
            dicer = dicer.title()
            print("You choose.. Cowboy. Gunsling it to win it, I suppose.")
            dicerCheck = 1
        elif dicer.title() == "Robot":
            dicer = dicer.title()
            print("You choose.. Robot. Rig the odds and the battles win themselves.")
            dicerCheck = 1
        else:
            dicer = input("That's not a character... yet. Try again: ")
            dicerCheck = 0

    name = input("Whats your name? Why do I ask? NO reason, no reason, dont worry. What is it?: ")
    ##if name == "Bart" or name == "bart":
    ##    print("/kill")
    ##    time.sleep(2)
    ##    print("Wait that didnt work? by the way im a......")
    ##    time.sleep(5)
    ##    print("...BARTENDER")
    ##    finalbossfight()
    
    text = input("""
(Press enter to continue dialogue)""")
    print("""
I.. actually dont care""")
    time.sleep(0.75)
    text = input("""What are you waiting for. Me? Im your narrator, not your freaking tutorial
go out and  do something!""")
    
    print("Loading next zone.")
    time.sleep(1)
    print("Loading next zone..")
    time.sleep(1)
    print("Loading next zone...")
    time.sleep(1)
    
    #fight() related
    if dicer == "Wizard":
        itemList = ["Old Staff", "Health Potion", "Elixir"] #elixr gives random buff
    elif dicer == "Ninja":
        itemList = ["Battered Blade", "Health Potion", "Smoke Bomb"] #smokebomb is free escape
    elif dicer == "Thief":
        itemList = ["Blunt Dagger", "Health Potion", "Stash"] #steals enemies last move
    elif dicer == "Cowboy":
        itemList = ["Weak Pistol", "Health Potion", "Lasso"] #stops enemy from making a move on their rturn
    elif dicer == "Robot":
        itemList = ["Heavy Wrench", "Health Potion", "Calculator"] #always roll a 6 on next attack
    
    
    if dicer == "Wizard":
        moveList = ["Flamethrower", "Waterfall", "Earthquake", "Whirlwind"] #all wizard moves add an elemental status
    elif dicer == "Ninja":
        moveList = ["Sword Whirl", "Poison Cloud", "Misdirection", "Dash Attack"] #poison adds the poison status effect, misdirection adds daze which stacked up enough turns into confuse
    elif dicer == "Thief":
        moveList = ["Sucker Punch", "Stab", ] #stab deals bleeding damage
    elif dicer == "Cowboy":
        moveList = ["Deadeye", "Glare", "Quick Draw", "Whiplash"] #glare adds fear status effect
    elif dicer == "Robot":
        moveList = ["Electrocute", "Charge", "Laserbeam", "Overclock"] #elctrocute adds shocked status effect, overclock gives higher damage but afterwards he cant move for a attackerMove = "Punch"
    dices = {
"dice1" : 0,
"dice2" : 0,
"dice3" : 0,
"dice4" : 0,
"dice5" : 0,
"dice6" : 0,
"dice7" : 0,
"dice8" : 0,
"dice9" : 0,
"dice10" : 0,
}
    

    floor = 1
    floorMultiplier = (floor / 5) + 1
    dmgMultiplier = 1
    level = 1
    coins = 50
    exp = 0
    maxHealth = 100
    health = maxHealth
    enemies = len(floors[floor-1])
    enemiesFloor = floors[floor-1]
    enemiesTotal = enemies
    hitCheck = p
    randomizer = p
    activeEffectDuration = p
    attacker = p
    attackerHealth = p
    lastMove = p
    moveFatigue = p
    fatigueCooldown = p
    total = p
    diceRolled = p
    activeEffect = p
    statusCheck = p
    attackMove1 = p
    attackMove2 = p
    attackMove3 = p

    start(floor, level, dicer, enemies)

    ##fightInfo = {"moveDict" : moveDict, "level" : level, "dicer" : dicer, "exp" : exp, "floor" : floor, "p" : p, "dices" : dices, "battlesFought" : battlesFought, "enemiesDefeated" : enemiesDefeated, "hitCheck" : hitCheck, "enemies" : enemies, "dmgMultiplier" : dmgMultiplier, "moveList" : moveList, "itemList" : itemList, "diceRolled" : diceRolled, "randomizer" : randomizer, "activeEffectDuration" : activeEffectDuration, "activeEffect" : activeEffect, "statusCheck" : statusCheck, "attacker" : attacker, "attackerHealth" : attackerHealth, "specialMoveMeter" : specialMoveMeter, "lastMove" : lastMove, "moveFatigue" : moveFatigue, "fatigueCooldown" : fatigueCooldown, "total" : total, "maxHealth" : maxHealth, "health" : health, "attackMove1" : attackMove1, "attackMove2" : attackMove2, "attackMove3" : attackMove3, "statsList" : statsList, "deaths" : deaths}
    
    backpack = [""]

    #Main battle loop
    
    finishCheck = 0
    while finishCheck == 0:
        move = input("\nWhat will you do?: ")
        if move == "Advance" or move == "advance" or move == "a":
            if enemiesDefeated != enemiesTotal:
                advanceChoices = random.randint(1,5)
                if advanceChoices == 1:
                    healNum = random.randint(20, 30)
                    health += healNum
                    if health > maxHealth:
                      health = maxHealth
                    print("You have been healed",healNum,"health and now have",health,"health")
                elif advanceChoices == 2:
                  print("You found a shop!")
                  shop(moveDict, health, maxHealth, backpack, coins)
                else:
                  fight(deaths)
                  
            else:
                print("You've found everything on this floor. Try going to the next one!")
              
        elif move.title() == "Items" or move == "i":
            items(itemList)
        elif move.title() == "Use Item" or move == "u":
            useItem(itemDict, itemList)
        elif move.title() == "Moves" or move == "m":
            moves(moveList)
        elif move.title() == "Info" or move == "ii":
            moveInfo(moveList, moveDict)
        elif move.title() == "Next Floor" or move == "n":
            floor = floorChange(enemiesFloor, enemies, floor)
        elif move.title() == "Backpack" or move == "b":
            backpackDisplay(backpack, moveList, moveDict)
        elif move.title() == "Clear" or move == "c":
          clearScreen(floor, level, dicer, enemies)
    #all chracters can block and reroll 

    #Action functions


    battlesFought = 1

    '''

    '''
main(0)
