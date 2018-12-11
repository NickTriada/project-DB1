import pyodbc
import take_csv as tcsv


class DBConnect(object):
    def __init__(self):
        global connection
        global pointer
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
        pointer = connection.cursor()
        global sql_call_del
        global sql_call_get
        global sql_call_input

        sql_call_get = ("""
            SELECT * FROM [testDB].[dbo].[final_data_table1]
            ORDER BY [ID]
            """)

        sql_call_input = ("""
            INSERT INTO final_data_table1 
            ([ID],[Name],[Position],[Office],[Age],[Salary],[Date]) 
            VALUES (?,?,?,?,?,?,?)
            """)

        sql_call_del = ("""
            delete from [testDB].[dbo].[final_data_table1] 
            where ID=?
            """)



    def get_db_data(self):
        pass

    def qtt_db_records(self):
        pointer.execute(sql_call_get)
        data_all = []
        while True:
            row = pointer.fetchone()
            if not row:
                break
            data_all.append(row)
        records_qtt = len(data_all)
        return records_qtt

    def add_db_record(self, **kwargs):
        values = [kwargs, kwargs, kwargs, kwargs, kwargs, kwargs, kwargs]
        pointer.execute(sql_call_input, values)
        connection.commit()


    def del_db_record(self, *args):
        pointer.execute(sql_call_del, args)
        connection.commit()
        connection.close()



def db_get_data():
    # connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
    # pointer = connection.cursor()

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

    return data_list

def del_record_db(dd):
    # conn = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
    # pointer = conn.cursor()

    # SQLCommand = ("""
    # delete from [testDB].[dbo].[final_data_table1]
    # where ID=?
    # """)

    pointer.execute(sql_call_del, dd)
    # Committing any pending transaction to the database.
    connection.commit()
    # closing connection
    print("Data Successfully Deleted")
    connection.close()

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
    Id = int(id_now) + 1

    if i == 0:  # adding to DB from entry fields
        Firstname = (kwargs['Firstname'])
        Position = (kwargs['Position'])
        Office = (kwargs['Office'])
        Age = (kwargs['Age'])
        Salary = (kwargs['Salary'])
        data = (kwargs['data'])

    else:  # adding from csv file by entered number
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



