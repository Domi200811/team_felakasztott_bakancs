# import files such as random, countries and capitals and ascii arts
import random
from contry_and_capital_list import countries_and_capitals
from ascii import HANGMANPICS

# error counter méretének megadása
MAX_ERRORS = len(HANGMANPICS) - 1

# country and capital felbontása és random kiválasztása
def pick_random_pair(): 
    pairs = [line.strip().split("|") for line in countries_and_capitals()]
    country, capital = random.choice(pairs)
    return country.strip(), capital.strip()

# hiddenbe konvertálás
def mask_word(word, guessed):
    return "".join(ch if ch.lower() in guessed or ch == " " else "-" for ch in word)

# egy körnek a megfogalmazása
def play_one_round(secret_word, label): #secret word         
    guessed = set() # egy elem csak 1x szerepelhet benne, elmenti a már kérdezett betűket
    errors = 0

    while errors < MAX_ERRORS: # ha a hibák elérik a max errorst eltörik
        print("\n" + HANGMANPICS[errors])
        print(f"{label}: {mask_word(secret_word, guessed)}")
        print(f"Hibás betűk: {' '.join(sorted(guessed - set(secret_word.lower())))}")
        print(f"Maradt próbálkozás: {MAX_ERRORS - errors}")

        guess = input("Adj meg egy betűt: ").strip().lower() # több betűt nem fogad el
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Érvénytelen! - Csak egy betűt írj.")
            continue

        if guess in guessed:    # nem lehet egy betűt többször tippelni
            print("Már tippelted ezt a betűt.") 
            continue

        guessed.add(guess)

        if guess in secret_word.lower():
            if all(ch.lower() in guessed or ch == " " for ch in secret_word):
                print(f"\nGratulálok! Kitaláltad a(z) {label.lower()}: {secret_word}") 
                return True
        else:
            errors += 1
            print("Rossz betű!")

    print("\n" + HANGMANPICS[errors])
    print(f"Sajnos elvesztetted a játékot. A helyes {label.lower()}: {secret_word}")
    return False
 
 #a játék alapelvei
def main():
    print("Üdvözöllek a játékban!")
    while True:
        print("\nMit szeretnél kitalálni?") 
        print("[1] Ország")
        print("[2] Főváros")
        print("[Enter] Kilépés")
        choice = input().strip()

        if choice == "":
            break
        if choice not in {"1", "2"}:
            print("Érvénytelen választás.") # csak az 1-t és 2-t fogadja el válaszként
            continue

        country, capital = pick_random_pair()

        if choice == "1":
            play_one_round(country, "Ország")
        else:
            play_one_round(capital, "Főváros")

        again = input("\nJátszunk még egy körrel? (i/n): ").strip().lower()
        if again != "i":
            break

    print("\nKöszönjük a játékot!")

# replaying function
if __name__ == "__main__":
    main()                   