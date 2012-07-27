#its an adventure game with zombies.
#Option A, leads to scenario A with options of its own.

from random import randint
from sys import exit

class Player(object):

    def __init__(self):
	#player carries fatigue based on choices made, changes outcome of other choices
    #or presents new choices all together. Haven't really decided
        self.fatigue = 0

    def fatinc(self, value):
        #increments fatigue by the value so I dont have to explicitly say "fat += x"
        self.fatigue += value
        print self.fatigue
        
	
    def death(self):
		#obviously the player can die, and these are some death messages.
        taunt = ["The last thing you hear is the oddly satisfying crunch as one of them bites through your trachea.",
		         "The taste of metal fills your mouth as your screams turn to mad gurgling. The end comes too slow.",
                 "As you see them ripping flesh from your bones, you scream.  Not because of the pain, but because there is nothing else you can do.",
                 "As the pain rips the voice from your lungs, your only comfort is that there will not be enough left of you to rise again."
				]
        print "\n" + "-"*40 + "\n" 
        return taunt[randint(0,len(taunt)-1)] + " You have died. Game Over."
        exit()
		

class Game(object):

    def __init__(self, start):
        self.start = start
        self.player = Player()
        self.doom = 0
        
    def play(self):
        next_scene = self.start
        #ask user if they want to play
        print "Shall we begin?"
        answer = raw_input("> ")
        if answer == "yes":
            answer = True
        else:
            answer = False
        #this loop should continuously run the next 
        #function unless an 'exit()' is called
        while answer:
            print "-"*40
            scene = getattr(self, next_scene)
            next_scene = scene()
    
    def anyKey(self):
        raw_input("\nPress Enter to Continue...\n")
    
    def textPrint(self, text, newline = 0):
        #prints out a block of text and caps it to X number of chars per line.
		#Words that go past the char limit start at the next line
        chars = list(text)
        for char in chars:
            line = []
            while len(chars) > 0:
                line[len(line):] = [chars.pop(0)]
                if line[len(line)-1] == " " and len(line) >= 60:
                    break
            print "".join(line)
        while newline > 0:
            print "\n"
            newline -= 1

            
class DizzyStreet(Game):
    
    def theStreet(self):
        self.doom = 1
        self.player.fatinc(40)
        
        self.textPrint("You wake to the sound of a distant shriek and a throbbing headache "+ 
                       "that starts from the base of your skull to the bridge of your nose. "+
                       "Your ears feels muffled, yet you can definitely hear them ringing. "+
                       "A yellow light pulses at you not far from where you lie. As your "+
                       "vision falls into focus, you see it is the rear taillight of a car. ")
        print "\n"               
        self.textPrint("Things are very wrong. You grab your bearings and slowly work your "+
                       "way up to your feet. As you stand, you take note of your surroundings. "+
                       "Your back is to a brick wall of what appears to be the front of an "+
                       "old apartment building. To your left, there is a narrow alley between "+
                       "the apartment building and the next building over. The car you saw earlier "+
                       "has crashed into the corner of the building to your left. Both the "+
                       "driver and passenger doors are open and no one looks to be inside."
                       )
        print "\n"               
        self.textPrint("Jugding by the mix of small storefronts and apartments across the "+
                       "street, you know you are in the city. Hmm... In fact, you feel "+
                       "like you've been to this neighborhood before. Often. As if it wer-")
        self.anyKey()
        self.textPrint("Pain takes you. As you try to remember, all you get is throbbing pain. "+
                       "It looks like deep thought is not going to be an asset to you any time "+
                       "soon. You shake your head and look further down the street. "+
                       "There are a couple other cars parked along the curb, and beyond "+
                       "this one crashed car, everything else seems to be orderly.")
        print "\n"
        self.textPrint("But then it finally hits you. "+
                       "There is no one outside. With the Sun high in the sky, it couldn't be past "+
                       "mid-afternoon. It's impossible for the streets to be this empty. "+
                       "In fact, there aren't even any cars driving by, and "+
                       "you do not see a single customer in any of the store windows. Something "+
                       "is definitely wrong. A feeling of dread "+
                       "begins to bubble up.")
        print "\n"
        self.textPrint("As you try to work out the situation, you hear the sound of glass shattering "+
                       "nearby. You think you also hear someone groan, but you aren't sure. What now?")
        print "\n"               
        self.textPrint("1. Investigate the sounds. Maybe it's someone with answers.")
        self.textPrint("2. Stay and wait. My legs are still shaky.")
        self.textPrint("3. Check the car. There's bound to be some clue to the situation.")
        choice = raw_input("> ")
        if choice == '1':
            return 'theFirst'
        elif choice == '2':
            self.player.fatinc(-5)
            return 'theStreet2'
        elif choice == '3':
            print choice
            return 'theCrashedCar'
        else:
            self.textPrint("You take a few aimless steps out into the street, and feel weak you "+
                           "are. You wobble back against the wall.")
            return 'theStreet2'
            
        self.textPrint(self.player.death())
        exit()

    def theFirst(self):
        self.doom += 1
        self.textPrint("You walk towards the other corner of the apartment building, past the "+
                       "door. Or at least you try. Your balance is definitely off, and there "+
                       "is a humming dizziness that makes it difficult to walk upright. With one "+
                       "hand on the wall as a guide, you make your way down the sidewalk.",1)

        self.textPrint("Just before you make it around the corner, you hear the sounds of glass "+
                       "crunching and feet shuffling. You turn the corner slowly to face another "+
                       "narrow alley, one with a chain link fence blocking off the other end, "+
                       "perhaps 50 to 60 feet down from you are. And next to the fence, you see"+
                       "a short man facing away from you, standing next to some trash, with pieces of "
                       "glass scattered around him. What now?",1)
        self.funny = True
        self.textPrint("1. Call out to him. It's time to get answers.")
        self.textPrint("2. Head over to him.")
        self.textPrint("3. Keep going down the sidewalk. This guy gives you weird vibes.")
        if self.funny:
            self.textPrint("4. Start shuffling. Everyday I'm shuffling.")
        choice = raw_input("> ")
        if choice == '1':
            self.textPrint("Option one")
        if choice == '2':
            self.textPrint("Option two")
        if choice == '3':
            self.textPrint("Wait what?")
            self.funny = false
        exit()
        

    def theCrashedCar(self):
        print "boobs wat"
        exit()
        self.textPrint(self.player.death())
        
     
    def theStreet2(self):
        print "Still here."
        
        exit()
        
        
new_game = DizzyStreet('theStreet')
new_game.play()

















