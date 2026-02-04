import random
from contry_and_capital_list import countries_and_capitals
from ascii import HANGMANPICS

MAX_ERRORS = len(HANGMANPICS) - 1

def pick_random_pair(): 
    pairs = [line.strip().split("|") for line in countries_and_capitals()]
    country, capital = random.choice(pairs)
    return country.strip(), capital.strip()

def mask_word(word, guessed):
    return "".join(ch if ch.lower() in guessed or ch == " " else "-" for ch in word)


def play_one_round(secret_word, label):         
    guessed = set()
    errors = 0

    while errors < MAX_ERRORS:
        print("\n" + HANGMANPICS[errors])
        print(f"{label}: {mask_word(secret_word, guessed)}")
        print(f"Hibás betűk: {' '.join(sorted(guessed - set(secret_word.lower())))}")
        print(f"Maradt próbálkozás: {MAX_ERRORS - errors}")

        guess = input("Adj meg egy betűt: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Érvénytelen! - Csak egy betűt írj.")
            continue

        if guess in guessed:
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
            print("Érvénytelen választás.")
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


if __name__ == "__main__":
    main()                   