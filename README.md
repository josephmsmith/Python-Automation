# Python Projects and Helpful Scripts

## [Mapping Sea Surface Temps(project)](https://github.com/josephmsmith/Python-Misc/blob/main/Plotting_SST_Data.ipynb)
Mapping Sea Surface Temperatures using data retrieved on NASA website. 

## [read_multiple_local_csvs](https://github.com/josephmsmith/Python-Misc/blob/main/read_multiple_local_csvs.py)
This script takes in a user input of the folder file path containing multiple flat files (specifically CSVs) with the same shape, combines them, and stores them in a single data frame used by pandas.

This script is designed for multiple CSVs without headers and assigns them a numerical value. 

## [pd_df_to_pgadmin](https://github.com/josephmsmith/Python-Misc/blob/main/pd_df_to_pgadmin.py)
This script is used to take in an existing dataframe created in pandas and export it to a new table in an existing database located in pgAdmin. 
This will fail if there are any existing tables with the same name
