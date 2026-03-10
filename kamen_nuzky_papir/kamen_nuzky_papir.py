import random

choices = ["kamen", "nuzky", "papir"]

while True:
    player = input("Vyber kamen, nuzky, papir (nebo napis konec): ").lower()

    if player == "konec":
        print("Konec hry.")
        break

    computer = random.choice(choices)

    print("Počítač vybral:", computer)

    if player == computer:
        print("Remíza")
    elif player == "kamen" and computer == "nuzky":
        print("Vyhrál jsi!")
    elif player == "nuzky" and computer == "papir":
        print("Vyhrál jsi!")
    elif player == "papir" and computer == "kamen":
        print("Vyhrál jsi!")
    else:
        print("Prohrál jsi!")

    print()  # prázdný řádek&