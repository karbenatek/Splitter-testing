import numpy
from matplotlib import pyplot as plt
import csv

file_paths = ['split8.csv', 'split8_redo.csv', 'split8_redo2.csv','split8_redo3.csv']

# Initialize an empty list to store the data
data_list = []

# Iterate over each file path
for file_path in file_paths:
    print(f'Reading data from file: {file_path}')
    meas = []
    
    # Open the CSV file in read mode
    with open(file_path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Assuming the CSV file has two columns (e.g., col1, col2)
            col1, col2 = row
            # Append the data as a tuple (col1, col2) to the data_list
            meas.append(100*int(col1)/int(col2))
            
    data_list.append(meas)

print(data_list)
plt.figure(figsize=(12,6))
for meas in data_list:
    plt.plot(meas, "x")
plt.legend([f"meas{i}" for i in range(1, len(data_list)+1)])
plt.xlabel("splitter output")
plt.ylabel("pulse/trigger ratio [/%]")
plt.savefig("split8-test.pdf")