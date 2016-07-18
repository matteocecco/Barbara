# Barbara

-type "exit" at any text break to close program<br>
-dialogue constructor: to build a dialogue, create two lists, one for questions (every question one element of the list), and one for answers<br>
-in progress.py, declare a new variable: <tt>example_dialogue = constructors.dialogue(questions_list, answers_list)</tt><br>
-answers to one question must be at the same offset in their list as the question in the questions list:<br>
<tt>questions = ["question1","question2"]</tt><br><tt>answers=["answer1", "answer2"]</tt><br> so that <tt>question[0]</tt> will get <tt>answer[0]</tt><br><br>
