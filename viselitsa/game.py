import random

WORDS_FILE = "words.txt"
PICTURES_FOLDER = "hangman/"
MAX_ERRORS = 6


def load_words():
    with open(WORDS_FILE, "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    return [word.strip().lower() for word in words if word.strip()]


def load_picture(errors):
    filename = PICTURES_FOLDER + str(errors) + ".txt"
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


def show_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    print("\nСлово:", result)


def start_game():
    words = load_words()
    word = random.choice(words)
    guessed_letters = []
    errors = 0

    print("Игра Виселица")
    print("Угадай загаданное слово!")

    load_picture(errors)

    while errors < MAX_ERRORS:
        show_word(word, guessed_letters)

        letter = input("Введи букву: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Введи одну букву.")
            continue

        if letter in guessed_letters:
            print("Ты уже вводил эту букву.")
            continue

        guessed_letters.append(letter)

        if letter in word:
            print("Правильно!")
        else:
            errors += 1
            print("Такой буквы нет.")
            load_picture(errors)

        if all(char in guessed_letters for char in word):
            print("Ты победил! Слово:", word)
            return

    print("Ты проиграл! Загаданное слово:", word)