def attack(fightMove, fightNumber, moveDict, attacksUsed=0):
    if attacksUsed == 0:
      displayMove = moveDict[fightMove.title()]
      return displayMove
    else:
      attacksUsed["attackMove%s" % (fightNumber)] = moveDict[fightMove.title()]
      return(attacksUsed["attackMove%s" % (fightNumber)])
