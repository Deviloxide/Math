import random

def effrons_dice(limit):
    dice_1 = [0, 0, 4, 4, 4, 4]
    dice_2 = [3, 3, 3, 3, 3, 3]
    dice_3 = [2, 2, 2, 2, 6, 6]
    dice_4 = [1, 1, 1, 5, 5, 5]

    print("The available dice are:")
    print("Dice a: [0, 0, 4, 4, 4, 4]")
    print("Dice b: [3, 3, 3, 3, 3, 3]")
    print("Dice c: [2, 2, 2, 2, 6, 6]")
    print("Dice d: [1, 1, 1, 5, 5, 5]" + "\n")

    user_choice = input("What dice do you choose? ")

    right = 0
    total = 0

    if user_choice == "a":
        print("The CPU chose to use dice d.")
        user = dice_1
        cpu = dice_4
    if user_choice == "b":
        print("The CPU chose to use dice a.")
        user = dice_2
        cpu = dice_1
    if user_choice == "c":
        print("The CPU chose to use dice b.")
        user = dice_3
        cpu = dice_2
    elif user_choice == "d":
        print("The CPU chose to use dice c.")
        user = dice_4
        cpu = dice_3

    for i in range(0,limit):
        num1 = random.randint(0, 5)
        num2 = random.randint(0, 5)
        if user[num1] > cpu[num2]:
            print(user[num1], " > ", cpu[num2])
            right += 1
            total += 1
        else:
            print(user[num1], " < ", cpu[num2])
            total += 1

    percent = (right * 100) / total

    return "You won {} out of {} ({}% win rate) ".format(right, total, percent)

print(effrons_dice(1000))
