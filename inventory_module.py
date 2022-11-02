import random
from short_funcs_module import moves

def backpackDisplay(backpack, moveList, moveDict):
  if backpack[0] == "":
    backpack[0] = "Nothing"
  if backpack[0] == "Nothing" and len(backpack) > 1:
    backpack.pop(0)
  print("In your backpack you have: ")
  print((*backpack), sep = ", ")

  

  soupCheck = False
  while not soupCheck:
    soup = input("""
What would you like to do in your backpack?
You can swap an item from here to your inventory (Swap),
or leave the backpack (Leave): """).title()
    if soup == "Swap" or soup == "s":
      if backpack[0] != "Nothing":
        souperCheck = False
        while not souperCheck:
          souper = input("What item would you like to put into the inventory: ").title()
          if souper in moveList:
            soupestCheck = False
            while not soupestCheck:
              moves(moveList)
              print("")
              soupest = input("What item would you like to put in the backpack").title()
              if soupest in backpack:
                moveList.remove(souper)
                moveList.append(soupest)
                backpack.remove(soupest)
                backpack.append(souper)
  
      else:
        print("Your backpack is empty... ")
        soupCheck = True
    elif soup == "Leave" or soup == "l":
      soupCheck = True
    else:
      soup = input("It's one or the other bud, though i'd highly advise the latter.\n(Swap)\n(LEAVE): ").lower()[0]


def shopCalc(ID):
    itemName = ID.name
    itemDamage = ID.dmg
    itemStatus = ID.status
    itemPriceVariance = random.randint(-10,10)
    if itemDamage == 0:
      itemDamageCalc = 6
    else:
      itemDamageCalc = itemDamage
    itemPrice = (itemDamageCalc * 5) + itemPriceVariance
    if itemStatus == "":
      itemStatus = "no"
    statsList = [itemName, itemPrice, itemDamage, itemStatus,]
    return statsList

def shop(moveDict, health, maxHealth, backpack, coins):
    moveDictList = list(moveDict.items())
    item1 = random.choice(moveDictList)
    item2 = random.choice(moveDictList)
    itemID1 = item1[1]
    itemID2 = item2[1]
    stats1 = shopCalc(itemID1)
    stats2 = shopCalc(itemID2)
    
    healthBoost = random.randint(10,40)
    healthPrice = healthBoost + random.randint(-10,10)
    print("Howdy! This is my quaint lil' shop\nFeel free to take anything you like")
    print(stats1[0],"""-""",stats1[1],"""coins - Deals""",stats1[2],"""dmg, inflicts""",stats1[3],"""status""")
    print(stats2[0],"""-""",stats2[1],"""coins - Deals""",stats2[2],"""dmg, inflicts""",stats2[3],"""status""")
    print("Health pack -",healthPrice,"coins - Heals",healthBoost,"health")

    print(f"You have {coins} coins")  

    itemChoice = input("""You can buy the first move (1),
the second move (2),
the Health Pack  (3),
or get outta here (Leave)
Dont just stand 'round ere, make a choice!: """)
    choiceValid = 0
    while choiceValid != 1:
        choiceValid = 1
        if itemChoice == "1":
          if coins >= stats1[1]:
            print("""Move added to backpack.
  You can access it with the (Backpack) command.""")
            backpack.append(stats1[0])
            coins -= stats1[1]
          else:
            choiceValid = 0
            print("I aint a charity! If you dont have the cash, you wont get it!")
            
        elif itemChoice == "2":
          if coins >= stats2[1]:
            print("""Move added to backpack.
  You can access it with the (Backpack) command.""")
            backpack.append(stats2[0])
            coins -= stats2[1]
          else:
            choiceValid = 0
            print("I aint a charity! If you dont have the cash, you wont get it!")
            
        elif itemChoice == "3":
          if coins >= healthPrice:
            health += healthBoost
            print("You should have",healthBoost,"more health now")
            if health > maxHealth:
              health = maxHealth
            print("You now have",health,"health")
            coins -= healthPrice
          else:
            choiceValid = 0
            print("I aint a charity! If you dont have the cash, you wont get it!")
            
        elif itemChoice.title() == "Leave" or itemChoice == "l":
          print("Guess i'll be seein' ya\nLater!")
        else:
          choiceValid = 0
          itemChoice = input("Dont 'ave that for ya, i'm afraid\nPick somethin' else: ")