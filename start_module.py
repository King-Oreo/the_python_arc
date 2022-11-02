
def start(floor, level, dicer, enemies):
  print("""
Floor {0} Lv {1} {2}
There are {3} enemies remaining on this floor
You can can move on (Advance), 
look at your items (Items), 
look at your moves (Moves),
see what your moves do (Info),
check your backpack (Backpack),
clear your screen and check your stats (Clear)
or try to get to the next floor (Next floor).
(btw you can just type in the first letter of all the words)""".format(floor, level, dicer, enemies))
