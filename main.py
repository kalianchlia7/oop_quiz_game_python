from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]    #call text in dictionary
    question_answer = question["answer"] #call answer in dicitonary
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)  #append question objects to new list

quiz = QuizBrain(question_bank) 
#passing in smth for q_list
#creating the quizbrain object

while quiz.still_has_questions():
    quiz.next_question()
    #calling the function in quizbrain

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")