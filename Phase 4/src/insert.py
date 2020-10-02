""" Contains all the functions related to insertion of entities into the database """


def InsertOrganisation(cur, con, entity_name: str = "Organisation") -> int:
    """ Inserts a new Organisation into the database """
    # Get information about the video game
    print(f"Enter new {entity_name}'s details:")
    row = {}
    row["Name"] = input(f"Enter the name of the {entity_name}: ")
    row["Headquarters"] = input(
        f"Enter the headquarters of {entity_name} (Optional): ") or None
    row["Founded"] = input(
        f"Enter the date when the {entity_name} was founded in YYYY-MM-DD format: ")
    row["Earnings"] = input(
        f"Enter earnings of {entity_name} in USD (Optional): ") or 0

    # Query to be executed
    query = """INSERT INTO Organisations (Name, Headquarters,
                                           Founded, Earnings)
                    VALUES (%(Name)s, %(Headquarters)s,
                             %(Founded)s, %(Earnings)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Get ID of last inserted organisation
    cur.execute("SELECT LAST_INSERT_ID() AS OrganisationID")
    return cur.fetchone()["OrganisationID"]


def InsertVideoGame(cur, con):
    """ Inserts a new Video Game into the database """
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
    query = """INSERT INTO VideoGames (Name, ReleaseDate, LatestPatch,
                                        RegisteredPlayers, OrganisationID)
                    VALUES (%(Name)s, %(ReleaseDate)s, %(LatestPatch)s,
                             %(RegisteredPlayers)s, %(OrganisationID)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def InsertDeveloper(cur, con):
    """ Inserts a new Developer in the database """
    row = {}
    row["OrganisationID"] = InsertOrganisation(cur, con, "Developer")
    row["CEO"] = input("Enter the Developer's CEO name: ")

    # Query to be executed
    query = """INSERT INTO Developers (OrganisationID, CEO)
                     VALUES (%(OrganisationID)s, %(CEO)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def InsertTeam(cur, con):
    # Get information about the Team
    """ Inserts a new Team in the database """
    row = {}
    row["OrganisationID"] = InsertOrganisation(cur, con, "Team")
    row["Manager"] = input("Enter the team's manager name: ")

    # Query to be executed
    query = """INSERT INTO Teams (OrganisationID, Manager)
                     VALUES (%(OrganisationID)s, %(Manager)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def InsertESportEvent(cur, con):
    raise NotImplementedError


def CreateRanklist(cur, con):
    raise NotImplementedError


def InsertPlayer(cur, con):
    """ Inserts a new player in the database."""
    # Get information about the player
    row = {}
    row["Username"] = input("Enter the username of the player: ") or None
    row["FirstName"] = input("Enter the first name of the player: ") or None
    row["LastName"] = input("Enter the last name of the player: ") or None
    row["Winnings"] = input(
        "Enter the total winnings of the player till now: ") or 0
    row["Nationality"] = input("Enter the Nationality of the player: ") or None
    row["DateOfBirth"] = input(
        "Enter the date of birth of the player in YYYY-MM-DD format: ") or None

    # Query to be executed
    query = """INSERT INTO Players (Username, FirstName, LastName,
                                    Winnings, Nationality, DateOfBirth)
                    VALUES (%(Username)s, %(FirstName)s, %(LastName)s,
                            %(Winnings)s, %(Nationality)s, %(DateOfBirth)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def InsertCoach(cur, con):
    """ Inserts a new coach in the database """
    # Get information about the Coach
    print("Enter new Coaches' information:")
    row = {}
    row["Name"] = input("Enter the name of the coach: ") or None
    row["StartDate"] = input(
        "Enter the start date of the coach in YYYY-MM-DD format: ") or None
    row["EndDate"] = input(
        "Enter the end date of the coach YYYY-MM-DD format (Optional): ") or None
    row["TeamID"] = input(
        "Enter the TeamID of the team that the coach is for: ") or None
    row["GameID"] = input(
        "Enter the GameID of the game that the coach is for: ") or None

    # Query to be executed
    query = """INSERT INTO Coaches (Name, StartDate, EndDate,
                                    TeamID, GameID)
                    VALUES (%(Name)s, %(StartDate)s, %(EndDate)s,
                            %(TeamID)s, %(GameID)s)
            """

    print("\nExecuting")
    print(query)

    # Executing query
    cur.execute(query, row)


def InsertHandler(cur, con):
    # Define handlers
    handlers = [
        InsertOrganisation,
        InsertVideoGame,
        InsertDeveloper,
        InsertTeam,
        InsertESportEvent,
        CreateRanklist,
        InsertPlayer,
        InsertCoach
    ]

    # Get operation to perform
    print("1. Insert Organisation")
    print("2. Insert Video Game")
    print("3. Insert Developer")
    print("4. Insert Team")
    print("5. Insert eSport Event")  # Sriram
    print("6. Create Ranklist")  # Sriram
    print("7. Insert Player")  # Rahul
    print("8. Insert Coach")  # Rahul
    print("9. Go Back")
    ch = int(input("Enter choice: "))
    if ch == 9:
        return

    try:
        handlers[ch-1](cur, con)
        con.commit()
        print("Insertion successful")
    except (IndexError, TypeError):
        print(f"Error: Invalid option {ch}")
    except Exception as error:
        con.rollback()
        print("Failed to insert into the Database")
        print(f"Error: {error}")
