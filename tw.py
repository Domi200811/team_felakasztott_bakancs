import json
import time
import sys
import itertools
import os


# ---------------------
# Utility effektek
# ---------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def dramatic_pause(sec=1):
    time.sleep(sec)


def countdown():
    for i in range(3, 0, -1):
        print(f"Eredmények betöltése {i}...")
        time.sleep(0.7)
    clear()


def loading_animation(text="Mentés", duration=2):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write("\r" + text + " " + next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + text + " kész!      \n")


def flashing_title(text, flashes=3):
    for _ in range(flashes):
        print(text)
        time.sleep(0.3)
        clear()
        time.sleep(0.2)
    print(text)


# ---------------------
# Scoreboard
# ---------------------

def scoreboard(score):
    try:
        with open("scoreboard.json", "r") as f:
            scores = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []

    countdown()

    flashing_title("🏆 HIGH SCORE 🏆")

    print("=" * 35)
    print(f"{'Rank':<5} {'Name':<12} {'Score':<10}")
    print("-" * 35)

    medals = ["🥇", "🥈", "🥉"]

    for i, player in enumerate(scores[:10], start=1):
        time.sleep(0.2)
        medal = medals[i-1] if i <= 3 else ""
        print(f"{i:<5} {medal:<2} {player['name']:<12} {player['score']:<10}")

    print("=" * 35)

    qualifies = (len(scores) < 10) or (score < scores[9]["score"])

    if qualifies:
        dramatic_pause(1)
        typewriter(f"\n🎉 Gratulálok! {score} tippel Top 10-be kerültél!", 0.03)

        name = input("Adj meg egy nevet vagy nyomj Entert: ").strip()

        if name:
            scores.append({"name": name, "score": score})
            scores.sort(key=lambda x: x["score"])
            scores = scores[:10]

            loading_animation()

            with open("scoreboard.json", "w") as f:
                json.dump(scores, f, indent=4)

            position = next(i for i, p in enumerate(scores) if p["name"] == name and p["score"] == score)

            dramatic_pause(0.5)

            if position == 0:
                typewriter("\n🔥🔥 ÚJ REKORD!!! 🔥🔥", 0.05)
                for _ in range(3):
                    print("✨✨✨✨✨✨✨✨✨✨")
                    time.sleep(0.2)
            elif position < 3:
                typewriter("\n🔥 Dobogós helyezés! 🔥", 0.04)
            else:
                typewriter(f"\nA(z) {position+1}. helyre kerültél!", 0.03)

    else:
        dramatic_pause(1)
        typewriter(f"\n{score} tipp kellett... ez most nem volt elég a Top 10-hez.", 0.03)


scoreboard(input())