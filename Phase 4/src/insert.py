""" Contains all the functions related to insertion of entities into the database """


def InsertOrganisation(cur, con, entity_name: str = "Organisation") -> int:
    """ Inserts a new Organisation into the database """
    # Get information about the video game
    print(f"Enter new {entity_name}'s details:")
    row = {}
    row["Name"] = input(f"Enter the name of the {entity_name}: ") or None
    row["Headquarters"] = input(
        f"Enter the headquarters of {entity_name} (Optional): ") or None
    row["Founded"] = input(
        f"Enter the date when the {entity_name} was founded in YYYY-MM-DD format: ") or None
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
    row["Name"] = input("Enter the name of the Video Game: ") or None
    row["ReleaseDate"] = input(
        "Enter the release date of the VideoGame in YYYY-MM-DD format: ") or None
    row["LatestPatch"] = input("Enter the latest release number: ") or None
    row["RegisteredPlayers"] = input(
        "Enter the number of players currently playing the game: ") or None
    row["OrganisationID"] = input(
        "Enter the OrganisationID of the Organisation that created the game: ") or None

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
    # Get information about the Developer
    row = {}
    row["OrganisationID"] = InsertOrganisation(cur, con, "Developer")
    row["CEO"] = input("Enter the Developer's CEO name: ") or None

    # Query to be executed
    query = """INSERT INTO Developers (OrganisationID, CEO)
                    VALUES (%(OrganisationID)s, %(CEO)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def InsertTeam(cur, con):
    """ Inserts a new Team in the database """
    # Get information about the Team
    row = {}
    row["OrganisationID"] = InsertOrganisation(cur, con, "Team")
    row["Manager"] = input("Enter the team's manager name: ") or None

    # Query to be executed
    query = """INSERT INTO Teams (OrganisationID, Manager)
                    VALUES (%(OrganisationID)s, %(Manager)s)
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def InsertESportEvent(cur, con):
    """Inserts a new ESportEvent in the database """
    # Get information about the Event
    row = {}
    row["Name"] = input("Enter the Name of the ESportEvent: ") or None
    row["StartDate"] = input(
        "Enter the start date of the ESportEvent in YYYY-MM-DD format: ") or None
    row["EndDate"] = input(
        "Enter the end date of the ESportEvent in YYYY-MM-DD format: ") or None
    row["PrizePool"] = input(
        "Enter the total prize pool for the ESportEvent in USD: ") or None

    # Query to be executed
    query = """INSERT INTO ESportEvents (Name, StartDate, EndDate, PrizePool)
                    VALUES (%(Name)s, %(StartDate)s, %(EndDate)s, %(PrizePool)s)
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def CreateRanklist(cur, con):
    """ Creates a ranklist for an ESportEvent. """
    # Get the first, second and the third place
    row = {}
    row["EventID"] = input(
        "Enter the EventID for the Event for which the Ranklist has to be created: ") or None
    row["FirstPlace"] = input(
        "Enter the TeamID of the Team who placed First in the Event: ") or None
    row["SecondPlace"] = input(
        "Enter the TeamID of the Team who placed Second in the Event: ") or None
    row["ThirdPlace"] = input(
        "Enter the TeamID of the Team who placed Third in the Event: ") or None

    # Query to be executed
    query = """INSERT INTO Ranklist (EventID, FirstPlace,
                                     SecondPlace, ThirdPlace)
                    VALUES (%(EventID)s, %(FirstPlace)s,
                            %(SecondPlace)s, %(ThirdPlace)s)
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


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

def InsertParticipationOfPlayerInEvent(cur, con):
    """ Inserts into the database, the played entity. """
    # Get the information
    print("Enter the required information: ")
    row = {}
    row["OrganisationID"] = input("Enter the Organisation ID of the participating team: ")
    row["EventID"] = input("Enter the ID of the ESportEvent the participation is being done in: ")
    row["PlayerID"] = input("Enter the ID of the participating player: ")
    row["GameID"] = input("Enter the VideoGameID of the Video Game the team is going to play: ")

    # Query to be executed
    query = """
            INSERT INTO
            Played (OrganisationID, EventID, PlayerID, GameID)
            VALUES (%(OrganisationID)s, %(EventID)s, %(PlayerID)s, %(GameID)s)
            """

    print("\nExecuting")
    print(query)

    # Executing query
    cur.execute(query, row)

def InsertOrganisationOfEvent (cur, con):
    """ Inserts into the entity Organised. """
    # Get the informatin
    print("Enter the required information: ")
    row = {}
    row["OrganisationID"] = input(
        "Enter the Organisation ID of the Organisation which is conducting the event: ")
    row["EventID"] = input("Enter the Event ID of the event being conducted: ")

    # Query to be executed
    query = """
            INSERT INTO
            Organised (OrganisationID, EventID)
            VALUES (%(OrganisationID)s, %(EventID)s)
            """

    print("\n Executing")
    print(query)

    # Execute query
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
        InsertCoach,
        InsertParticipationOfPlayerInEvent,
        InsertOrganisationOfEvent
    ]

    # Get operation to perform
    print("01. Insert Organisation")
    print("02. Insert Video Game")
    print("03. Insert Developer")
    print("04. Insert Team")
    print("05. Insert ESport Event")
    print("06. Create Ranklist")
    print("07. Insert Player")
    print("08. Insert Coach")
    print("09. InsertParticipationOfPlayerInEvent")
    print("10. InsertOrganisationOfEvent")
    print("11. Go Back")
    ch = int(input("Enter choice: "))
    if ch == 11:
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
