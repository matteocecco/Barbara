#import the various modules needed
import tavern                                                                                                               
import constructors
import sys

#text break so the console doesn't get flooded with too much text at once. Also, allow exit whenever you want
def text_break():
    stop = raw_input()
    if stop == "exit":
        sys.exit()
    return stop
    
#idk why this infinite loop, guess I had an idea. Or maybe to try different things without closing and reopening everytime
while True:
    
    #player name, why not. Will be needed later when Player class is added
    player_name = raw_input("\tHello, stranger! Do you remember what your name is?:\t")
    print("\tSadly, that is the only thing you remember\n")
   
    #ye, various text breaks
    text_break()
    print("\tYou wake up in an empty alley, with nothing but your clothes on. You don't know where you are\n")
    text_break()
    print("\tYou see a tavern on your left, and the town's little marketplace on your right. You head for the tavern.")
    text_break()
    
    #constructors.dialogue() means that the dialogue function is imported from another module (constructors.py in this case
    tavern_dialogue = constructors.dialogue(tavern.first_questions, tavern.first_answers)
    
    #more complicated dialogue
    tavern_continuation = constructors.continued_dialogue(tavern_dialogue, tavern.second_questions, tavern.second_answers)
    
    #let's carry on with text, shall we?
    print("\tYou see two men quietly drinking something. In the far corner, a woman is sitting on a man's lap")
    
    #oh, a wild player_choice appears! Forgot about it
    choice = constructors.player_choice(tavern.interaction_decision, tavern.interaction_input)
    
    #yeah that's how functions work. Save a returned value in a variable with any name and mess with it later on
    if choice == "1":
        #now, do we go to the two men
        conversation = constructors.dialogue(tavern.men_questions, tavern.men_answers)
    elif choice == "2":
        #or to the woman?
        conversation = constructors.dialogue(tavern.woman_questions, tavern.woman_answers)
    
    print("\t")
    end = raw_input()
