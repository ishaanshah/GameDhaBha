import subprocess as sp
import pymysql
import pymysql.cursors
import sys


def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def InsertVideoGame():
    """ Inserts a new Video Game into the database """
    try:
        # Get information about the video game
        print("Enter new Video Game's details:")
        row = {}
        row["Name"] = input("Enter the name of the Video Game: ")
        row["ReleaseDate"] = input(
            "Enter the release date of the VideoGame in YYYY-MM-DD format: ")
        row["LatestPatch"] = input("Enter the latest release number: ")
        row["RegisteredPlayers"] = input(
            "Enter the number of players currently playing the game: ")
        row["OrganisationID"] = int(
            input("Enter the OrganisationID of the Organisation that created the game: "))

        # Query to be executed
        query = f"""INSERT INTO VideoGames (Name, ReleaseDate, LatestPatch,
                                            RegisteredPlayers, OrganisationID)
                         VALUES ("{row["Name"]}", "{row["ReleaseDate"]}", "{row["LatestPatch"]}",
                                 "{row["RegisteredPlayers"]}", "{row["OrganisationID"]}")
                 """

        print("\nExecuting")
        print(query)

        # Execute query
        cur.execute(query)
        con.commit()
        print("Insertion successful")
    except Exception as error:
        con.rollback()
        print("Failed to insert into the Database")
        print(f"Error {error}")

# Existing function in the given template. Keeping as of now for reference. To remove later when the project is complete.
#
# def hireAnEmployee():
#     """
#     This is a sample function implemented for the refrence.
#     This example is related to the Employee Database.
#     In addition to taking input, you are required to handle domain errors as well
#     For example: the SSN should be only 9 characters long
#     Sex should be only M or F
#     If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
#     HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
#     """
#     try:
#         # Takes emplyee details as input
#         row = {}
#         print("Enter new employee's details: ")
#         name = (input("Name (Fname Minit Lname): ")).split(' ')
#         row["Fname"] = name[0]
#         row["Minit"] = name[1]
#         row["Lname"] = name[2]
#         row["Ssn"] = input("SSN: ")
#         row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
#         row["Address"] = input("Address: ")
#         row["Sex"] = input("Sex: ")
#         row["Salary"] = float(input("Salary: "))
#         row["Dno"] = int(input("Dno: "))
#
#         query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
#             row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])
#
#         print(query)
#
#         cur.execute(query)
#         con.commit()
#
#         print("Inserted Into Database")
#
#     except Exception as e:
#         con.rollback()
#         print("Failed to insert into database")
#         print(">>>>>>>>>>>>>", e)
#
#     return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        InsertVideoGame()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")


# Global
while(1):
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
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1")  # Hire an Employee
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Quit")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit(0)
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
