#mostly questions and answers to import in progression.py module. Theoretically everything that happens in the tavern should stay here will happen someday
first_questions = ["(1)I have lost my memory. Do you know who I am?", "(2)I must have gotten drunk. What happened yesterday?"]
first_answers = ["He shakes his head.\n\t\"You got really drunk here last night, but I never saw you before that.\"",
                 "He tries to remember.\n\t\"You got really drunk yesterday. You passed out and hit your head on the table. "
                 "Someone brought you out, said he would help you.\""]

second_questions = {(1): ["(1)Was I with someone? Who?", "(2)Tell me everything you saw me do"],
                    (2): ["(1)Do you remember who helped me? Where can I find him?",
                          "(2)Did I have something yesterday that I didn't have now? Could he have robbed me?"]}
second_answers = {(1): ["\"Yes, you were with another man. You weren't talking to each other, but he bought you beer. "
                        "\n\tHe said he would be taking care of you after you passed out.\"",
                      "\"You came in here with another man, you were looking exhausted. He bought you beer, but you "
                      "weren't talking.\n\tYou were about to leave when you fainted. He said he knew someone who could help you.\""],
                  (2): ["\"I never saw him before either. Maybe the guards saw you two, they might have more information."
                        "\"", "\"You had a short sword, but that's all. I suppose you didn't have money, he bought you beer.\""]}

interaction_decision = "(1)Talk to the two men\n\t(2)Talk to the man and the woman"
interaction_input = ["1", "2"]

men_questions = ["Sorry to interrupt, but can you help me? The innkeeper told me I lost consciousness last night."
                 "\n\tHave you noticed anything strange? I was told a man helped me and now I'm looking for him."]
men_answers = ["They look up but don't say a word. After staring in your eyes for a minute, the older one speaks."
               "\n\t\"We didn't see anything. We just arrived here. Please leave us.\" You see the knife in his hand and step back."]
woman_questions = []
woman_answers = []

men_appearance = ("You see two men sitting at a table, sipping beer, keeping their eyes low. "
                 "They're wearing hoods and look exhausted")
woman_appearance = ("A woman is sitting on a mans lap in a dimly lit corner.\n\tShe's wearing the red dress "
                    "prostitutes wear, but she is not trying to seduce the man.")
