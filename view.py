import pyodbc
try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\PC\PycharmProjects\pythonProject1\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('SELECT * FROM Table1')
    for x in database.fetchall():
        print(x)


except pyodbc.Error:
    print("Error in Connection")
