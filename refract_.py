import pyodbc
import take_csv as tcsv
import ui as ui

global connection
global pointer
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
pointer = connection.cursor()

# getting data from local DB
def db_get_data():
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
    pointer = connection.cursor()

    pointer.execute("""
    SELECT * FROM [testDB].[dbo].[final_data_table1]
    ORDER BY [ID]
    """)
    db_get_data.data_all = []
    while True:
        row = pointer.fetchone()
        if not row:
            break
        db_get_data.data_all.append(row)
    how_many_ids_at_db = len(db_get_data.data_all)
    print("records at DB (quantity):", how_many_ids_at_db, "\n")
    print(db_get_data.data_all[:])
    return how_many_ids_at_db

def get_list():
    pointer = connection.cursor()
    pointer.execute("""
                SELECT * FROM [testDB].[dbo].[final_data_table1]
                ORDER BY [ID]
                """)

    table_data_firstname = []
    table_data_Position = []
    table_data_Office = []
    table_data_Age = []
    table_data_Salary = []
    table_data_Date = []
    data_list = [[], [], [], [], [], []]

    while True:
        row = pointer.fetchone()
        if not row:
            break
        table_data_firstname.append(row.Name)
        table_data_Position.append(row.Position)
        table_data_Office.append(row.Office)
        table_data_Age.append(row.Age)
        table_data_Salary.append(row.Salary)
        table_data_Date.append(row.Date)
    data_list = [table_data_firstname, table_data_Position, table_data_Office,
                 table_data_Age, table_data_Salary, table_data_Date]

    #print(data_list[1][0])
    return data_list

def del_record_db(dd):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
    pointer = conn.cursor()
    # pointer.execute("""
    # SELECT * FROM [testDB].[dbo].[final_data_table1]
    # """)
    #
    # records = pointer.fetchall()
    #
    # for record in records:
    #     print(record)


    #cursor = pointer
    SQLCommand = ("""
    delete from [testDB].[dbo].[final_data_table1] 
    where ID=?
    """)
    ID = dd
    # Processing Query
    pointer.execute(SQLCommand, ID)
    # Committing any pending transaction to the database.
    conn.commit()
    # closing connection
    print("Data Successfully Deleted")
    conn.close()

    #
    # pointer.execute("""
    # delete from [testDB].[dbo].[final_data_table1]
    # where ID=?
    # """)
    # ID = dd

    print("\nRecord Deleted successfully ")
    # print("\nDisplaying Total records from table after Deleting single record \n ")
    # pointer.execute("""
    #     SELECT * FROM [testDB].[dbo].[final_data_table1]
    #     """)
    #
    # records = pointer.fetchall()
    # for record in records:
    #     print(record)



# insert data to local DB
def record_to_db(i, id_now, kwargs):
    print(kwargs['Firstname'])
    print(kwargs['Position'])



    csv_data = tcsv.csv_data()
    #print(csv_data[0])
    #i = 7               # <------
    Id = int(id_now) + 1

    if i == 0:
        Firstname = (kwargs['Firstname'])
        Position = (kwargs['Position'])
        Office = (kwargs['Office'])
        Age = (kwargs['Age'])
        Salary = (kwargs['Salary'])
        data = (kwargs['data'])

    else:
        Firstname = csv_data[i][0]
        Position = csv_data[i][1]
        Office = csv_data[i][2]
        Age = csv_data[i][3]
        Salary = csv_data[i][5]
        data = csv_data[i][4]

    #cursor = connection.cursor()
    SQLCommand = ("""
    INSERT INTO final_data_table1 
    ([ID],[Name],[Position],[Office],[Age],[Salary],[Date]) 
    VALUES (?,?,?,?,?,?,?)
    """)
    Values = [Id, Firstname,Position, Office, Age, Salary, data]
    # Processing Query
    pointer.execute(SQLCommand, Values)
    # Committing any pending transaction to the database.
    connection.commit()
    # closing connection
    print("Data Successfully Inserted")
    #connection.close()


def main(xx, **kwargs):
    num_line = xx

    #print({kwargs['OFFICE']})
    record_to_db(num_line, db_get_data(), kwargs)
    print("After adding records at DB (quantity):", db_get_data())
    return 1


if __name__ == '__main__':
    main()



