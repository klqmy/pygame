import random

levels = [
    {
        "question": "Вы стоите перед тремя дверями. Первая дверь ведет к огнедышащему дракону. Вторая дверь ведет к загадочному лабиринту. Третья дверь - ваш выход.",
        "correct_answer": "3",
        "options": ["1. Первая", "2. Вторая", "3. Третья"]
    },
    {
        "question": "Какой из этих предметов - друг человека? Первая дверь - хомяк. Вторая дверь - кошка. Третья дверь - собака.",
        "correct_answer": "3",
        "options": ["1. Хомяк", "2. Кошка", "3. Собака"]
    },
    {
        "question": "Кто может летать, но не имеет крыльев? Первая дверь - птица. Вторая дверь - самолет. Третья дверь - мечта.",
        "correct_answer": "3",
        "options": ["1. Птица", "2. Самолет", "3. Мечта"]
    },
    {
        "question": "Что можно поймать, но не может бежать? Первая дверь - рыба. Вторая дверь - холод. Третья дверь - мысль.",
        "correct_answer": "3",
        "options": ["1. Рыба", "2. Холод", "3. Мысль"]
    },
    {
        "question": "Какой месяц имеет 28 дней? Первая дверь - август. Вторая дверь - все. Третья дверь - февраль.",
        "correct_answer": "2",
        "options": ["1. Август", "2. Все", "3. Февраль"]
    },
    {
        "question": "Какой океан самый большой? Первая дверь - Атлантический океан. Вторая дверь - Индийский океан. Третья дверь - Тихий океан.",
        "correct_answer": "3",
        "options": ["1. Атлантический", "2. Индийский", "3. Тихий"]
    },
    {
        "question": "Сколько континентов на Земле? Первая дверь - 5. Вторая дверь - 6. Третья дверь - 7.",
        "correct_answer": "3",
        "options": ["1. 5", "2. 6", "3. 7"]
    },
    {
        "question": "Что может заполнить комнату, но не занимает места? Первая дверь - Свет. Вторая дверь - Звук. Третья дверь - Воздух.",
        "correct_answer": "1",
        "options": ["1. Свет", "2. Звук", "3. Воздух"]
    },
    {
        "question": "Какой год был годом начала Второй мировой войны? Первая дверь - 1939. Вторая дверь - 1941. Третья дверь - 1945.",
        "correct_answer": "1",
        "options": ["1. 1939", "2. 1941", "3. 1945"]
    },
    {
        "question": "Небесное тело, вращающееся по орбите вокруг звезды или её остатков? Первая дверь - комета. Вторая дверь - звезда. Третья дверь - планета.",
        "correct_answer": "3",
        "options": ["1. Комета", "2. Звезда", "3. Планета"]
    },
    {
        "question": "Какой элемент периодической таблицы обозначается символом 'O'? Первая дверь - золото. Вторая дверь - кислород. Третья дверь - водород.",
        "correct_answer": "2",
        "options": ["1. Золото", "2. Кислород", "3. Водород"]
    },
    {
        "question": "Какое число является квадратом 144?",
        "correct_answer": "2",
        "options": ["1. 10", "2. 12", "3. 14"]
    },
    {
        "question": "Сколько планет в нашей солнечной системе? Первая дверь - 8. Вторая дверь - 9. Третья дверь - 7.",
        "correct_answer": "1",
        "options": ["1. 8", "2. 9", "3. 7"]
    },
    {
        "question": "Какой этот цвет - смесь красного и белого? Первая дверь - фиолетовый. Вторая дверь - розовый. Третья дверь - оранжевый.",
        "correct_answer": "2",
        "options": ["1. Фиолетовый", "2. Розовый", "3. Оранжевый"]
    },
    {
        "question": "Какой самый большой млекопитающий в мире? Первая дверь - слон. Вторая дверь - синий кит. Третья дверь - жираф.",
        "correct_answer": "2",
        "options": ["1. Слон", "2. Синий кит", "3. Гиппопотам"]
    }
]

