import csv
import os


class dbFile:

    def __init__(self):

        self.__fileName = "database.csv"
        if not os.path.exists(self.__fileName):
            open(self.__fileName, "a").close()

    def getData(self):

        if os.stat(self.__fileName).st_size == 0:
            print("File is empty!")
            return [0, []]

        with open(self.__fileName, "r", newline="") as file:
            reader = csv.reader(file)
            countOfEntries = 0
            databaseList = []
            for row in reader:
                countOfEntries = int(row[0])
                databaseList.append(row)
            return [countOfEntries, databaseList]

    def writeData(self, databaseList):
        with open(self.__fileName, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(databaseList)

    def appendData(self, databaseItem):
        with open(self.__fileName, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(databaseItem)

