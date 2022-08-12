import random

class Quiz:
    
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question: {self.questionIndex + 1} : {question.text}")
        
        for q in question.choices:
            print("-" + q)
            
        answer = "python"  # change if you want to return a False answers or use input method for an ansewer from user
        
        if question.checkAnswer(answer):
            self.score += 1
            print("Yes, true!")
            
        self.questionIndex += 1
        self.loadQuestion()
        
    def displayScore(self):
        print("Your test result: ".center(100, "*"))
        point = 100 / len(self.questions)
        total_score = round(self.score * point)
        print(f"Your total score: ", str(total_score))         
            
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def displayProgress(self):
        total_question = len(self.questions)
        question_number = self.questionIndex + 1
        print(f"You are on {question_number} of {total_question}".center(100, "*"))