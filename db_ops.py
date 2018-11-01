import pyodbc
import take_csv as tcsv

# getting data from local DB
def db_get_data():
    db_get_data.connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
    pointer = db_get_data.connection.cursor()
    pointer.execute("""
    SELECT * FROM [testDB].[dbo].[final_data_table1]
    """)
    db_get_data.data_all = []
    while True:
        row = pointer.fetchone()
        if not row:
            break
        db_get_data.data_all.append(row)
    how_many_ids_at_db = len(db_get_data.data_all)
    print("records at DB (quantity):", how_many_ids_at_db, "\n")
    return how_many_ids_at_db


# insert data to local DB
def record_to_db(id_now):
    csv_data = tcsv.csv_data()
    #print(csv_data[0])
    i = 4
    Id = int(id_now) + 1
    Firstname = csv_data[i][0]
    Position = csv_data[i][1]
    Office = csv_data[i][2]
    Age = csv_data[i][3]
    Salary = csv_data[i][5]
    data = csv_data[i][4]

    cursor = db_get_data.connection.cursor()
    SQLCommand = ("""
    INSERT INTO final_data_table1 
    ([ID],[Name],[Position],[Office],[Age],[Salary],[Date]) 
    VALUES (?,?,?,?,?,?,?)
    """)
    Values = [Id, Firstname,Position, Office, Age, Salary, data]
    # Processing Query
    cursor.execute(SQLCommand, Values)
    # Committing any pending transaction to the database.
    db_get_data.connection.commit()
    # closing connection
    print("Data Successfully Inserted")
    db_get_data.connection.close()


record_to_db(db_get_data())
print("After adding records at DB (quantity):", db_get_data())


