
class Quiz:
    def __init__(self,questionbank):
        self.qno=0
        self.questionbank=questionbank
        self.score =0

    def still_questions(self):
        if self.qno!=len(self.questionbank):
            return True
        else :
            return False

    def next_question(self):
        # question equals the question present in the question bank at the index of self.qno 
        answer=input(f"Q{self.qno+1}.{self.questionbank[self.qno].question}(True/False)").lower()
        
        self.check_ans(answer,self.questionbank[self.qno].answer)
        self.qno+=1

    def check_ans (self,answer,correct_ans):
        if answer == correct_ans.lower() :
            self.score+= 1
            print("the answer is correct ")
            # print(f"your score is {self.score}/{self.score}")
        else :
            print("the answer is wrong ")
            # print(f"your score is {self.score}/{self.qno}")

        print(f"the correct answer is {correct_ans}")
        print(f"your score is {self.score}/{self.qno+1}")

        



















