from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# ------------------------------- Result ------------------------------- #
# Q.1: The HTML5 standard was published in 2014. (True/False): True
# You got it right!
# The correct answer was: True.
# Your current score is: 1/1
#
#
# Q.2: The first computer bug was formed by faulty wires. (True/False): False
# You got it right!
# The correct answer was: False.
# Your current score is: 2/2
#
#
# Q.3: FLAC stands for 'Free Lossless Audio Condenser'. (True/False): True
# That's wrong.
# The correct answer was: False.
# Your current score is: 2/3
#
#
# Q.4: All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine. (True/False): False
# You got it right!
# The correct answer was: False.
# Your current score is: 3/4
#
#
# Q.5: Linus Torvalds created Linux and Git. (True/False): True
# You got it right!
# The correct answer was: True.
# Your current score is: 4/5
#
#
# Q.6: The programming language 'Python' is based off a modified version of 'JavaScript' (True/False): False
# You got it right!
# The correct answer was: False.
# Your current score is: 5/6
#
#
# Q.7: AMD created the first consumer 64-bit processor. (True/False): True
# You got it right!
# The correct answer was: True.
# Your current score is: 6/7
#
#
# Q.8: 'HTML' stands for Hypertext Markup Language. (True/False): True
# You got it right!
# The correct answer was: True.
# Your current score is: 7/8
#
#
# Q.9: In most programming languages, the operator ++ is equivalent to the statement '+= 1'. (True/False): True
# You got it right!
# The correct answer was: True.
# Your current score is: 8/9
#
#
# Q.10: The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory. (True/False): True
# That's wrong.
# The correct answer was: False.
# Your current score is: 8/10
#
#
# You've completed the quiz
# Your final score was: 8/10
