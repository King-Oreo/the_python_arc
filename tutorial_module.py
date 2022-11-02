import time

def tutorial():
    global dicer
    text = input("Since this is your first fight, im going to need to teach you\nsome things about clobberin' enemies like me.\nI go by Dummy 'round these parts")
    print("""Battle start!
    Lv 1 Dummy blocked your way!
    What will you do?
    """)
    time.sleep(1)
    if dicer == "Cowboy":
        print("""You got a few moves on you kiddo.
        You might aswell Quick Draw right about now, since that'll
        always hit me before i can hit ya back.""")
        moveValid = False
        while not moveValid:
            tutorialMove = input("Type in the name of the move to use it! (Type \"Quick draw\")")
            if tutorialMove == "Quick Draw" or tutorialMove == "Quick draw" or tutorialMove == "quick draw":
                print("You hit Dummy with Quick Draw for 10 dmg.\nDummy hit you with Jab for 1 dmg")
                time.sleep(0.75)
                print("Nice one kid, you're a natural")
                moveValid = True
            elif tutorialMove == "Glare" or tutorialMove == "glare":
                print("You hit Dummy for 0 dmg, inflicting Fear\nDummy hit you with Jab for 1 dmg")
                time.sleep(3)
                print("""Woah kid, didnt know you could do that one. Just so ya know,
                      Fear means that my next attack is much more likely ta miss,
                      so keep that in mind""")
                moveValid = True

