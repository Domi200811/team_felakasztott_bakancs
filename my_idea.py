import random
from contry_and_capital_list import countries_and_capitals
from ascii import HANGMANPICS

MAX_ERRORS = len(HANGMANPICS) - 1   # Létrehoztam egy "MAX_ERRORS"-t, ami a "HANGMANPICS" hosszához van kötve, ezért szinkron lesz a hibák és az "ascii" art között.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Előszó: A módosítások az ÉN saját stílusomban van írva! Nyugodtan írjátok át, ha nem olyan erthető, vagy nem a te stílusotok.
# Megpróbáltam mindent minél jobban elmagyarázni, de ha van kérdésetek holnap elmondom szívesen, vagy Discordon online bármikor.
# Nagyjából szerintem megértettem, hogy mit szerettetek volna, és annyit nem is kellet módosítani, inkább kiegészíteni.
# Próbáltam minél jobbat írni, de előre is bocsi, ha nem tetszik valami, nagyon fáradt vagyok.
# Azért remélem tudtam valamennyit segíteni, hogy időben készen legyetek.
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



#                                                                   A JÁTÉK KRITÉRIUMAI
#/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/

def pick_random_pair():        # Garantálja, hogy a country és a capital együtt marad, így elkerüli a nem kapcsolódó [Index](ek) választását. Egyszerűbben: nem szarik be.  
    pairs = [line.strip().split("|") for line in countries_and_capitals()]  # A [country | capital] pár elválasztása "|"(vonallal).
    country, capital = random.choice(pairs)      # Véletlenszerű country | capital
    return country.strip(), capital.strip()

# def hangmanci(city):
#     for i in city:
#         if i == ' ':
#             hidden1.append(' ')
#         else:
#             hidden1.append('-')
#     print(''.join(hidden1))
#     return city, city.count(' ')
#                                    Amúgy ez a két [def] nagyon szuperül meg lett csinálva [def hangmanci és hangmancu]. A+ effort
#                                    Nekem ez a módzser megy ezért használom a lentit, de ha nem tetszik akkor változtassatok.
# def hangmancu(country):
#     for i in country:
#         if i == ' ':
#             hidden2.append(' ')
#         else:
#             hidden2.append('-')
#     print(''.join(hidden2))
#     return country, country.count(' ')

#       |
#       |
#       V
# Kicsit átalakítottam, hogy minden körben lerakja a "-" (kötőjeleteket) és így nem fog kelleni az hidden1/2.
def mask_word(word, guessed):
    return "".join(ch if ch.lower() in guessed or ch == " " else "-" for ch in word) #ch = character


def play_one_round(secret_word, label):         
    guessed = set()
    errors = 0
#------->
    # A "Core" HANGMAN loop egyetlen "titkos" szora "kötve".
    # A "secret_word" a szó, amit a "player"-nek ki kell taláni. (country/capital)
    # A "Player"-nek megjelenő kis leírás (pl.: ország/város)


