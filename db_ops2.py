import pyodbc
import csv


class DBConnect(object):
    def __init__(self):
        global connection
        global pointer
        global sql_call_del
        global sql_call_get
        global sql_call_input
        global sql_entry_count

        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB;UID=;PWD=')
        pointer = connection.cursor()

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

        sql_entry_count = (""" 
            SELECT COUNT(ID) 
            FROM [testDB].[dbo].[final_data_table1]
            """)

    def csv_data(self):
        list_of_lists = []
        lists = []
        file_path = 'data.csv'
        with open(file_path, 'rU') as f:  # opens PW file
            data = list(list(rec) for rec in csv.reader(f, delimiter=','))  # reads csv into a list of lists
            for row in data:
                list_of_lists.append((list(lists)))
                lists = []
                for username in row:
                    lists.append(username)
        del list_of_lists[0]
        del list_of_lists[0]
        return list_of_lists

    def entry_count(self):
        count = pointer.execute(sql_entry_count)
        data = count.fetchall()
        for i in data:
            x = i[0]
        return x

    def get_all_db_records(self):
        data = pointer.execute(sql_call_get)

        table_data_firstname = []
        table_data_Position = []
        table_data_Office = []
        table_data_Age = []
        table_data_Salary = []
        table_data_Date = []
        data_list = [[], [], [], [], [], []]

        while True:
            row = data.fetchone()
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

    def add_db_record(self, kwargs):
        Id = DBConnect.entry_count(self) + 1
        Firstname = (kwargs['Firstname'])
        Position = (kwargs['Position'])
        Office = (kwargs['Office'])
        Age = (kwargs['Age'])
        Salary = (kwargs['Salary'])
        data = (kwargs['data'])
        Values = [Id, Firstname, Position, Office, Age, Salary, data]
        pointer.execute(sql_call_input, Values)
        connection.commit()
        print("Data Successfully Inserted")

    def add_db_record_csv(self, i):
        csv_data = DBConnect.csv_data(self)
        Id = DBConnect.entry_count(self) + 1
        Firstname = csv_data[i][0]
        Position = csv_data[i][1]
        Office = csv_data[i][2]
        Age = csv_data[i][3]
        Salary = csv_data[i][5]
        data = csv_data[i][4]
        Values = [Id, Firstname, Position, Office, Age, Salary, data]
        pointer.execute(sql_call_input, Values)
        connection.commit()
        print("CSV Data Successfully Inserted")

    def del_db_entry(self, id_entry):
        pointer.execute(sql_call_del, id_entry)
        connection.commit()
        print("Entry Successfully Deleted")


global kwr_data
kwr_data = dict(Firstname="Bob", Position="General", Office="Fremont", Age="85", Salary="$15225", data="15-12-98")
db = DBConnect()                          # assigning to class
# x = db.entry_count(); print(x)          # Count how many entry's at the DB already
# print(db.get_all_db_records()[0][x-1])  # Get all records from DB as list of lists where [6 main columns][N - rows]
# db.add_db_record(kwr_data)              # Record new entry to DB from kwr_data dictionary
# print(db.get_all_db_records()[0][x])    # Get all records from DB as list of lists where [6 main columns][N - rows]
# print(db.entry_count())                 # Count how many entry's at the DB already
# db.del_db_entry(28)                     # Delete entry from DB
# print(db.entry_count())                 # Count how many entry's at the DB already
# db.add_db_record_csv(31)                # Get data from csv file end enter it to DB
# x = db.entry_count(); print(x)          # Count how many entry's at the DB already


def main():
    x = db.entry_count()
    print(x)

    db.add_db_record_csv(40)

    x = db.entry_count()
    print(x)
    pass


if __name__ == '__main__':
    main()