bonus_questions = [
    {
        "question": "Какая гора самая высокая в мире? Первая дверь - Чогори (К2). Вторая дверь - Джомолунгма (Эверест). Третья дверь - Канченджанга.",
        "correct_answer": "2",
        "options": ["1. Чогори (К2)", "2. Джомолунгма (Эверест)", "3. Канченджанга"]
    },
    {
        "question": "Я всегда с тобой, но ты не можешь меня увидеть. Первая дверь - Тень. Вторая дверь - Время. Третья дверь - Воздух.",
        "correct_answer": "2",
        "options": ["1. Тень", "2. Время", "3. Нос"]
    },
    {
        "question": "У него есть зубы, но он не может кусать. Что это? Первая дверь - Пила. Вторая дверь - Расчёска. Третья дверь - Грабли.",
        "correct_answer": "2",
        "options": ["1. Пила", "2. Расчёска", "3. Грабли"]
    }
]

def play_level(level, hints_available):
    print(f"\nУровень: {levels[level]['question']}")
    options = levels[level]["options"]

    for option in options:
        print(option)

    if hints_available > 0:
        use_hint = input(f"Ваше количество подсказок: {hints_available}. Хотите использовать подсказку? (да/нет): ").strip().lower()
        if use_hint in ["да"]:
            print(f"Подсказка: Правильный ответ - {levels[level]['correct_answer']}.")
            hints_available -= 1

    while True:
        try:
            answer_index = int(input("Выберите номер двери (1-3): "))
            if answer_index < 1 or answer_index > 3:
                print("Пожалуйста, введите номер от 1 до 3.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    player_answer = str(answer_index)

    if player_answer == levels[level]["correct_answer"]:
        print("Правильный выбор! Вы можете перейти к следующему уровню.")
        return True, hints_available
    else:
        print("Неправильный выбор.")
        return False, hints_available

def play_bonus_level():
    bonus_question = random.choice(bonus_questions)
    print(f"\nБонусный уровень: {bonus_question['question']}")
    options = bonus_question["options"]

    for option in options:
        print(option)

    while True:
        try:
            answer_index = int(input("Выберите номер ответа (1-3): "))
            if answer_index < 1 or answer_index > 3:
                print("Пожалуйста, введите номер от 1 до 3.")
                continue
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    player_answer = str(answer_index)

    return player_answer == bonus_question["correct_answer"]

def main():
    print("Добро пожаловать в игру 'Выбери дверь'. Тут вам предстоит выбрать дверь с правильным ответом на вопрос. Также в игре есть бонусный уровень, за прохождение которого вы получаете подсказку на любой интересующий вас вопрос.")
    
    attempts = 1
    hints_available = 0
    bonus_count = 0
    last_bonused = False

    while attempts > 0:

        random_levels = random.sample(range(len(levels)), len(levels))

        for level in random_levels:

            if (bonus_count < 3 and not last_bonused and random.randint(0, 5) == 0):
                if level > 0:
                    last_bonused = True 
                    print("Вы нашли бонусную дверь!")
                    skip_bonus = input("Хотите пройти бонусный уровень? (да/нет): ").strip().lower()
                    if skip_bonus in ["да"]:
                        if play_bonus_level():
                            hints_available += 1
                            print(f"Вы получили подсказку! У вас теперь есть {hints_available} подсказок.")
                        else:
                            print("Вы проиграли в бонусном уровне. Игра продолжается.")
                    else:
                        print("Вы пропустили бонусный уровень.")
                    continue
            else:
                last_bonused = False

            success, hints_available = play_level(level, hints_available)
            if not success:
                print("Вы выбрали неправильную дверь. Игра окончена!")
                return

        attempts -= 1
        print("Поздравляем! Вы успешно прошли все уровни.")
        break 

if __name__ == "__main__":
    main()
