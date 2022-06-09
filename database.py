from dbfile import dbFile


class Database:

    def __init__(self):
        self.__file = dbFile()
        fileData = self.__file.getData()
        self.__entryID = fileData[0]
        self.__databaseList = fileData[1]
        print("Database created!")

    def addEntry(self, fuelType, volume, deliveryVolume,  annualConsumption):
        self.__entryID += 1
        databaseItem = [
            str(self.__entryID),
            fuelType,
            str(volume),
            str(deliveryVolume),
            str(annualConsumption)
        ]
        self.__databaseList.append(databaseItem)
        self.__file.appendData(databaseItem)

    def printEntries(self):
        for item in self.__databaseList:
            print(item)

    def deleteEntry(self, number):
        isFound = False
        for item in self.__databaseList:
            if item[0] == str(number):
                self.__databaseList.remove(item)
                isFound = True

        if isFound is False:
            print("Entry not found!")
            return

        self.__file.writeData(self.__databaseList)
        print("deleteEntry")

    def editEntry(self, number):
        pass
















