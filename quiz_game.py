import random
import time

print("==========================================")
print("               QUIZ GAME ")
print("==========================================")

name = input("Podaj swoje immię: ")
score = 0

questions_easy = [
    ("Ile to 2+2?", "4"),
    ("Stolica Polski?", "warszawa"),
    ("Ile dni ma tydzień?", "7"),
    ("Jakiego koloru jest trawa?", "zielony"),
    ("Ile to 10-5?", "5")
]

questions_hard = [
    ("Ile to 15*3?", "45"),
    ("Jak nazywa się język programowania którego się uczysz?", "python"),
    ("Co oznacza HTML?", "hypertext markup language"),
    ("Jak nazywa się funkcja do wyświetlania tekstu w Pythonie?", "print"),
    ("Jak nazywa się pętla która działa dopóki warunek jest prawdziwy?", "while")
]

print("\nWybierz poziom trudności:")
print("1 - łatwy")
print("2 - trudny")

level = input("Twój wybór: ")

if level == "1":
    questions = questions_easy
    level_name = "łatwy"
elif level == "2":
    questions = questions_hard
    level_name = "trudny"
else:
    print("Nieznany wybór, ustawiam poziom łatwy.")
    questions = questions_easy
    level_name = "łatwy"

random.shuffle(questions)

print("\nUruchamianie quizu...")
for i in range(0, 101, 25):
    print("Ładowanie:", i, "%")
    time.sleep(0.4)

question_number = 1
total_questions = len(questions)

for q, a in questions:
    print("\n-----------------------------")
    print("Pytanie", question_number, "z", total_questions)
    print(q)

    user = input("Twoja odpowieź: ").lower().strip()

    if user == a:
        print("Dobrze!")
        score += 1

    else:
        print("źle! Poprawna odpowiedź to:", a)

    question_number += 1
    time.sleep(0.5)

print("\n=======================================")
print("            KONIEC QUIZU")
print("=========================================")
print("Gracz:", name)
print("Poziom:", level_name)
print("Wynik:", score, "/", total_questions)

percent = int((score / total_questions) * 100)
print("Procent poprawnych odpowiedzi:", percent, "%")

if percent == 100:
    print("Perfekcyjnie! Jestes mistrzem quizu")
elif percent >= 70:
    print("Bardzo dobrze!")
elif percent >= 40:
    print("Nieźle, ale można lepiej")
else:
    print("ćwicz dalej, będzie coraz lepiej")

with open("wyniki_quiz.txt", "a") as file:
    file.write(f"Gracz: {name} | Poziom: {level_name} | Wynik: {score}/{total_questions} | {percent}%\n")

print("\nWynik został zapisany do pliku wyniki_quiz.txt")
print("Dziękuję za grę!")

