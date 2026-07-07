## **Task-1 Hangman game**

# 🎮 Hangman Game

A simple text-based Hangman game built using **Python**. The player tries to guess a randomly selected word one letter at a time before running out of attempts.

## 📌 Features

- Randomly selects a word from a predefined list.
- Allows the player to guess one letter at a time.
- Maximum of **6 incorrect attempts**.
- Displays the progress using underscores (`_`).
- Prevents duplicate guesses.
- Validates user input (accepts only single alphabet letters).
- Console-based gameplay with no graphics or audio.

## 🛠️ Technologies Used

- Python 3
- Random Module
- Lists
- Strings
- While Loop
- If-Else Statements

## 📂 Project Structure

```
Hangman-Game/
│── hangman.py
│── README.md
|__ Learnings
```

## ▶️ How to Run

1. Clone this repository.
2. Open the project in your preferred Python IDE or terminal.
3. Run the following command:

```bash
python hangman.py
```

## 🎯 Game Rules

- A random word is selected from the predefined list.
- Guess one letter at a time.
- Each incorrect guess reduces your remaining attempts.
- You have **6 chances** to guess the word.
- Guess all letters correctly before your attempts run out to win.

## 📷 Sample Output

```
Welcome to the Simple Hangman Game

Guess the word:
_ _ _ _ _

Enter a letter: a
Correct!

Word: a _ _ _ _

Enter a letter: p
Correct!

Word: a p p _ _

Congratulations! You Win!
```

## 🚀 Future Improvements

- Add difficulty levels.
- Add hints for words.
- Display Hangman ASCII art.
- Allow players to play multiple rounds.
- Load words from a file or API.

## 👩‍💻 Author

**Hema Gandimanu**

B.Tech Computer Science & Engineering Student

---
⭐ If you like this project, consider giving it a star on GitHub!
