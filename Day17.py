question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.right_answer=0
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_input=input(f"Q.{self.question_number}: {current_question.text} (True/False)? :")
        self.check_answer(user_input,current_question.answer)
    def check_answer(self,user_input,question_answer):
        if user_input.lower()==question_answer.lower():
            print("You got it right!")
            self.right_answer+=1
        else:
            print("That's wrong.")
        print(f"The correct answer was {question_answer}.")
        print(f"Your currect score is {self.right_answer}/{self.question_number}")
        print("\n")


class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer


question_bank=[]
for x in question_data:
    question_bank.append(Question(x["text"],x["answer"]))

print(question_bank[0].text)
a=QuizBrain(question_bank)
while a.still_has_questions():
    a.next_question()

print("You have completed the quiz.")
print(f"Your final score was {a.right_answer}/{a.question_number}")
