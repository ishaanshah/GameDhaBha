""" Contains all the functions related to the search of enitities in the Database """


from tabulate import tabulate


def SearchPlayerByName(cur, con):
    """ Searches for the provided name's similar occurences in the Player's first and last name """
    # Take in the input for the search query
    search = {}
    search["pattern"] = input("Enter the player name that you are looking for: ")
    search["pattern"] = "%" + search["pattern"] + "%"

    query = """
            SELECT *
            FROM Players
            WHERE FirstName LIKE %(pattern)s
            OR LastName LIKE %(pattern)s
            """


    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, search)

    # Print the output

    headers = ["Username", "PlayerID", "FirstName", "LastName", "Winnings",
                "Nationality", "DateOfBirth"]
    rows = []

    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([
            res["Username"], res["PlayerID"], res["FirstName"], res["LastName"],
            res["Winnings"], res["Nationality"], res["DateOfBirth"]
            ])


    print(tabulate(rows, headers = headers, tablefmt = "orgtbl"))
    print("")



def SearchOrganisationByName(cur, con):
    """ Searches for an Organisation by the name given. """
    # Take in the input for the search query
    search = {}
    search["pattern"] = input("Enter the organisation's name that you are looking for: ")
    search["pattern"] = "%" + search["pattern"] + "%"

    query = """
            SELECT *
            FROM Organisations
            WHERE Name LIKE %(pattern)s
            """


    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, search)

    # Print the output

    headers = ["OrganisationID", "Name", "Headquarters", "Founded", "Earnings"]
    rows = []

    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([
            res["OrganisationID"], res["Name"], res["Headquarters"], res["Founded"],
            res["Earnings"]
            ])


    print(tabulate(rows, headers = headers, tablefmt = "orgtbl"))
    print("")

def SearchHandler(cur, con):
    # Define Handlers
    handlers = [
        SearchPlayerByName,
        SearchOrganisationByName
    ]

    # Get operation to Perform
    print("1. Search Player by Name.")
    print("2. Search Organisation by Name.")
    print("3. Go Back.")

    ch = int(input("Enter choice: "))
    if ch == 3:
        return

    try:
        handlers[ch - 1](cur, con)
        con.commit()
        print("Search Successful.")
    except (IndexError, TypeError):
        print(f"Error: Invalid Option {ch}")
    except Exception as error:
        con.rollback()
        print("Failed to update the Database.")
        print(f"Error: {error}")
