import pandas as pd
import os

# Set the directory containing the CSV files, user input
directory = input("Enter the CSV folder file path here: ")

# Get a list of all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]

# Initialize an empty list to store the dataframes
dfs = []

# Loop through each CSV file, read it into a dataframe, and append it to the list
for csv_file in csv_files:
    filepath = os.path.join(directory, csv_file)
    df = pd.read_csv(filepath, header=None)
    dfs.append(df)
    print(f"File {csv_file} has shape {df.shape}")

# Concatenate all the dataframes in the list into one dataframe
combined_df = pd.concat(dfs, ignore_index=True)

# Set the column names to be integers starting from 0
combined_df.columns = range(combined_df.shape[1])

# Print the combined dataframe
print(combined_df)
