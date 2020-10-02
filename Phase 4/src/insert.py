""" Contains all the functions related to insertion of entities into the database """


def InsertOrganisation(cur, con):
    """ Inserts a new Organisation into the database """
    try:
        # Get information about the video game
        print("Enter new Organisation's details:")
        row = {}
        row["Name"] = input("Enter the name of the Organisation: ")
        row["Headquarters"] = input(
            "Enter the headquarters of organisation (Optional): ") or None
        row["Founded"] = input(
            "Enter the date when the organisation was founded in YYYY-MM-DD format: ")
        row["Earnings"] = input(
            "Enter earnings of organisation in USD (Optional): ") or None

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
        con.commit()
        print("Insertion successful")
    except Exception as error:
        con.rollback()
        print("Failed to insert into the Database")
        print(f"Error: {error}")


def InsertVideoGame(cur, con):
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
        query = """INSERT INTO VideoGames (Name, ReleaseDate, LatestPatch,
                                            RegisteredPlayers, OrganisationID)
                         VALUES (%(Name)s, %(ReleaseDate)s, %(LatestPatch)s,
                                 %(RegisteredPlayers)s, %(OrganisationID)s)
                """

        print("\nExecuting")
        print(query)

        # Execute query
        cur.execute(query, row)
        con.commit()
        print("Insertion successful")
    except Exception as error:
        con.rollback()
        print("Failed to insert into the Database")
        print(f"Error: {error}")


def InsertDeveloper(cur, con):
    raise NotImplementedError


def InsertTeam(cur, con):
    raise NotImplementedError


def InsertESportEvent(cur, con):
    raise NotImplementedError


def CreateRanklist(cur, con):
    raise NotImplementedError


def InsertPlayer(cur, con):
    raise NotImplementedError


def InsertCoach(cur, con):
    raise NotImplementedError


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
    except (IndexError, TypeError):
        print(f"Error: Invalid option {ch}")
    except Exception as error:
        print(f"Error: {error}")
