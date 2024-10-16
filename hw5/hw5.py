import logic
from decouple import config


while True:
    total = int(config("MY_MONEY"))

    while total > 0:
        your_sum = int(input("Enter your sum: "))

        if your_sum > total:
            print(f"Your total is {total}, please lesser.")
            continue

        your_number = input("Guess a number: ")

        if your_number == logic.win_number:
            total += your_sum * 2
            print(f"You win {your_sum * 2}")
        else:
            total -= your_sum
            print("You lose :(")

        play_again = input("Do you want to play again? (Yes/No): ").capitalize()

        if play_again == "Yes":
            continue
        elif play_again == "No":
            print(f"Your total: {total}")
            total = 0
            break
        else:
            print("Invalid Error. Yes or No?")
            continue

    if total <= 0:
        print("Game End!")
        break