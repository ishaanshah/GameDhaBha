""" Contains all the functions related to the updation of enitities in the Database """


def UpdateVideoGameLatestPatch(cur, con):
    """ Updates the latest patch for a VideoGame in the database """
    # Get the latest patch
    row = {}
    row["GameID"] = input(
        "Enter GameID of the Video Game for which latest "
        "patch has to be updated: ") or None
    row["LatestPatch"] = input("Enter latest patch for the game: ") or None

    # Query to be executed
    query = """UPDATE VideoGames
                  SET LatestPatch = %(LatestPatch)s
                WHERE GameID = %(GameID)s
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)


def AcquirementOfOrganization(cur, con):
    raise NotImplementedError


def AcquireOrganization(cur, con):
    raise NotImplementedError


def UpdateESportEventStartDate(cur, con):
    raise NotImplementedError


def UpdateESportEventEndDate(cur, con):
    raise NotImplementedError


def UpdateESportEventPrizePool(cur, con):
    """ Updates the latest patch for a VideoGame in the database """
    # Get the prize pool
    row = {}
    row["EventToUpdate"] = input(
        "Enter the Event ID of the eSport Event whose "
        "prize pool has to be updated: ") or None
    row["NewPrizePool"] = input(
        "Enter the updated prize pool of the eSport Event in USD: ") or None

    query = """UPDATE ESportEvents
                  SET PrizePool = %(NewPrizePool)s
                WHERE EventID = %(EventToUpdate)s
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def UpdatePlayerWinnings(cur, con):
    raise NotImplementedError


def UpdateHandler(cur, con):
    # Define Handlers
    handlers = [
        UpdateVideoGameLatestPatch,
        AcquirementOfOrganization,
        AcquireOrganization,
        UpdateESportEventStartDate,
        UpdateESportEventEndDate,
        UpdateESportEventPrizePool,
        UpdatePlayerWinnings
    ]

    # Get operation to Perform
    print("1. Update VideoGame Latest Patch.")
    print("2. Update that an Organization is Acquired.")
    print("4. Update the start date of an ESportEvent.")
    print("5. Update the end date of an ESportEvent.")
    print("6. Update the prize pool of an ESportEvent.")
    print("7. Update the winnings of a player.")
    print("8. Go Back")

    ch = int(input("Enter choice: "))
    if ch == 8:
        return

    try:
        handlers[ch - 1](cur, con)
        con.commit()
        print("Update Successful.")
    except (IndexError, TypeError):
        print(f"Error: Invalid Option {ch}")
    except Exception as error:
        con.rollback()
        print("Failed to update the Database.")
        print(f"Error: {error}")
