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
        raw_input("\nPress Enter\n")
    
    def textPrint(self, text):
        #prints out a block of text and caps it to X number of chars per line.
		#Words that go past the char limit start at the next line
        #print "\n"
        chars = list(text)
        for char in chars:
            line = []
            while len(chars) > 0:
                line[len(line):] = [chars.pop(0)]
                if line[len(line)-1] == " " and len(line) >= 60:
                    break
            print "".join(line)

            
class TheDarkApartment(Game):
    
    def theStreet(self):
        self.doom = 3
        self.player.fatinc(25)
        print self.player.fatigue
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
                       "driver's and passenger door are open and no one looks to be inside."
                       )
        self.anyKey()
        self.textPrint("Jugding by the mix of small store fronts and apartments across the "+
                       "the street, you know you are in the city. Hmm... In fact, you feel "+
                       "like you've been to this neighborhood before. Often. As if it wer-")
        print "\n"
        self.textPrint("Pain takes you. As you try to remember, all you get is throbbing pain. "+
                       "It looks like deep thinking is not going to be an asset to you any time "+
                       "soon. There are a couple other cars parked along the street, and beyond "+
                       "this one crashed car, everything else appears to be orderly.")
        print "\n"
        self.textPrint("And then it "+
                       "hits. There is no one outside. In fact, there are no cars driving by, and "+
                       "you can not see customers in any of the store windows. A feeling of dread "+
                       "begins to bubble up.")
        print "\n"
        self.textPrint("")
        
        choice = raw_input("> ")
        self.textPrint(self.player.death())
        exit()
 
new_game = TheDarkApartment('theStreet')
new_game.play()

















