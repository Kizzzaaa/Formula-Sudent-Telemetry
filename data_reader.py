# Import necessary modules
import csv  # Module to work with CSV files
import pandas as pd  # Data analysis and manipulation tool
import matplotlib.pyplot as plt  # Plotting library
import numpy as np  # Library for numerical computations

# Step 1: Reading the CSV file using the csv module (consider removing this part to streamline the code)
file = open('pressure_data.csv')  # Open the CSV file in read mode
type(file)  # Print the type of the 'file' object (not necessary, can be removed)
csvreader = csv.reader(file)  # Create a csv reader object to read the file line by line
header = []  # Initialize an empty list to store the header
header = next(csvreader)  # Retrieve the header (first line) from the file
print(header)  # Print the header
rows = []  # Initialize an empty list to store the rows
for row in csvreader:  # Loop through each row in the file
    rows.append(row)  # Append each row to the 'rows' list
print(rows)  # Print the rows

# Step 2: Reading the CSV file using pandas and saving it as an Excel file
csvDataframe = pd.read_csv('pressure_data.csv')  # Read the CSV file into a pandas DataFrame
resultExcelfile = pd.ExcelWriter('pressure_data.xlsx')  # Create an Excel writer object
csvDataframe.to_excel(resultExcelfile, index=False)  # Write the DataFrame to an Excel file
resultExcelfile.close()  # Close the Excel writer object to save the data to the file

# Step 3: Reading the Excel file and performing initial analysis
excelDataframe = pd.read_excel('pressure_data.xlsx')  # Read the data from the Excel file into a DataFrame
print(excelDataframe)  # Print the data
df = pd.read_excel('pressure_data.xlsx')  # Read the data again (consider removing this line to avoid redundancy)
print(df.describe())  # Print statistical details of the DataFrame

# Step 4: Calculating dynamic pressure and airspeed
df['dynamic_pressure'] = df['total_pressure'] - df['static_pressure']  # Calculate dynamic pressure
print(df)  # Print the DataFrame with the new column
air_density = 1.225  # Define air density (in kg/m^3)
df['airspeed(m/s)'] = (2 * df['dynamic_pressure'] / air_density) ** 0.5  # Calculate airspeed in m/s
df['air_speed(mph)'] = 2.237 * df['airspeed(m/s)']  # Convert airspeed to mph
df.to_excel('modified_pressure_data.xlsx', index=False)  # Save the modified data to a new Excel file

# Step 5: Slicing the first 180 readings to analyze the first 3 minutes of a session
timestamp = df['timestamp']  # Get the timestamp column
timestamp_180 = timestamp[:180]  # Slice the first 180 timestamps
airspeed = df['airspeed(m/s)']  # Get the airspeed column
airspeed_180 = airspeed[:180]  # Slice the first 180 airspeed readings

# Step 6: Converting timestamps to seconds and plotting the data
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert the timestamp column to datetime objects
df['time(s)'] = (df['timestamp'] - df['timestamp'].iloc[0]).dt.total_seconds()  # Calculate time in seconds since the first timestamp
time = df['time(s)']  # Get the time in seconds column
time_180 = time[:180]  # Slice the first 180 time readings

# Plotting the data
plt.plot(time_180, airspeed_180, label='2x')  # Plot airspeed over time (consider adding a legend to explain the label '2x')
plt.title('Airspeed Over Time', fontdict={'fontsize':20})  # Set the title of the plot
plt.xlabel('Time(s)')  # Label the x-axis
plt.ylabel('Airspeed(m/s)')  # Label the y-axis
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.xticks(np.arange(0, 200, 5))  # Set custom x-axis ticks
plt.yticks(np.arange(12, 18, 0.25))  # Set custom y-axis ticks
plt.grid(True)  # Add a grid to the plot
plt.show()  # Display the plot