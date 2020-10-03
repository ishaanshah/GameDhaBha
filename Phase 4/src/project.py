""" Contains all the functions related to projection of entities from the database """

from tabulate import tabulate


def GetEventsAfter(cur, con):
    """ Gets ESports events that take place after a certain date """
    row = {}
    row["Date"] = input(
        "Enter the date after which ESports events should be "
        "returned in YYYY-MM-DD format: ") or None

    # Query to be executed
    query = """SELECT *
                 FROM ESportEvents
                WHERE StartDate >= %(Date)s
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the events
    headers = ["EventID", "Name", "StartDate", "EndDate", "PrizePool"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([
            res["EventID"], res["Name"], res["StartDate"],
            res['EndDate'], res["PrizePool"]
        ])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def ProjectHandler(cur, con):
    # Define handlers
    handlers = [
        GetEventsAfter
    ]

    # Get operation to perform
    print("1. Get Events after")
    print("2. Go Back")
    ch = int(input("Enter choice: "))
    if ch == 2:
        return

    try:
        handlers[ch-1](cur, con)
        con.commit()
        print("Projection successful")
    except (IndexError, TypeError) as error:
        print(f"Error: Invalid option {ch}")
        print(error)
    except Exception as error:
        con.rollback()
        print("Failed to retrieve data form the  Database")
        print(f"Error: {error}")
