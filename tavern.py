
first_questions = ["(1)I have lost my memory. Do you know who I am?", "(2)I must have gotten drunk. What happened yesterday?"]
first_answers = ["He shakes his head.\n\t\"You got really drunk here last night, but I never saw you before that.\"", "He tries to remember.\n\t\"You got really drunk yesterday. You passed out and hit your head on the table. Someone brought you out, said he would help you.\""]  

second_questions = {(1): ["(1)Was I with someone? Who?", "(2)Tell me everything you saw me do"],
                    (2): ["(1)Do you remember who helped me? Where can I find him?", "(2)Did I have something yesterday that I didn't have now? Could he have robbed me?"]}
second_answers = {(1): ["\"Yes, you were with another man. You weren't talking to each other, but he bought you beer. \n\tHe said he would be taking care of you after you passed out.\"",
                      "\"You came in here with another man, you were looking exhausted. He bought you beer, but you weren't talking.\n\tYou were about to leave when you fainted. He said he knew someone who could help you.\""],
                  (2): ["\"I never saw him before either. Maybe the guards saw you two, they might have more informations.\"", "\"You had a short sword, but that's all. I suppose you didn't have money, he bought you beer.\""]}

interaction_decision = "(1)Talk to the two men\n\t(2)Talk to the man and the woman"
interaction_input = ["1", "2"]

men_questions = {(1, 1): ["1.1.1\tSorry to interrupt, but can you help me? The innkeeper told me I lost consciousness last night.\n\tHave you noticed anything strange? I was told a man helped me",
                          "1.1.2"],
                (1, 2): ["1.2.1",
                         "1.2.2"],
                (2, 1): ["2.1.1",
                         "2.1.2"],
                (2, 2): ["2.2.1",
                         "2.2.2"]}
men_answers = {(1, 1): ["1.1.1\tThe men look up. \"We don't know anything. Please leave us alone\"", "1.1.2"],
                (1, 2): ["1.2.1",
                         "1.2.2"],
                (2, 1): ["2.1.1",
                         "2.1.2"],
                (2, 2): ["2.2.1",
                         "2.2.2"]}
woman_questions = {}
woman_answers = {}