# This script is used to take in an existing dataframe created in pandas and export it to a new table in an existing database
# Make sure to create a database before initiating script

# imports
import pandas as pd
from sqlalchemy import create_engine
import os

# define database connection parameters (5)
db_user = 'insert_db_username'
db_password = 'insert_db_password'
db_host = 'insert_db_host'
db_port = 'insert_db_port'
db_name = 'insert_created_db_name'

# define db connection string
db_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# create db engine (this will create connection to db using the url created above)
engine = create_engine(db_string)

# export df to new table, if it exists already the export will fail, index false prevents index to import in pgadmin
new_table_name = 'this_will_be_your_new_table_name'
analysis1_data.to_sql(new_table_name, engine, if_exists = 'fail', index=False)

# close db connection to free resources with local machine and server, prevent a crash! 
engine.dispose()