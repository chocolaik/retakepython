from datetime import datetime

GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
END = "\033[0m"

today = datetime.today().date()

with open("tasks.txt", "r", encoding="utf-8") as file:
    tasks = file.readlines()

for task in tasks:
    task = task.strip()

    if not task:
        continue

    name, date_text = task.split(";")
    task_date = datetime.strptime(date_text, "%Y-%m-%d").date()

    if task_date < today:
        color = RED
        status = "Просрочена"
    elif task_date == today:
        color = GREEN
        status = "Текущая"
    else:
        color = BLUE
        status = "Будущая"

    print(color + name + " - " + status + END)
