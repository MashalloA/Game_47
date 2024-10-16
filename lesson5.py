import random
import json

# Чтение конфигурационного файла
def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

# Основная логика игры
def play_game(config):
    min_num = config['min_number']
    max_num = config['max_number']
    attempts = config['attempts']
    capital = config['initial_capital']

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас {capital} денег и {attempts} попыток угадать число от {min_num} до {max_num}.\n")

    target_number = random.randint(min_num, max_num)

    for i in range(attempts):
        if capital <= 0:
            print("У вас закончились деньги. Игра окончена!")
            break

        print(f"\nПопытка {i+1} из {attempts}. У вас {capital} денег.")
        try:
            bet = int(input(f"Введите вашу ставку (до {capital}): "))
            if bet > capital or bet <= 0:
                print("Неправильная ставка. Попробуйте снова.")
                continue

            guess = int(input(f"Введите ваше число от {min_num} до {max_num}: "))

            if guess == target_number:
                capital += bet  # Удваиваем ставку
                print(f"Поздравляем! Вы угадали! Теперь у вас {capital} денег.")
                break
            else:
                capital -= bet  # Теряем ставку
                print(f"Неверно! Вы теряете {bet}. У вас осталось {capital} денег.")
        except ValueError:
            print("Неправильный ввод. Введите число.")

    if capital > 0:
        print(f"\nИгра окончена! Ваш итоговый капитал: {capital}")
    else:
        print("\nК сожалению, вы потеряли все деньги.")

# Пример конфигурационного файла config.json:
# {
#     "min_number": 1,
#     "max_number": 10,
#     "attempts": 3,
#     "initial_capital": 100
# }

if __name__ == "__main__":
    config_path = 'config.json'  # Путь к конфигурационному файлу
    config = read_config(config_path)
    play_game(config)