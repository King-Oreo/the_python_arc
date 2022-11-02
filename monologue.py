import time
from sys import stdout
import os

def words(text="""So… you’re dead.

That’s kinda sad isn’t it?

Didn’t you have stuff to do,

people to see,

places to be?

Wouldn’t you like to get back to that?

Whatever you did with your life before you were here?

Bad news is, you’re in hell.

The big man upstairs might’ve let you go if you really wanted to.

Here, you’ll have no such luck.

The thing is, my boss, the big one down here, he has a soft spot for one thing…

Gambling.

I can give you a few die (plural of dice, i mean), and you can try to get out of here with them.

Convince the big guy you’re not worth keeping here, by beating him in a game of chance.

But everyone, and everything had the same idea as i did.

Everyone wants out.

Some people, might want to help you out of here.

But…

Most people wanna get out of here as badly as you, and they’ll kill to do it.

All 5 levels of this place have rulers that will murder you to prove their dominance.

You’ll come straight back here after you die, no matter what.

No one has ever made it out of here.

Ever.

So you have an ultimatum here.

Leave now.

Or…

Fight, for the rest of your existence, for the rest of eternity, for a fleeting, infinitesimal chance of escape. 

It’s up to you to decide."""):
  for char in text:
    if char == "\n":
      input("\n")
      os.system('clear')
    else:
      stdout.write(char)
      stdout.flush()
      time.sleep(0.05)
  input("\n")
  os.system('clear')