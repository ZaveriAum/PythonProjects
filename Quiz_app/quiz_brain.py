class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.quiz_score = 0
        self.question_list = question_list

    def still_has_question(self, question_list):
        return not self.question_number == len(question_list)

    def next_question(self, question_list):
        print(f"Here is your question:- {self.question_number + 1}.\n{question_list[self.question_number].text}")
        self.question_number += 1
        ans = input("True or False ?").lower()
        self.check_answer(ans, question_list[self.question_number - 1].answer, question_list)

    def check_answer(self, user_answer, correct_answer, question_list):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.quiz_score += 1
        else:
            print(f"You got it wrong.\nThe correct answer is {correct_answer}")
        print(f"You score: {self.quiz_score}/{self.question_number}\n")
        if self.question_number == len(question_list):
            print(f"You have completed the quiz.\nYour final score is {self.quiz_score}/{self.question_number}")
