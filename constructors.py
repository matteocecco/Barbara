import sys                                                                              #import the sys module. Needed to exit the program by typing "exit"
import random                                                                           #import the random module. Needed to roll dice

def dialogue(questions, answers):                                                       #questions and answers need to be lists
    choice_int = 1
    for question in questions:                                                          #cicle through the questions
        print("\t%s" % question)                                                        #print every question on a separate line
    if len(questions) > 1:                                                              #if there's more than one question (length of list is > 1 element):
        while True:                                                                     #Loop to verify that the input is an integer (else the program would break)
            choice = raw_input()                                                        #take the input
            if choice:                                                                  #can't remember why I put this
                pass                                                                    #considering it does nothing. pass means "carry on, I'm a placeholder but don't do nothing"
            try:                                                                        #try/except. Try to do this:
                choice_int = int(choice)                                                #convert choice to integer (raw_input() takes only strings)
                break                                                                   #exit loop if it works
            except ValueError:                                                          #but if it doesn't work (choice is not a number, ValueError)
                print("\tYou forgot what you wanted to ask")                            #don't break context with stupid error messages, and repeat the loop. Take input again, convert
    else:                                                                               #if there's only one question
        raw_input()                                                                     #simply break the text so the next lines print only after hitting enter
    choice = choice_int - 1                                                             #choice_int is always at least 1, but list offsets start at 0, so we need to take one down
    print("\t%s\n" % answers[choice])                                                   #print the answer in the list that corresponds to the option chosen
    return choice_int                                                                   #return which option was chosen (needed for branching conversations)


def continued_dialogue(first_question, questions, answers):                             #for longer dialogues that depend on previous choices. first_question carries the return value of the previous questions, questions and answers have to be dictionaries this time
    values = []                                                                         #l is an empty list for now
    if type(first_question) is int:                                                     #if first_question is an integer (ie only one question is influencing this conversation
        value = dialogue(questions[first_question], answers[first_question])            #run the dialogue function and store it's return in value. This time the parameters are dictionaries, and every key points to a list of questions. In this case the key is the question chosen before (see also example below)
        values = (first_question, value)                                                #take both first_question and the new value and store them in a tuple
    elif type(first_question) is list:                                                  #else if first_question is a list(so it's three layers deep or more into the conversation
        tup = tuple(first_question)                                                     #make first_question a tuple (dictionaries don't take lists as keys
        value = dialogue(questions[tup], answers[tup])                                  #same concept as before, just more elaborate. Key is not a single integer but a tuple, meaning there is more options available
        back_to_list = list(tup)                                                        #now the tuple is converted back to a list
        back_to_list.append(value)                                                      #and we append the new value to the list
        values = tuple(back_to_list)                                                    #and we reconvert back to tuple
    else:                                                                               #if something went wrong, it's because first_question is not the right type
        print type(first_question)                                                      #so print what type it is
    return list(values)                                                                 #return values as a list


def player_choice(printed_text, expected_input):                                        #unused yet, but it will shine someday. To make sure the program knows what to do if typos happen. printed_text is a string, expected_input a list of strings
    while True:                                                                         #infinite loop
        choice = raw_input("\t%s\n\t" % printed_text).lower()                           #lowercase everything, easier to control
        if choice in expected_input:                                                    #if the choice is in expected input
            return choice                                                               #return said choice (to use in later if/else loops)
        elif choice == "exit":                                                          #if you type exit
            sys.exit()                                                                  #close the program
        else:                                                                           #if typo
            print("\tYou forgot what you wanted to do\n")                               #error messagge without breaking the flow
            continue                                                                    #just carry on back from the beginning of the loop (probably useless but I like it so it stays there


def dice_roll():                                                                        #dice roll, will need for skill checks  
    return random.randint(1, 20)                                                        #return a random integer between 1 and 20

def pcheck(user, check, check_find, max_find, critical_failure):                        #perception check, to use when player class and object are created
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
