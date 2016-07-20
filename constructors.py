import sys
import random

def dialogue(questions, answers):                                                       #questions and answers need to be lists
    choice_int = 1
    for question in questions:                                                          #cicle through the questions
        print("\t%s" % question)                                                        #print every question on a separate line
    if len(questions) > 1:
        while True:                                                                     #bit more complicated.  Loop to verify that the input is an integer (else the program would break)
            choice = raw_input()                                                        #take the input
            if choice:
                pass
            try:                                                                        #try/except. Try to do this:
                choice_int = int(choice)                                                #convert choice to integer (iirc input() takes only strings)
                break                                                                   #exit loop if it works
            except ValueError:                                                          #but if it doesn't work (choice is not an integer)
                print("\tYou forgot what you wanted to ask")                            #don't break context with stupid error messages, and repeat the loop. take input again, convert
    else:
        raw_input()
    choice = choice_int - 1
    print("\t%s\n" % answers[choice])
    return choice_int


def continued_dialogue(first_question, questions, answers):
    l = []
    if type(first_question) is int:
        value = dialogue(questions[first_question], answers[first_question])
        l = (first_question, value)
    elif type(first_question) is list:
        tup = tuple(first_question)
        value = dialogue(questions[tup], answers[tup])
        back_to_list = list(tup)
        back_to_list.append(value)
        l = tuple(back_to_list)
    else:
        print type(first_question)
    return list(l)


def player_choice(printed_text, expected_input):
    while True:
        choice = raw_input("\t%s\n\t" % printed_text).lower()
        if choice in expected_input:
            return choice
        elif choice == "exit":
            sys.exit()
        else:
            print("\tYou forgot what you wanted to do\n")
            continue


def dice_roll():
    return random.randint(1, 20)

"""
def pcheck(user, check, check_find, max_find, critical_failure):        #perception check, to use when player class and object are created
    dice = dice_roll()
    combined = user.stats['str'] + dice
    if combined >= check and dice == 20:
        print("\t%s\n\t%s" % (check_find, max_find))
        return 2
    elif combined >= check:
        print("\t%s" % check_find)
        return 1
    elif combined < check:
        print("\tYou see nothing you didn't see so far")
        return 0
    elif combined < check and dice == 1:
        print("\t%s" % critical_failure)
        return -1
"""
example_questions = ["(1)Question 1", "(2)Question 2"]                                      #could be more than just two questions, but it's easier
example_answers = ["Answer to question 1", "Answer to question 2"]
example_dialogue = dialogue(example_questions, example_answers)

continued_questions = {1: ["(1)I guess you chose question 1 before", "(2)Again, you chose question 1 first"],
                        2: ["(1)You must have chosen question 2 earlier", "(2)Booyah! Question 2, amirite?"]}
continued_answers = {1: ["Heh, you chose 1 both times. Consistent", "First 1, now 2."],
                        2: ["first 2, now 1? Ok", "2, and 2 again? Consistency is the key"]}
continued_example_dialogue = continued_dialogue(example_dialogue, continued_questions, continued_answers)

last_example_questions = {(1, 1): ["Let's make this quick. You chose, 1, then 1, now this is 1 again", "1, then 1, now 2"],
                            (1, 2): ["1, then 2, now 1", "1, then 2, now 2"],
                            (2, 1): ["2, then 1, now 1 again", "2, then 1, now 2"],
                            (2, 2): ["2, then 2, now 1", "2, then 2, now 2"]}
last_example_answers = {(1, 1): ["1-1-1", "1-1-2"],
                        (1, 2): ["1-2-1", "1-2-2"],
                        (2, 1): ["2-1-1", "2-1-2"],
                        (2, 2): ["2-2-1", "2-2-2"]}
last_example = continued_dialogue(continued_example_dialogue, last_example_questions, last_example_answers)
