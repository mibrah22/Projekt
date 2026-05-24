"""Duolingo."""

class Word:
    def __init__(self, english, estonian, russian):
        self.english = english
        self.translation = estonian
        self.russian = russian


class User:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.words = {}

    def add_word(self, word):
        self.words[word.english] = word
        

    def get_words(self):
        return self.words


class Lesson:
    def __init__(self, user, name):
        self.languages = ["english", "estonian", "russian"]
        self.user = user
        self.name = name
        self.lessonLanguage = None
        self.targetLanguage = None
        self.words = []

    def _ask_language_choice(self, message):
        print(message)
        choice = input("1. English\n2. Estonian\n3. Russian\n")
        return self._choice_to_language(choice)

    def choose_language(self):
        self.lessonLanguage = self._ask_language_choice("Choose source language:")
        self.targetLanguage = self._ask_language_choice("Choose target language:")
        if self.targetLanguage == self.lessonLanguage:
            print("Source and target are the same. Defaulting target to Estonian.")
            if self.lessonLanguage != "estonian":
                self.targetLanguage = "estonian"
            else:
                self.targetLanguage = "english"

    def _choice_to_language(self, choice):
        if choice == "1":
            return "english"
        if choice == "2":
            return "estonian"
        if choice == "3":
            return "russian"
        print("Invalid choice. Defaulting to English.")
        return "english"

    def _word_in_language(self, word, language):
        if language == "estonian":
            return word.translation
        if language == "russian":
            return word.russian
        return word.english
        
    def get_words(self):
        return self.words

    def startLesson(self):
        self.choose_language()
        print(
            f"Starting {self.name}: {self.lessonLanguage} -> {self.targetLanguage} "
            f"for {self.user.name}. Your current score is {self.user.score}. Good luck!"
        )
        start_score = self.user.score
        for word in self.words:
            source_text = self._word_in_language(word, self.lessonLanguage)
            target_text = self._word_in_language(word, self.targetLanguage)
            print(
                f"What is the translation of '{source_text}' "
                f"from {self.lessonLanguage} to {self.targetLanguage}?"
            )
            answer = input().strip()
            if answer.lower() == target_text.lower():
                print("Correct!")
                self.user.score += 1
            else:
                print(f"Wrong! The correct answer is '{target_text}'.")
        lesson_score = self.user.score - start_score
        print("Lesson finished!")
        print(f"User: {self.user.name}")
        print(f"Lesson: {self.name}")
        print(f"Correct answers in this lesson: {lesson_score} / {len(self.words)}")
        print(f"Total score: {self.user.score}")


word1 = [
    Word("Hello", "Tere", "Привет"),
    Word("Goodbye", "Head aega", "До свидания"),
    Word("Thank you", "Aitäh", "Спасибо"),
    Word("Yes", "Jah", "Да"),
    Word("No", "Ei", "Нет"),
    Word("Please", "Palun", "Пожалуйста"),
    Word("Sorry", "Vabandust", "Извините"),
    Word("Excuse me", "Vabandage", "Извините"),
    Word("How are you?", "Kuidas sul läheb?", "Как дела?"),
    Word("What is your name?", "Mis su nimi on?", "Как тебя зовут?"),
    Word("Correct", "Õige", "Верно")
]

user1 = User('Alice')
lesson1 = Lesson(user1, "Basic Vocabulary")
lesson1.words.extend(word1)
lesson1.startLesson()
