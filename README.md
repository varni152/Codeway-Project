
#Quiz Game
#Overview
The Quiz Game is a Python script that simulates a multiple-choice quiz. It consists of two classes: MCQuestion to represent individual quiz questions, and QuizGame to manage the quiz, track the player's score, and display results. The script allows players to answer questions, provides feedback on correctness, and displays the final score.

#Features
Multiple-Choice Questions: The script supports multiple-choice questions with shuffled answer choices.

Dynamic Question Presentation: Questions are presented in a randomized order, and answer choices are shuffled for each question.

User Interaction: The game engages players by prompting them to select answers using letter choices (e.g., A, B, C).

Score Tracking: The player's score is tracked throughout the game, and the final score is displayed at the end.

Play Again Option: After completing the quiz, players have the option to play again.

#Classes
1.MCQuestion:

Represents a single multiple-choice question.

Attributes:

text: The text of the question.
choices: List of answer choices.
correct_choice: The correct answer.
Methods:

shuffle_choices: Shuffles answer choices and updates the correct choice accordingly.
is_correct: Checks if the user's choice is correct.
2.QuizGame:

Manages the quiz gameplay.

Attributes:

questions: List of MCQuestion objects.
score: Player's score.
question_no: Current question number.
Methods:

display_welcome_message: Displays a welcome message at the beginning of the game.
present_question: Presents a question to the player, takes input, and provides feedback.
play_game: Initiates the quiz game loop.
display_final_results: Displays the final score and completion message.
play_again: Asks the player if they want to play again.
#How to Use
1.Run the Script:

Execute the script by running the quiz_game.py file.
Answer Questions:

Answer each multiple-choice question by entering the letter corresponding to your choice.
Final Score:

After completing the quiz, the script displays the final score and provides an option to play again.
Play Again:

Choose to play the quiz again or exit the game.
