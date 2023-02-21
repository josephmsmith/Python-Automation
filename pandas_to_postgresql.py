def createengine(eng, usr, pas, address, port, db):
    engine = create_engine(f'{eng}://{usr}:{pas}@{address}:{port}/{db}')
    return engine.connect()
    # reference    f'postgresql://postgres:16f5@localhost:5434/bikeshare')


def dataload(connection, table_name, df):
    df.to_sql(table_name, connection, if_exists='replace', chunksize=1000)


def main():
    csv = input('what file would you like to install: (provide path)')
    df = createdf(csv)
    eng = input('engine: ')
    usr = input('user: ')
    password = input('password: ')
    address = input('address: ')
    port = input('port: ')
    db = input('database: ')
    connection = createengine(eng, usr, password, address, port, db)
    table_name = input('name of table: ')
    dataload(connection, table_name, df)
    connection.close()


main()

# go to anaconda prompt and you must run before executing (this is only required once)
# conda install -c conda-forge psycopg2
# conda install -c conda-forge sqlalchemy
# Before Running you must make a DB in pgadmin
# Start a thread here with any questions
# Put all of this code into one cell for ipynb or one .py file in jupyterlab.
# TLDR this code will automagically create tables for you and load data for you in postgresql 