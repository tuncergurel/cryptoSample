import pyodbc


def sqlConnect():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=server;'
                          'Database=AdventureWorks2019;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    return cursor






