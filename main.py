from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    datas = Question(question["text"], question["answer"])
    question_bank.append(datas)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
final_score = quiz.score
total_questions = len(question_bank)
print(f"Your final score was: {final_score}/{total_questions}")