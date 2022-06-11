from dbfile import dbFile


class Database:

    def __init__(self):
        self.__file = dbFile()
        fileData = self.__file.getData()
        self.__entryID = fileData[0]
        self.__databaseList = fileData[1]

    def addEntry(self, fuelType, volume, deliveryVolume,  annualConsumption, volumeIn5Years):
        self.__entryID += 1
        databaseItem = [
            str(self.__entryID),
            fuelType,
            str(volume),
            str(deliveryVolume),
            str(annualConsumption),
            str(volumeIn5Years)
        ]
        self.__databaseList.append(databaseItem)
        self.__file.appendData(databaseItem)

    @property
    def getEntries(self):
        return self.__databaseList

    def deleteEntry(self, number):
        isFound = False
        for item in self.__databaseList:
            if item[0] == str(number):
                self.__databaseList.remove(item)
                isFound = True

        if isFound is False:
            print("|\n| Запись не найдена!")
            return

        self.__file.writeData(self.__databaseList)
        print("|\n| Запись с номером", number, "удалена успешно!")

    def editEntry(self, number):
        isFound = False
        for item in self.__databaseList:
            if item[0] == str(number):
                item[1] = str(input("| Тип топлива: "))
                item[2] = int(input("| Объём: "))
                item[3] = int(input("| Объём поставок в год: "))
                item[4] = int(input("| Годовое потребление: "))
                item[5] = item[2] + (item[3] - item[4]) * 5
                if item[5] < 0:
                    item[5] = "меньше нуля"
                isFound = True

        if isFound is False:
            print("|\n| Запись не найдена!")
            return

        self.__file.writeData(self.__databaseList)
        print("|\n| Запись с номером", number, "отредактирована успешно!")
















