import tavern
import constructors


def  innkeeper_dialogue():
    print("\tThe innkeeper greets you. He looks angry")
    

def trade():
    pass


def text_break():
    stop = raw_input()
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
    
    """print("\tYou head towards the marketplace, maybe someone has seen you the night before.\n"
          "\tYou see a merchant, and realize you need a weapon, at least to defend yourself")
    
    
    trade()"""
    
    print("\t")
    end = raw_input()