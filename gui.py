import tkinter as tk
from tkinter import ttk
from tkinter import Checkbutton

def createWindow(db):

    window = tk.Tk()

    window.title("Python database")
    window.geometry("800x600")
    window.resizable(False, False)

    tabControl = ttk.Notebook(window)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Database")
    tabControl.add(tab2, text="Add entry")

    drawTable(tab1, db)
    addEntry(tab2)

    tabControl.pack(expand=1, fill="both")

    window.mainloop()


def addEntry(root):

    entryData = []

    frame = tk.Frame(master=root, pady=16)
    frame.pack()

    # fuel type field
    label_fuel_type = tk.Label(master=frame, text="Fuel type: ")
    entry_fuel_type_field = tk.StringVar()
    entry_fuel_type = tk.Entry(master=frame, textvariable=entry_fuel_type_field)

    label_fuel_type.grid(row=0, column=0, sticky="w")
    entry_fuel_type.grid(row=0, column=1, pady=2, padx=8)

    # volume field
    label_volume = tk.Label(master=frame, text="Volume: ")
    entry_volume_field = tk.StringVar()
    entry_volume = tk.Entry(master=frame, textvariable=entry_volume_field)

    label_volume.grid(row=1, column=0, sticky="w")
    entry_volume.grid(row=1, column=1, pady=2, padx=8)

    # delivery volume field
    label_delivery_volume = tk.Label(master=frame, text="Delivery volume: ")
    entry_delivery_volume_field = tk.StringVar()
    entry_delivery_volume = tk.Entry(master=frame, textvariable=entry_delivery_volume_field)

    label_delivery_volume.grid(row=2, column=0, sticky="w")
    entry_delivery_volume.grid(row=2, column=1, pady=2, padx=8)

    # annual consumption field
    label_annual_consumption = tk.Label(master=frame, text="Annual consumption: ")
    entry_annual_consumption_field = tk.StringVar()
    entry_annual_consumption = tk.Entry(master=frame, textvariable=entry_annual_consumption_field)

    label_annual_consumption.grid(row=3, column=0, sticky="w")
    entry_annual_consumption.grid(row=3, column=1, pady=2, padx=8)

    button = tk.Button(master=frame, text="Add entry")
    button.grid(pady=16, columnspan=2)


def drawTable(root, db):

    tableHead = ["options", "id", "fuel_type", "volume", "delivery_volume", "annual_consumption"]

    frame = tk.Frame(master=root, pady=16)
    frame.pack(fill=tk.BOTH)

    tableFrame = tk.Frame(master=frame, relief=tk.SUNKEN, borderwidth=1)
    tableFrame.grid()

    for i, table in enumerate(tableHead):
        label = tk.Label(master=tableFrame, text=table, relief=tk.RAISED, borderwidth=1)
        label.grid(row=0, column=i)

    for i in range(0, 5):
        optionsFrame = tk.Frame(master=tableFrame, relief=tk.RAISED, borderwidth=1)
        optionsFrame.grid(row=1, column=0)

        checkBox = Checkbutton(master=optionsFrame)
        editButton = tk.Button(master=optionsFrame, text="Edit", relief=tk.FLAT)
        deleteButton = tk.Button(master=optionsFrame, text="Delete", relief=tk.FLAT)
        checkBox.grid(row=0, column=0)
        editButton.grid(row=0, column=1)
        deleteButton.grid(row=0, column=2)

    """
    optionsFrame = tk.Frame(master=frame, relief=tk.RAISED, borderwidth=1)
    optionsFrame.grid(row=1, column=0)

    checkBox = Checkbutton(master=optionsFrame)
    editButton = tk.Button(master=optionsFrame, text="Edit", relief=tk.FLAT)
    deleteButton = tk.Button(master=optionsFrame, text="Delete", relief=tk.FLAT)
    checkBox.grid(row=0, column=0)
    editButton.grid(row=0, column=1)
    deleteButton.grid(row=0, column=2)

    entryFrame = tk.Frame(master=frame, relief=tk.RAISED, borderwidth=1)
    entryFrame.grid(row=1, column=1)

    fuelTypeLabel = tk.Label(master=entryFrame, text="Oil")
    fuelTypeLabel.grid(row=1, column=1)
    """

