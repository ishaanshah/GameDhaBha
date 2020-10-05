import subprocess as sp
import pymysql
import pymysql.cursors
import sys

from insert import InsertHandler
from update import UpdateHandler
from search import SearchHandler
from project import ProjectHandler
from report import ReportHandler

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if ch == 1:
        InsertHandler(cur, con)
    elif ch == 2:
        UpdateHandler(cur, con)
    elif ch == 3:
        raise NotImplementedError
    elif ch == 4:
        ProjectHandler(cur, con)
    elif ch == 5:
        raise NotImplementedError
    elif ch == 6:
        SearchHandler(cur, con)
    elif ch == 7:
        ReportHandler(cur, con)
    else:
        print("Error: Invalid Option")


# Global
while True:
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hard core username and password
    username = "root"
    password = "password"

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=password,
                              db='GameDhaBha',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while True:
                tmp = sp.call('clear', shell=True)
                print("1. Insert")
                print("2. Update")
                print("3. Delete")
                print("4. Project")
                print("5. Aggregate")
                print("6. Search")
                print("7. Report")
                print("8. Quit")
                ch = int(input("Enter choice: "))
                tmp = sp.call('clear', shell=True)
                if ch == 8:
                    exit(0)
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
