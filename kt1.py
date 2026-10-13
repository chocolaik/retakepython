count = 0
print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

while True:
    text = input()

    if text == "ПОКА":
        count += 1
    else:
        count = 0

        if text.islower():
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
        elif text.isupper():
            print("НЕТ, НИ РАЗУ С 1944 ГОДА!")

    if count == 3:
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break