import pyodbc
cnxn = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=AP;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Invoices")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row)
cnxn.close()
