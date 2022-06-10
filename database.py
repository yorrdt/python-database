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
            print("Entry not found!")
            return

        self.__file.writeData(self.__databaseList)
        print("deleteEntry")

    def editEntry(self, number):
        pass
