# while kitalalas:
#     guess = input('Adj meg 1db betűt!')
#     if guess in country:
#        
#     elif guess not in country:
#         hibas.append(guess)
#         print(f'{hibas}')
#        
#     hibapont == len(country) or hibapont == len(city)
#     kitalalas = False
#   |
#   |
#   |
#   V
#   Ezt is kicsit átírtam de nagyjából értem mire gondoltatok (remélem, sry fáradt vagyok)
    # Nézi(errors < MAX_ERRORS), hogy a "HANGMANPICS"-nél hány kép van még hátra és, ha kifogy akkor leáll a game.
    while errors < MAX_ERRORS:
        # Mutatja az aktuális képet és a rejtett szót.
        print("\n" + HANGMANPICS[errors])
        print(f"{label}: {mask_word(secret_word, guessed)}")
        print(f"Hibás betűk: {' '.join(sorted(guessed - set(secret_word.lower())))}") # Könnyebbé teszi a rossz betűk kiszámítását, és a "(guessed - set" megakadályozza a duplikált tippet
        print(f"Maradt próbálkozás: {MAX_ERRORS - errors}")     # Hót egyszerű számítás: A max elrontásból kivonjuk a rossz tippeket és annyi életed van basically 

        guess = input("Adj meg egy betűt: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():   # Lekezeltem az üres bemeneteket és a nem alfabetikus karaktereket (az utóbbi nem kötelező).
            print("Érvénytelen! - Csak egy betűt írj.")
            continue    # Continue return helyett.

        if guess in guessed:
            print("Már tippelted ezt a betűt.") # Mivel a "guessd" az [set] ezért, ha a "guess" benne van akkor már tippelte a "player".
            continue    # Continue return helyett.

        guessed.add(guess)

# for i in countries_and_capitals():
#         x, y = i.strip().split("|")
#         x=x.lstrip()
#         y=y.lstrip()
#         orszag.append(x)
#         capital.append(y)
# ran_country= random.randint(0, (len(orszag)))
# ran_capital= random.randint(0, (len(capital)))
#   |
#   |
#   |
#   V

# Ezt is kicsit módosítottam
        # A code ellenőrzi, ha a tipp felfedi-e az egész szót, majd ennek megfelelően 2 dolog történhet.
        if guess in secret_word.lower():
            if all(ch.lower() in guessed or ch == " " for ch in secret_word):
                print(f"\nGratulálok! Kitaláltad a(z) {label.lower()}: {secret_word}")     # Ha a kitalált betű kiegészíti a szót, a "player" megnyerte a kört.
                return True
        else:
            errors += 1
            print("Rossz betű!")    # Ha nem akkor + 1 wrong guess.

    # Ha elfogynak az életei a "player"-nek akkor az utolsó "HANGMANPICS".
    print("\n" + HANGMANPICS[errors])
    print(f"Sajnos elvesztetted a játékot. A helyes {label.lower()}: {secret_word}")    #Megmutatja a végső képet("HANGMANPICS"), és felfedi a helyes választ.
    return False                                                                        # + Egy végső üzenet, ami lezárja a köröket.



#                                                               MAIN GAME
#/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/---/

# Maga a "main def"-et elválasztottam a többitől és a végére raktam, hogy jobban látható legyen, de nem befojásolja a működést(nyilvánvalóan). 
def main():
    print("Üdvözöllek a játékban!")             # Dekorálni majd dekoráltok, azt majd tetszés szerint.
    while True:                                 # Alap eleje a programnak, innen indul.
        print("\nMit szeretnél kitalálni?")     # Megtartottam a kinézetüket, ez ismerős lehet. 
        print("[1] Ország")
        print("[2] Főváros")
        print("[Enter] Kilépés")
        choice = input().strip()    # Végül mégis kell strip(), my bad sry.

        if choice == "":            # Egyszerű lekezelés: Ha nem 1/2 akkor csak eltörik.
            break
        if choice not in {"1", "2"}:
            print("Érvénytelen választás.")
            continue

        country, capital = pick_random_pair()       # Meghívom a "pick_random_par()"-re a "country"-t és a "capital"-t.

        if choice == "1":
            play_one_round(country, "Ország")       # Alap logika: ha "1", akkor country-mód, ahogy ti is csináltátok.
        else:
            play_one_round(capital, "Főváros")      # Ha meg nem "1" akkor (nyilván "2") - "capital"-mód.

        # Mégegy kör lehetősége: Nem kötelező btw. (Ez még az enyémben sincs benne xd. Már jobbak vagytok)
        again = input("\nJátszunk még egy körrel? (i/n): ").strip().lower()
        if again != "i":
            break

    print("\nKöszönjük a játékot!")


if __name__ == "__main__":  # Basic formátum:
    main()                  # Ezt így kell hagyni különben nem fog működni!!!!!! 