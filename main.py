import os
import keyboard
from database import Database

commands_list = ["1. Добавить запись", "2. Редактировать запись",
                 "3. Удалить запись", "4. Вывести записи",
                 "5. Фильтрация записей", "6. Справка", "7. Выход"]


def clearConsole():
    if os.name == ("nt", "dos"):
        os.system("cls")
        return
    os.system("clear")


clearConsole()

databaseObj = Database()
selectedItem = 0

print(f"Привет, {os.getlogin()}. Добро пожаловать в базу данных!")


def drawMenu(item):
    print("Меню: ")
    for i in range(0, len(commands_list)):
        if i == item:
            print(f"> {commands_list[i]}")
        else:
            print(f"{commands_list[i]}")
    print("\nДля перемещения по меню используйте клавиши up и down")
    print("Для выбора подходящего пункта меню нажмите клавишу right")

drawMenu(0)


def on_release_down(e):
    global selectedItem
    clearConsole()
    if selectedItem < len(commands_list) - 1:
        selectedItem += 1
    drawMenu(selectedItem)


def on_release_up(e):
    global selectedItem
    clearConsole()
    if selectedItem > 0:
        selectedItem -= 1
    drawMenu(selectedItem)


def menuConditions(menu_item):

    if menu_item == 0:
        print("|" + 28 * "-" + "| Добавление новой записи |" + 27 * "-" + "|")

        fuelType = input("| Тип топлива: ")
        volume = int(input("| Объём: "))
        deliveryVolume = int(input("| Объём поставок в год: "))
        annualConsumption = int(input("| Годовое потребление: "))
        volumeIn5Years = volume + (deliveryVolume - annualConsumption) * 5
        if volumeIn5Years < 0:
            volumeIn5Years = "меньше нуля"

        databaseObj.addEntry(fuelType, volume, deliveryVolume, annualConsumption, volumeIn5Years)

        print("|" + 82 * "-" + "|")

    elif menu_item == 1:
        print("edit")
    elif menu_item == 2:
        print("|" + 32 * "-" + "| Удаление записи |" + 31 * "-" + "|")
        print("|" + 82 * "-" + "|")

    elif menu_item == 3:

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

    elif menu_item == 4:
        print("filter")
    elif menu_item == 5:
        print("help")
    elif menu_item == 6:
        print("quit")
        exit(0)
    else:
        print("Wrong input!")


keyboard.on_release_key("down", callback=on_release_down)
keyboard.on_release_key("up", callback=on_release_up)

while True:
    keyboard.wait("right")
    clearConsole()
    menuConditions(selectedItem)
    selectedItem = 0
    print("Нажмите клавишу esc (или клавиши up или down) для перехода на главное меню")
    keyboard.wait("esc")
    clearConsole()
    drawMenu(0)







