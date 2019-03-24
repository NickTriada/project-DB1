import pyodbc
import csv

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=NICKTRIADA\SQLEXPRESS;DATABASE=testDB121;UID=;PWD=')
pointer = connection.cursor()


def entry_count():
    sql_entry_count = (""" 
        SELECT COUNT(ID) 
        FROM [testDB121].[dbo].[final_data_table1]
        """)
    count = pointer.execute(sql_entry_count)
    data = count.fetchall()
    for i in data:
        x = i[0]
    return x

def get_all_db_records():
    sql_call_get = ("""
                SELECT * FROM [testDB121].[dbo].[final_data_table1]
                ORDER BY [ID]
                """)

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


print(entry_count())
# print(get_all_db_records()[:][:])