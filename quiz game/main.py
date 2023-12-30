from question_model import QuestionAns
from data import question_data
from quiz_brain import Quiz

questionbank=[]

for i in question_data:
    questionbank.append(QuestionAns(i["question"],i["correct_answer"]))


quiz = Quiz(questionbank)
while quiz.still_questions()  :
    quiz.next_question()

print("you completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.qno}")