"""Duolingo."""

class Word:
    # Класс Word нужен для хранения одного слова сразу на трёх языках.
    # Один объект Word = одно слово или одна фраза.
    def __init__(self, english, estonian, russian):
        # Сохраняем английский вариант слова.
        self.english = english

        # Сохраняем эстонский вариант слова.
        self.translation = estonian

        # Сохраняем русский вариант слова.
        self.russian = russian


class User:
    # Класс User хранит информацию о пользователе.
    # Например: имя пользователя, его очки и слова.
    def __init__(self, name):
        # Сохраняем имя пользователя.
        self.name = name

        # В начале у пользователя 0 очков.
        # За каждый правильный ответ мы будем добавлять 1 очко.
        self.score = 0

        # Здесь можно хранить слова пользователя.
        # Это словарь: ключ = английское слово, значение = объект Word.
        self.words = {}

    def add_word(self, word):
        # Добавляем слово в словарь пользователя.
        # Например:
        # ключ: "Hello"
        # значение: объект Word("Hello", "Tere", "Привет")
        self.words[word.english] = word
        

    def get_words(self):
        # Возвращаем все слова пользователя.
        return self.words


class Lesson:
    # Класс Lesson отвечает за сам урок.
    # В уроке есть пользователь, название урока, языки и список слов.
    def __init__(self, user, name):
        # Список языков, которые поддерживает программа.
        self.languages = ["english", "estonian", "russian"]

        # Пользователь, который проходит урок.
        self.user = user

        # Название урока.
        self.name = name

        # Язык, с которого нужно переводить.
        # Пока пользователь не выбрал язык, здесь None.
        self.lessonLanguage = None

        # Язык, на который нужно переводить.
        # Пока пользователь не выбрал язык, здесь None.
        self.targetLanguage = None

        # Список слов для урока.
        self.words = []

    def _ask_language_choice(self, message):
        # Этот метод спрашивает у пользователя язык.
        # Мы сделали отдельный метод, чтобы не писать одинаковый input два раза.

        print(message)

        # Показываем пользователю варианты выбора.
        choice = input("1. English\n2. Estonian\n3. Russian\n")

        # Превращаем выбор "1", "2" или "3" в название языка.
        return self._choice_to_language(choice)

    def choose_language(self):
        # Метод для выбора языков урока.

        # Пользователь выбирает язык, с которого он будет переводить.
        self.lessonLanguage = self._ask_language_choice("Choose source language:")

        # Пользователь выбирает язык, на который он будет переводить.
        self.targetLanguage = self._ask_language_choice("Choose target language:")

        # Проверяем, не выбрал ли пользователь одинаковые языки.
        # Например: English -> English.
        # Так делать нельзя, потому что переводить слово на тот же язык бессмысленно.
        if self.targetLanguage == self.lessonLanguage:
            print("Source and target are the same. Defaulting target to Estonian.")

            # Если исходный язык НЕ эстонский,
            # тогда язык ответа автоматически будет эстонский.
            if self.lessonLanguage != "estonian":
                self.targetLanguage = "estonian"

            # Если исходный язык уже эстонский,
            # тогда язык ответа автоматически будет английский.
            else:
                self.targetLanguage = "english"

    def _choice_to_language(self, choice):
        # Этот метод превращает число в название языка.

        # Если пользователь ввёл 1, выбираем английский язык.
        if choice == "1":
            return "english"

        # Если пользователь ввёл 2, выбираем эстонский язык.
        if choice == "2":
            return "estonian"

        # Если пользователь ввёл 3, выбираем русский язык.
        if choice == "3":
            return "russian"

        # Если пользователь ввёл что-то неправильное,
        # программа автоматически выбирает английский язык.
        print("Invalid choice. Defaulting to English.")
        return "english"

    def _word_in_language(self, word, language):
        # Этот метод возвращает слово на нужном языке.

        # Если нужен эстонский язык, возвращаем эстонский перевод.
        if language == "estonian":
            return word.translation

        # Если нужен русский язык, возвращаем русский перевод.
        if language == "russian":
            return word.russian

        # Во всех остальных случаях возвращаем английский вариант.
        return word.english

    def get_words(self):
        # Возвращаем список слов урока.
        return self.words

    def startLesson(self):
        # Метод запускает урок.

        # Сначала пользователь выбирает языки.
        self.choose_language()

        # Показываем начало урока.
        print(
            f"Starting {self.name}: {self.lessonLanguage} -> {self.targetLanguage} "
            f"for {self.user.name}. Your current score is {self.user.score}. Good luck!"
        )

        # Запоминаем, сколько очков было до начала урока.
        start_score = self.user.score

        # Проходим по каждому слову из списка слов.
        for word in self.words:
            # Получаем слово на исходном языке.
            source_text = self._word_in_language(word, self.lessonLanguage)

            # Получаем правильный ответ на целевом языке.
            target_text = self._word_in_language(word, self.targetLanguage)

            # Спрашиваем пользователя перевод.
            print(
                f"What is the translation of '{source_text}' "
                f"from {self.lessonLanguage} to {self.targetLanguage}?"
            )

            # Получаем ответ пользователя.
            # strip() убирает лишние пробелы в начале и в конце.
            answer = input().strip()

            # Сравниваем ответ пользователя с правильным ответом.
            # lower() нужен, чтобы большие и маленькие буквы не мешали проверке.
            if answer.lower() == target_text.lower():
                print("Correct!")

                # Если ответ правильный, добавляем 1 очко.
                self.user.score += 1
            else:
                # Если ответ неправильный, показываем правильный ответ.
                print(f"Wrong! The correct answer is '{target_text}'.")

        # Считаем, сколько правильных ответов было именно в этом уроке.
        lesson_score = self.user.score - start_score

        # Показываем результат урока.
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
