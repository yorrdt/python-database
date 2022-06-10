import tkinter as tk
from database import Database
from tkinter import ttk
from tkinter import Checkbutton

databaseObj = Database()


def createWindow():

    window = tk.Tk()

    window.title("Python database")
    window.geometry("768x600")
    window.resizable(False, False)

    tabControl = ttk.Notebook(window)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Database")
    tabControl.add(tab2, text="Add entry")

    addEntry(window, tab2)

    tabControl.pack(expand=1, fill="both")

    def onTabChange(event):
        tab = event.widget.tab("current")["text"]
        if tab == "Database":
            print("tab1")
            drawTable(window, tab1)
        elif tab == "Add entry":
            print("tab2")


    tabControl.bind("<<NotebookTabChanged>>", onTabChange)

    window.mainloop()


def addEntry(window, root):

    def addEntryToDatabase():
        databaseObj.addEntry(
            entry_fuel_type.get(),
            entry_volume.get(),
            entry_delivery_volume.get(),
            entry_annual_consumption.get()
        )
        entry_fuel_type.delete(0, tk.END)
        entry_volume.delete(0, tk.END)
        entry_delivery_volume.delete(0, tk.END)
        entry_annual_consumption.delete(0, tk.END)
        entry_fuel_type.focus()
        print("Entry was successfully added!")

    frame = tk.Frame(master=root, pady=16)
    frame.pack()

    # fuel type field
    label_fuel_type = tk.Label(master=frame, text="Fuel type: ")
    entry_fuel_type = tk.Entry(master=frame)

    label_fuel_type.grid(row=0, column=0, sticky="w")
    entry_fuel_type.grid(row=0, column=1, pady=2, padx=8)

    # volume field
    label_volume = tk.Label(master=frame, text="Volume: ")
    entry_volume = tk.Entry(master=frame)

    label_volume.grid(row=1, column=0, sticky="w")
    entry_volume.grid(row=1, column=1, pady=2, padx=8)

    # delivery volume field
    label_delivery_volume = tk.Label(master=frame, text="Delivery volume: ")
    entry_delivery_volume = tk.Entry(master=frame)

    label_delivery_volume.grid(row=2, column=0, sticky="w")
    entry_delivery_volume.grid(row=2, column=1, pady=2, padx=8)

    # annual consumption field
    label_annual_consumption = tk.Label(master=frame, text="Annual consumption: ")
    entry_annual_consumption = tk.Entry(master=frame)

    label_annual_consumption.grid(row=3, column=0, sticky="w")
    entry_annual_consumption.grid(row=3, column=1, pady=2, padx=8)

    button = tk.Button(master=frame, text="Add entry", command=addEntryToDatabase)
    button.grid(pady=16, columnspan=2)


def drawTable(window, root):

    tableHead = [
        ["options", 20],
        ["id", 8],
        ["fuel_type", 12],
        ["volume", 20],
        ["delivery_volume", 20],
        ["annual_consumption", 20]
    ]
    checkBoxesValues = []

    entriesList = databaseObj.getEntries

    frame = tk.Frame(master=root, pady=16)
    frame.pack(fill=tk.BOTH)

    tableFrame = tk.Frame(master=frame, relief=tk.SUNKEN, borderwidth=1)
    tableFrame.grid()

    for i in range(0, len(tableHead)):
        label = tk.Label(master=tableFrame, text=tableHead[i][0], relief=tk.RAISED, borderwidth=1, width=tableHead[i][1])
        label.grid(row=0, column=i)

    for i in range(0, len(entriesList)):

        optionsFrame = tk.Frame(master=tableFrame)
        optionsFrame.grid(row=i+1, column=0)

        checkBoxValue = tk.IntVar()
        checkBox = Checkbutton(master=optionsFrame, variable=checkBoxValue)
        editButton = tk.Button(master=optionsFrame, text="Edit", relief=tk.FLAT)
        deleteButton = tk.Button(master=optionsFrame, text="Delete", relief=tk.FLAT)

        checkBox.grid(row=0, column=0)
        checkBoxesValues.append(checkBoxValue.get())

        editButton.grid(row=0, column=1)
        deleteButton.grid(row=0, column=2)

        for j in range(0, len(entriesList[0])):
            label = tk.Label(master=tableFrame, text=entriesList[i][j])
            label.grid(row=i + 1, column=j + 1)

