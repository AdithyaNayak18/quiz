# from main import question_bank
#
# score = 0
#
# for i in range(0, 11):
#
#     newq_text = question_bank[i].text
#     newq_answer = question_bank[i].answer
#
#     print(newq_text)
#
#     user_ans = input("Your answer: ")
#
#
#     if user_ans == newq_answer:
#         score += 1
#         print("You're right!")
#         print("Score : ", score)
#         continue
#
#     else:
#         print("You're wrong!")
#         print("Score : ", score)
#         exit(0)
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        input(f"Q.{self.question_number}: {current_question.text} (True/False) : ")

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you're right!")
            self.score+=1

        else:
            print("You're wrong!")

        print(f"Score = {self.score}/{self.question_number}\n")

