import pyodbc
try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\PC\PycharmProjects\pythonProject1\Database01.accdb;')
    print("Database is Connected")

    user_id = 13
    FullName = 'Mark Adrian Beranque'
    Age = '18'
    Address = 'Cavite'
    Birthdate = '28/12/2003'
    SemGrade = 90

    database = connect.cursor()
    database.execute('update Table1 set Fullname=? where id=?', (FullName, user_id))
    database.execute('update Table1 set Age=? where id=?', (Age, user_id))
    database.execute('update Table1 set Address=? where id=?', (Address, user_id))
    database.execute('update Table1 set Birthdate=? where id=?', (Birthdate, user_id))
    database.execute('update Table1 set SemGrade=? where id=?', (SemGrade, user_id))
    database.commit()
    print("Data is updated")

except pyodbc.Error:
    print("Error in Connection")
