from database import Database
from gui import createWindow

db = Database()
# db.addEntry("Oil", 156000, 25000, 6500)
# db.addEntry("Petrol", 258000, 48000, 12000)
# db.addEntry("Diesel", 189000, 34000, 17000)

db.printEntries()

createWindow()

