import random

# Definice proměnných
tajne_cislo = random.randint(1, 100)
pokusy = 0
max_pokusu = 10
uhodnuto = False

print("Vítej ve hře Hádej číslo!")
print("Myslím si číslo mezi 1 a 100.")
print(f"Máš {max_pokusu} pokusů.\n")

# Základní cyklus
while pokusy < max_pokusu and not uhodnuto:

    tip = int(input("Zadej svůj tip: "))
    pokusy += 1

    # Podmínky if / else
    if tip == tajne_cislo:
        uhodnuto = True
        print(f"Správně! Uhodl jsi číslo za {pokusy} pokusů.")

    elif tip < tajne_cislo:
        print("Moc malé číslo!")

    else:
        print("Moc velké číslo!")

    print(f"Zbývající pokusy: {max_pokusu - pokusy}\n")

# Podmínka po skončení cyklu
if not uhodnuto:
    print(f"Prohrál jsi! Správné číslo bylo {tajne_cislo}.")
else:
    print("Vyhrál jsi!")

# Ukázka for cyklu
print("\nDěkujeme za hraní!")
for i in range(3):
    print("Ahoj!")