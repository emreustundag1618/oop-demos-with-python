# Question class
###  Instance Attributes: text, choice, answer
###  Instance Methods: checkAnswer() --> True or False

# Quiz class
###  Instance Attributes: questions, questionIndex, score
###  Instance Methods: 
###         getQuestion() ---> gets a question object by question index
###         displayQuestion() ---> shows object accessed by getQuestion()
###         loadQuestion() ---> starts the test
###         displayScore() ---> displays the score
###         displayProgress() ---> display the progress (like if 3rd question of 5: 3 / 5

class Question:
    
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("an error occured")
        return self.answer == answer

q1 = Question("Which is the most common programming language for Data Science?",["python","c#","java","dart"],"python")
q2 = Question("Which is the most popular for Machine Learning?",["python","java","c#","dart"],"python")
q3 = Question("Which is the most library-written language for Deep Learning?",["python","java","dart","c#"],"python")

questions = [q1, q2, q3]