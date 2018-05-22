# Dragon Realm
# Based on Example from Invent Your Own Computer Games in Python
# Coded By Whitney King

import random
import time

def displayIntro():
    print('''You awaken in a mysterious land overun by dragons. In front of 
    you, lie the entrances to two dark caves. You can sense both a forboding 
    energy, as well as a peaceful one, but from which direction each is coming 
    it is not clear. Your fate will be determined by which cave entrance you 
    choose...''')
    print()
    print('''Pick wisely, adventurer, for in one cave, dwells a dragon fierce 
    and hungry, and in the other a dragon generous and wise. ''')
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave shall you enter (1 or 2)?')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach cave ' + chosenCave + '...')
    time.sleep(2)
    print('A large dragon emerges from the shadows!')
    print('''A flash of white appears, his fangs catching the light as he opens his 
    jaws...''')
    print()
    time.sleep(3)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('''And greets you warmly! \'Hello small thing! Come inside, come 
        inside, you never what kind of rapscallion you might encounter along 
        the way out there! Quickly, now, quickly!''')
        print()
        print('''What are you anyways perhaps a worm or a poppycock? Nevermind, 
        nevermind... anyways do come in and share in my numinous treasure, and 
        gaze upon my eternal flame of prosperity while I enrich your mind with 
        great wisdom!''')
        print()
        print()
        print()
    else:
        print('''You\'ve chosen poorly! Without blinking, the dragon snaps you up 
        in one bite! You use what little energy you have to beg the Gods to spare 
        you a quick and merciful death, but it is not to be so!''')
        print()
        print(''' With each contraction of the dragon's throat, the bones in your 
        body break, puncturing your internal organs. Passing through the dragons
        firey hot glands makes your skin bubble and burst from the blue flames 
        and cold heat, causing your flesh to curl and melt off your bones.''')
        print()
        print('The dragon softly whispers "Mmmm, bacon."')
        print()
        print()
        print()

playAgain = 'yes'


# Game Loop Begins


while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()