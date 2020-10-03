""" Contains all the functions related to aggregation of entities from the database """

from tabulate import tabulate


def GetYoungestPlayer(cur, con):
    """ Gets the age of youngest player in the database """
    # Query to be executed
    query = """SELECT MIN(TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE())) AS MinAge
                 FROM Players
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query)

    # Calculate and print the player with minimum age
    headers = ["Age"]
    rows = []
    res = cur.fetchone()
    if res is not None:
        rows.append([res["MinAge"]])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def AggregateHandler(cur, con):
    # Define handlers
    handlers = [
        GetYoungestPlayer
    ]

    # Get operation to perform
    print("1. Get youngest player from database")
    print("2. Go Back")
    ch = int(input("Enter choice: "))
    if ch == 2:
        return

    try:
        handlers[ch-1](cur, con)
        con.commit()
        print("Retrieval successful")
    except (IndexError, TypeError) as error:
        print(f"Error: Invalid option {ch}")
        print(error)
    except Exception as error:
        con.rollback()
        print("Failed to retrieve data form the Database")
        print(f"Error: {error}")
