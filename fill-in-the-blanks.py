# IURIE POPOVICI Stage 2 Final Project

blanks = ["__1__", "__2__", "__3__", "__4__"]
easy_quiz ="""Illinois is a state in the __1__ region of the United
States. The state's largest city is __2__,
the capital is __3__. Illinois is located in the __4__ Time Zone.
"""
easy_answers = ["Midwestern", "Chicago", "Springfield", "Central"]
medium_quiz = """__1__ is the third most populous city in the
United States. With over 2.7 million residents,
it is the most populous city in the state of __2__ and the Midwestern
United States, and the county seat of Cook County.
The Chicago __3__ area, often referred to as __4__, has nearly
10 million people and is the third-largest in the U.S.
"""
medium_answers = ["Chicago", "Illinois", "metropolitan", "Chicagoland"]
hard_quiz = """Python is an easy to learn, powerfull programming
__1__. It has a simple but effective approach to object-oriented
__2__. Python's elegant syntax and dynamic typing, together with its
interpreted nature, make it an ideal language for scripting and rapid
application __3__ in many areas on most __4__.
"""
hard_answers = ["language", "programming", "development", "platforms"]


def correct_answer(paragraph, answers, index ):
    """Takes as input a text with blanks, user's correct answers, and
    outputs the text with blanks filled in.
    """
    max_index = 3
    print "Correct !\n"
    paragraph = paragraph.replace(('__'+str(index + 1)+'__'), answers[index])
    print "The current paragraph:\n" + paragraph
    index = index + 1
    if index <= max_index:
        user_input = raw_input("\nWhat should be substituted in for " + blanks[index] + "? ")
        answer = user_input
        return paragraph, answer, index
    else:
        print "You Won!!!\n"
        exit()

def check_answer(word, paragraph, answers):
    """Takes as input the answer given by user and checks if it is the
    correct or wrong answer. It also counts the number of tries. The
    lower() method was used to make user's input case-insensitive.
    """
    index, number_of_tries, max_tries = 0, 0, 5
    answer = str(word)
    while number_of_tries < max_tries:
        if answer.lower() != answers[index].lower():
            number_of_tries += 1
            if number_of_tries == max_tries:
                print "You've failed too many straight guesses!  Game over!\n"
            else:
                print "That isn't the correct answer! Tries left: " + str(max_tries-number_of_tries) + "\n"
                print "The current paragraph:\n" + paragraph
                user_input = raw_input("What should be substituted in for " + blanks[index] + "? ")
                answer = user_input
        else:
            number_of_tries = 0
            paragraph, answer, index = correct_answer(paragraph, answers, index)

def level(quiz, answers, pick_level):
    """Outputs the text of chosen difficulty and takes user's answers
    as input.
    """
    print "You've chosen " + pick_level + "//5 tries per problem.\n\nThe current paragraph:\n" + quiz + "\n"
    index = 0
    user_input = raw_input("What should be substituted in for " + blanks[index] + "? ")
    word = str(user_input)
    check_answer(word, quiz, answers)

def take_quiz():
    """Plays the full quiz, giving the user a choise of difficulty. The
    lower() method was used to make user's input case-insensitive.
    """
    pick_level = raw_input("Select a game difficulty from easy/medium/hard by typing it in:\n").lower()
    if pick_level == 'easy':
        level(easy_quiz, easy_answers, pick_level)
    elif pick_level == 'medium':
        level(medium_quiz, medium_answers, pick_level)
    elif pick_level == 'hard':
        level(hard_quiz, hard_answers, pick_level)
    else:
        print "That's not an option!"
        take_quiz()

take_quiz()

