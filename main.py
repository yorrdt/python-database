import os

from getkey import getkey, keys

from database import Database

commands_list = ["1. Добавить запись", "2. Редактировать запись", "3. Удалить запись", "4. Вывести записи",
                 "5. Фильтрация записей", "6. Справка", "7. Выход"]

filter_list = ["1. Номер записи", "2. Нефтепродукт", "3. Объем", "4. Объем поставок в год",
               "5. Годовое потребление", "6. Количество через 5 лет"]


def clear_console():
    if os.name == ("nt", "dos"):
        os.system("cls")
        return
    os.system("clear")


clear_console()

databaseObj = Database()
selectedItem = 0


def draw_menu(item):
    print("Меню: ")
    for i in range(0, len(commands_list)):
        if i == item:
            print(f"> {commands_list[i]}")
        else:
            print(f"{commands_list[i]}")
    print("\nДля перемещения по меню используйте клавиши UP и DOWN")
    print("Для выбора подходящего пункта меню нажмите клавишу ENTER")


def draw_filter_menu(item):
    print("|" + 30 * "-" + "| Фильтрация записей |" + 30 * "-" + "|")
    print("| " + "Выберите параметр фильтрации: \n")
    for i in range(0, len(filter_list)):
        if i == item:
            print(f"> {filter_list[i]}")
        else:
            print(f"{filter_list[i]}")
    print("\n|\n| Для перемещения по меню используйте клавиши UP и DOWN")
    print("| Для выбора подходящего пункта меню нажмите клавишу ENTER")
    print("|" + 82 * "-" + "|")


def on_press_down():
    global selectedItem
    clear_console()
    if selectedItem < len(commands_list) - 1:
        selectedItem += 1
    draw_menu(selectedItem)


def on_press_up():
    global selectedItem
    clear_console()
    if selectedItem > 0:
        selectedItem -= 1
    draw_menu(selectedItem)


filterSelectedItem = 0


def on_press_down_filter():
    global filterSelectedItem
    clear_console()
    if filterSelectedItem < len(filter_list) - 1:
        filterSelectedItem += 1
    draw_filter_menu(filterSelectedItem)


def on_press_up_filter():
    global filterSelectedItem
    clear_console()
    if filterSelectedItem > 0:
        filterSelectedItem -= 1
    draw_filter_menu(filterSelectedItem)


def wait_press(pressed_key):
    key = getkey()
    while key != pressed_key:
        key = getkey()


def show_intro_screen():
    print("|" + 27 * "-" + "| Информационная заставка |" + 28 * "-" + "|")
    print("|" + " ".center(82) + "|")
    print("| " + "\"База данных автоматизации учёта и прогноза запасов нефтепродуктов,".center(80) + " |")
    print("| " + "реализуемых нефтебазой\"".center(80) + " |")
    print("|" + " ".center(82) + "|")
    print("|" + "Разработчик: Мороз Егор Владимирович".center(82) + "|")

    # something

    print("|" + 21 * "-" + "[ Нажмите ENTER для начала работы с БД ]".center(40) + 21 * "-" + "|")
    wait_press(keys.ENTER)
    clear_console()
    draw_menu(0)


show_intro_screen()


def filter_conditions(selectedItem):
    clear_console()
    print(selectedItem)
    global filterSelectedItem
    filterSelectedItem = 0


def menu_conditions(menu_item):

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

        print("|" + 80 * "-" + "|")

        print("| " + "ID".center(4) + " | "
              + "Нефтепродукт".center(12) + " | "
              + "Объём".center(10) + " | "
              + "Объём поставок".center(14) + " | "
              + "Годовое".center(11) + " | "
              + "Кол-во через".center(12) + " |")
        print("| " + 4 * " " + " | "
              + 12 * " " + " | "
              + 10 * " " + " | "
              + "в год".center(14) + " | "
              + "потребление".center(11) + " | "
              + "5 лет".center(12) + " |")

        print("|" + 80 * "-" + "|")

        entries = databaseObj.getEntries
        for i in range(0, len(entries)):
            print(f"| {entries[i][0]:<4}", end=" | ")
            print(f"{entries[i][1]:<12}", end=" | ")
            print(f"{entries[i][2]:<10}", end=" | ")
            print(f"{entries[i][3]:<14}", end=" | ")
            print(f"{entries[i][4]:<11}", end=" | ")
            print(f"{entries[i][5]:<12}", end=" |\n")

        print("|" + 80 * "-" + "|")

    elif menu_item == 4:

        draw_filter_menu(0)

        filter_key = keys.L
        while filter_key != keys.ENTER:
            filter_key = getkey()
            if filter_key == keys.DOWN:
                on_press_down_filter()
            elif filter_key == keys.UP:
                on_press_up_filter()

        filter_conditions(filterSelectedItem)

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

    clear_console()
    menu_conditions(selectedItem)
    selectedItem = 0
    print("\nНажмите клавишу ESC для перехода на главное меню")
    wait_press(keys.ESC)
    clear_console()
    draw_menu(0)








