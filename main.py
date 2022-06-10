import os
from database import Database

commands_list = [
    ["a", "добавить запись"],
    ["e", "редактировать запись"],
    ["d", "удалить запись"],
    ["p", "вывести записи"],
    ["f", "фильтрация записей"],
    ["h", "справка"],
    ["q", "выход"]
]

os.system("clear")

print(f"Привет, {os.getlogin()}. Добро пожаловать в базу данных!")

databaseObj = Database()

while True:
    print("Меню:")
    for i in range(0, len(commands_list)):
        print(f"\'{commands_list[i][0]}\' - {commands_list[i][1]}")

    command = input("> ")
    os.system("clear")
    if command == commands_list[0][0]:
        print("|" + 28 * "-" + "| Добавление новой записи |" + 27 * "-" + "|")

        fuelType = str(input("| Тип топлива: "))
        volume = int(input("| Объём: "))
        deliveryVolume = int(input("| Объём поставок в год: "))
        annualConsumption = int(input("| Годовое потребление: "))
        volumeIn5Years = volume + (deliveryVolume - annualConsumption) * 5
        if volumeIn5Years < 0:
            volumeIn5Years = "меньше нуля"

        databaseObj.addEntry(fuelType, volume, deliveryVolume, annualConsumption, volumeIn5Years)

        print("|" + 82 * "-" + "|")

    elif command == commands_list[1][0]:
        print("edit")
    elif command == commands_list[2][0]:
        print("delete")
    elif command == commands_list[3][0]:

        print("|" + 82 * "-" + "|")

        print("| " + "ID".center(4) + " | "
              + "Нефтепродукт".center(12) + " | "
              + "Объём".center(10) + " | "
              + "Объём поставок".center(14) + " | "
              + "Годовое".center(11) + " | "
              + "Кол-во через".center(14) + " |")
        print("| " + 4 * " " + " | "
              + 12 * " " + " | "
              + 10 * " " + " | "
              + "в год".center(14) + " | "
              + "потребление".center(11) + " | "
              + "5 лет".center(14) + " |")

        print("|" + 82 * "-" + "|")

        entries = databaseObj.getEntries
        for i in range(0, len(entries)):
            print(f"| {entries[i][0]:<4}", end=" | ")
            print(f"{entries[i][1]:<12}", end=" | ")
            print(f"{entries[i][2]:<10}", end=" | ")
            print(f"{entries[i][3]:<14}", end=" | ")
            print(f"{entries[i][4]:<11}", end=" | ")
            print(f"{entries[i][5]:<14}", end=" |\n")

        print("|" + 82 * "-" + "|")

    elif command == commands_list[4][0]:
        print("filter")
    elif command == commands_list[5][0]:
        print("help")
    elif command == commands_list[6][0]:
        print("quit")
        exit(0)
    else:
        print("Wrong input!")



