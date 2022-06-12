import os
from getkey import getkey, keys
from database import Database

commands_list = ["1. Добавить запись", "2. Редактировать запись", "3. Удалить запись",
                 "4. Вывести записи", "5. Фильтрация записей", "6. Выход"]

filter_list = ["1. Номер записи", "2. Нефтепродукт", "3. Объем", "4. Объем поставок в год",
               "5. Годовое потребление", "6. Количество через 5 лет"]


def clear_console():
    if os.name == ("nt", "dos"):
        os.system("cls")
        return
    os.system("clear")


clear_console()
databaseObj = Database()


def print_menu_with_selected_item(item, out_list):
    print("Меню: ")
    for i in range(0, len(out_list)):
        if i == item:
            print(f"> {out_list[i]}")
        else:
            print(f"{out_list[i]}")


def draw_filter_menu(item):
    print("|" + 30 * "-" + "| Фильтрация записей |" + 30 * "-" + "|")
    print("| " + "Выберите параметр фильтрации: \n")
    print_menu_with_selected_item(item, filter_list)
    print("\n|" + 82 * "-" + "|")


selectedItem = 0


def on_press_down():
    global selectedItem
    clear_console()
    if selectedItem < len(commands_list) - 1:
        selectedItem += 1
    print_menu_with_selected_item(selectedItem, commands_list)


def on_press_up():
    global selectedItem
    clear_console()
    if selectedItem > 0:
        selectedItem -= 1
    print_menu_with_selected_item(selectedItem, commands_list)


filterSelectedItem = 0


def on_press_down_filter():
    global filterSelectedItem
    clear_console()
    if filterSelectedItem < len(filter_list) - 1:
        filterSelectedItem += 1
    print_menu_with_selected_item(filterSelectedItem, filter_list)


def on_press_up_filter():
    global filterSelectedItem
    clear_console()
    if filterSelectedItem > 0:
        filterSelectedItem -= 1
    print_menu_with_selected_item(filterSelectedItem, filter_list)


def wait_press(pressed_key):
    k = getkey()
    while k != pressed_key:
        k = getkey()


def show_intro_screen():
    print("|" + 27 * "-" + "| Информационная заставка |" + 28 * "-" + "|")
    print("|" + " ".center(82) + "|")
    print("| " + "\"База данных автоматизации учёта и прогноза запасов нефтепродуктов,".center(80) + " |")
    print("| " + "реализуемых нефтебазой\"".center(80) + " |")
    print("|" + " ".center(82) + "|")
    print("|" + "Разработчик: Мороз Егор Владимирович".center(82) + "|")
    print("|" + " ".center(82) + "|")
    print("|" + 24 * "-" + "| Справка по работе с программой |" + 24 * "-" + "|")
    print("|" + " ".center(82) + "|")
    print("| 1. Для перемещения по меню используйте клавиши UP и DOWN, для выбора пункта меню |")
    print("|" + 4 * " " + "нажмите клавишу ENTER.".ljust(78) + "|")
    print("| 2. Для добавления данных в базу данных выберите пункт меню \"Добавить запись\" и" + 3 * " " + "|")
    print("|" + 4 * " " + "введите необходимые данные.".ljust(78) + "|")
    print("|" + " 3. Для редактирования данных выберите пункт меню \"Редактировать запись\"," + 9 * " " + "|")
    print("|" + 4 * " " + "введите номер записи и новые данные для записи.".ljust(78) + "|")
    print("|" + " 4. Для удаления записи из базы данных выберите пункт меню \"Удалить запись\" и" + 5 * " " + "|")
    print("|" + 4 * " " + "введите номер записи.".ljust(78) + "|")
    print("|" + " 5. Чтобы вывести все записи на экран выберите пункт меню \"Вывести записи\"." + 7 * " " + "|")
    print("|" + " 6. Для фильтрации данных выберите пункт меню \"Фильтрация записей\". Далее" + 9 * " " + "|")
    print("|" + 4 * " " + "выберите параметр фильтрации и введите данные для выполнения операции." + 8 * " " + "|")
    print("|" + " 7. Для завершения работы выберите пункт меню \"Выход\".".ljust(82) + "|")
    print("|" + " ".center(82) + "|")
    print("|" + 16 * "-" + "[ Нажмите ENTER для начала работы с Базой Данных ]" + 16 * "-" + "|")
    wait_press(keys.ENTER)
    clear_console()
    print_menu_with_selected_item(0, commands_list)


show_intro_screen()


def show_table_head():
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


def print_entry_data(entries_list, num):
    print(f"| {entries_list[num][0]:<4}", end=" | ")
    print(f"{entries_list[num][1]:<12}", end=" | ")
    print(f"{entries_list[num][2]:<10}", end=" | ")
    print(f"{entries_list[num][3]:<14}", end=" | ")
    print(f"{entries_list[num][4]:<11}", end=" | ")
    print(f"{entries_list[num][5]:<12}", end=" |\n")


def filtering_by_number(num):
    minValue = int(input("| Введите минимальную границу фильтрации: "))
    maxValue = int(input("| Введите максимальную границу фильтрации: "))
    isFound = False

    entries = databaseObj.getEntries
    for i in range(0, len(entries)):
        if minValue <= int(entries[i][num]) <= maxValue:
            if isFound is False:
                show_table_head()
            isFound = True
            print_entry_data(entries, i)

    if isFound is False:
        print("|\n| Ни одной записи для фильтрации не найдено")


def filtering_by_string(value, num):
    isFound = False

    entries = databaseObj.getEntries
    for i in range(0, len(entries)):
        if value == entries[i][num]:
            if isFound is False:
                show_table_head()
            isFound = True
            print_entry_data(entries, i)

    if isFound is False:
        print("|\n| Ни одной записи для фильтрации не найдено")


def filter_conditions(menu_item):
    clear_console()
    global filterSelectedItem
    filterSelectedItem = 0

    print("|" + 29 * "-" + "| Фильтрация записей |" + 29 * "-" + "|")
    print(f"|\n| Параметр фильтрации: {filter_list[menu_item][3:len(filter_list[menu_item])]}", end="\n|\n")

    if menu_item == 0 or 2 <= menu_item <= 5:
        filtering_by_number(menu_item)

    elif menu_item == 1:
        value = str(input("| Введите название нефтепродукта: "))
        filtering_by_string(value, menu_item)

    print("|" + 80 * "-" + "|")


def keys_check(on_press_down_func, on_press_up_func):
    key = keys.L
    while key != keys.ENTER:
        key = getkey()
        if key == keys.DOWN:
            on_press_down_func()
        elif key == keys.UP:
            on_press_up_func()


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

        show_table_head()

        entries = databaseObj.getEntries
        for i in range(0, len(entries)):
            print_entry_data(entries, i)

        print("|" + 80 * "-" + "|")

    elif menu_item == 4:

        draw_filter_menu(0)
        keys_check(on_press_down_filter, on_press_up_filter)
        filter_conditions(filterSelectedItem)

    elif menu_item == 5:
        exit(0)


while True:

    keys_check(on_press_down, on_press_up)
    clear_console()
    menu_conditions(selectedItem)
    selectedItem = 0
    print("\nНажмите клавишу ESC для перехода на главное меню")
    wait_press(keys.ESC)
    clear_console()
    print_menu_with_selected_item(0, commands_list)








