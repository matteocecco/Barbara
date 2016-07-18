import sys


def dialogue(questions, answers):                                                   #questions and answers need to be lists
    for question in questions:                                                      #cicle through the questions
        print("\t%s" % question)                                                    #print every question on a separate line
    while True:                                                                     #bit more complicated.  Loop to verify that the input is an integer (else the program would break)
        choice = raw_input()                                                        #take the input
        try:                                                                        #try/except. Try to do this:
            choice_int = int(choice)                                                #convert choice to integer (iirc input() takes only strings)
            break                                                                   #exit loop if it works
        except ValueError:                                                          #but if it doesn't work (choice is not an integer)
            print("\tYou forgot what you wanted to ask")                            #don't break context with stupid error messages, and repeat the loop. take input again, convert
    choice = choice_int - 1
    print("\t%s\n" % answers[choice])
    return choice_int


def continued_dialogue(first_question, questions, answers):
    dialogue(questions[first_question], answers[first_question])


def player_choice(printed_text, expected_input):
    while True:
        choice = raw_input("\t%s\n\t" % printed_text).lower()
        if choice in expected_input:
            break
        elif choice == "exit":
            sys.exit()
        else:
            print("\tYou forgot what you wanted to do\n")
            continue
    return choice


