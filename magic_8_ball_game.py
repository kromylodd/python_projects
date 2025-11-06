import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
def is_valid(question):
    if question == "" or question[-1] != "?":
        return False
    else:
        return True
more_questions = ""
print("enter your name")
name = input()
print(f"wazzap {name}")
while more_questions != "n":
    answer = answers[random.randint(0,20)]
    question = ""
    while not is_valid(question):
        print("put a valid question, needs to end with '?'")
        question = input()
    print(f"The answer to your question is {answer}")
    print("any more questions? (n for exit, anything else for a question)")
    more_questions = input()
print(f"glad youre satisfied {name}, seeu")
