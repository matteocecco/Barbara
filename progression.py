import tavern
import constructors
import sys


def trade():
    pass


def text_break():
    stop = raw_input()
    if stop == "exit":
        sys.exit()
    return stop

while True:
    player_name = raw_input("\tHello, stranger! Do you remember what your name is?:\t")
    print("\tSadly, that is the only thing you remember\n")
    text_break()
    print("\tYou wake up in an empty alley, with nothing but your clothes on. You don't know where you are\n")
    text_break()
    print("\tYou see a tavern on your left, and the town's little marketplace on your right. You head for the tavern.")
    text_break()
    
    tavern_dialogue = constructors.dialogue(tavern.first_questions, tavern.first_answers)
    tavern_continuation = constructors.continued_dialogue(tavern_dialogue, tavern.second_questions, tavern.second_answers)
    print tavern_continuation
    print("You see two man quietly drinking something. In the far corner, a woman is sitting on a man's lap")
    choice = constructors.player_choice(tavern.interaction_decision, tavern.interaction_input)
    conversation = 0
    if choice == "1":
        conversation = constructors.continued_dialogue(tavern_continuation, tavern.men_questions, tavern.men_answers)
    elif choice == "2":
        conversation = constructors.continued_dialogue(tavern_continuation, tavern.woman_questions, tavern.woman_answers)

    trade()
    
    print("\t")
    end = raw_input()
