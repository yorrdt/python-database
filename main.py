import os

from getkey import getkey, keys

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

def drawMenu(item):
    print("Меню: ")
    for i in range(0, len(commands_list)):
        if i == item:
            print(f"> {commands_list[i]}")
        else:
            print(f"{commands_list[i]}")
    print("\nДля перемещения по меню используйте клавиши UP и DOWN")
    print("Для выбора подходящего пункта меню нажмите клавишу ENTER")


def on_press_down():
    global selectedItem
    clearConsole()
    if selectedItem < len(commands_list) - 1:
        selectedItem += 1
    drawMenu(selectedItem)


def on_press_up():
    global selectedItem
    clearConsole()
    if selectedItem > 0:
        selectedItem -= 1
    drawMenu(selectedItem)


def wait_press(pressed_key):
    key = getkey()
    while key != pressed_key:
        key = getkey()


def showIntroScreen():
    print("|" + 27 * "-" + "| Информационная заставка |" + 28 * "-" + "|")
    print("|" + " ".center(82) + "|")
    print("| " + "\"База данных автоматизации учёта и прогноза запасов нефтепродуктов,".center(80) + " |")
    print("| " + "реализуемых нефтебазой\"".center(80) + " |")
    print("|" + " ".center(82) + "|")
    print("|" + "Разработчик: Мороз Егор Владимирович".center(82) + "|")


    print("|" + 21 * "-" + "[ Нажмите ENTER для начала работы с БД ]".center(40) + 21 * "-" + "|")
    wait_press(keys.ENTER)
    clearConsole()
    drawMenu(0)


showIntroScreen()


def menuConditions(menu_item):

    if menu_item == 0:
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

    elif menu_item == 1:
        print("|" + 28 * "-" + "| Редактирование записи |" + 27 * "-" + "|")

        numberOfItem = int(input("| Введите номер записи, которую вы хотите отредактировать: "))
        databaseObj.editEntry(numberOfItem)

        print("|" + 82 * "-" + "|")

    elif menu_item == 2:
        print("|" + 32 * "-" + "| Удаление записи |" + 31 * "-" + "|")

        numberOfItem = int(input("| Введите номер записи, которую вы хотите удалить: "))
        databaseObj.deleteEntry(numberOfItem)

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
        exit(0)
    else:
        print("Wrong input!")


while True:

    key = keys.L
    while key != keys.ENTER:
        key = getkey()
        if key == keys.DOWN:
            on_press_down()
        elif key == keys.UP:
            on_press_up()

    clearConsole()
    menuConditions(selectedItem)
    selectedItem = 0
    print("\nНажмите клавишу ESC для перехода на главное меню")
    wait_press(keys.ESC)
    clearConsole()
    drawMenu(0)








