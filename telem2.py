import csv  # Module to work with CSV files
import pandas as pd  # Data analysis and manipulation tool
import matplotlib.pyplot as plt  # Plotting library
import numpy as np  # Library for numerical computations
import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk
import tkinter.messagebox
from tkinter import *

def fileopener():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    
    if root.filename:  # Check if a file was selected
        file_name = root.filename.split('/')[-1]  # Extract the file name from the file path
        file_path.set(root.filename)  # Update the StringVar with the file path
        file_name_var.set(file_name)  # Update the StringVar with the file name

        # Reading the CSV file using the csv module
        file = open(root.filename)  # Open the CSV file in read mode
        csvreader = csv.reader(file)  # Create a csv reader object to read the file line by line
        header = next(csvreader)  # Retrieve the header (first line) from the file
        print(header)  # Print the header
        rows = []  # Initialize an empty list to store the rows
        for row in csvreader:  # Loop through each row in the file
            rows.append(row)  # Append
        print(rows)  # Print the rows

def csvtoexcel():
    csvDataframe = pd.read_csv(root.filename)  # Read the CSV file into a pandas DataFrame
    resultExcelfile = pd.ExcelWriter('test.xlsx')  # Create an Excel writer object
    csvDataframe.to_excel(resultExcelfile, index=False)  # Write the DataFrame to an Excel file
    resultExcelfile.close()  # Close the Excel writer object to save the data to the file

def Filenamepopup():
    tkinter.messagebox.showinfo("File Path", file_path.get())
#Create the Root Window
root = tk.Tk()
root.geometry("800x600")
root.maxsize(1920, 1080)
root.title("Telemetry Viewer")

# Create StringVar variables to hold the file path and name
file_path = tk.StringVar()
file_name_var = tk.StringVar()

# Creates a main menu
main_menu = tk.Menu(root)

# Creates a sub menu
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=fileopener)
file_menu.add_command(label="Save", command=lambda: print("Save selected"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Creates a view menu
view_menu = tk.Menu(main_menu, tearoff=0)
view_menu.add_command(label="Graph View", command=lambda: print("Switched to Graph View"))
view_menu.add_command(label="Data View", command=lambda: print("Switched to Data View"))

#Create Middle Menu Frame
left_frame = Frame(root, width=200, height=600, bg='grey', bd=1, relief="solid")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

# Add submenu to main menu
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="View", menu=view_menu)

# Configure the main window to use the main menu
root.config(menu=main_menu)

# Data Import button
upload_button = tk.Button(left_frame, text="Upload CSV File", command=fileopener)
upload_button.grid(column=0, row=0, padx=10, pady=10)

#Button to convert selected file to excel file
csvtoexcel_button = tk.Button(left_frame, text="CSV Files to Excel", command=csvtoexcel)
csvtoexcel_button.grid(column=1, row=0, padx=10, pady=10)

#Save button
save_button = tk.Button(left_frame, text="Save File", command=Filenamepopup)
save_button.grid(column=2, row=0, padx=10, pady=10)


root.mainloop()