import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome(self):
        print("Welcome to the Quiz Game!")
        print("Rules: Answer each question to the best of your ability. Let's get started!\n")

    def display_question(self, question):
        print(question['question'])
        for idx, choice in enumerate(question['choices'], start=1):
            print(f"{idx}. {choice}")
        print()

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.")
            self.score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")

    def play_quiz(self):
        self.display_welcome()

        for question in self.questions:
            self.display_question(question)
            user_answer = input("Your answer : ")
            correct_answer = question['correct_choice']

            self.evaluate_answer(user_answer, correct_answer)
            print(f"Your current score: {self.score}\n")

        print("Quiz complete!")
        print(f"Your final score is: {self.score}")
        print("Thanks for playing!")

def main():
    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'choices': ['London', 'Berlin', 'Paris', 'Madrid'],
            'correct_choice': 'Paris'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'choices': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
            'correct_choice': 'Mars'
        },
        {
            'question': 'Python is a programming language. (True/False)',
            'choices': ['True', 'False',],
            'correct_choice': 'True'
        },
        # Add more questions as needed
    ]

    game = QuizGame(quiz_questions)
    game.play_quiz()

if __name__ == "__main__":
    main()
