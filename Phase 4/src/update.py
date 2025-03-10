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
    """ Updates the 'Owns' relationship to reflect acquirement of an Organisation """
    # Get details about the acquirement
    row = {}
    row["ParentID"] = input(
        "Enter OrganisationID of parent organistion: ") or None
    row["SubsidiaryID"] = input(
        "Enter OrganisationID of subsidiary organistion: ") or None
    row["AcquiredOn"] = input(
        "Enter the date when acquirement took place in YYYY-MM-DD format: ") or None

    query = """INSERT INTO Owns(ParentID, SubsidiaryID, AcquiredOn)
                    VALUES (%(ParentID)s, %(SubsidiaryID)s, %(AcquiredOn)s)
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def UpdateESportEventStartDate(cur, con):
    """ Updates the Start Date of en ESportEvent """
    # Get details about the update
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the ESportEvent whose start date needs to be changed: ") or None
    row["StartDate"] = input(
        "Enter the new start date of the ESportEvent: ") or None

    query = """UPDATE ESportEvents
                  SET StartDate = %(StartDate)s
                WHERE EventID = %(EventID)s
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def UpdateESportEventEndDate(cur, con):
    """ Updates the End Date of en ESportEvent """
    # Get details about the update
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the ESportEvent whose end date needs to be changed: ") or None
    row["EndDate"] = input(
        "Enter the new end date of the ESportEvent: ") or None

    query = """UPDATE ESportEvents
                  SET EndDate = %(EndDate)s
                WHERE EventID = %(EventID)s
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def UpdateESportEventPrizePool(cur, con):
    """ Updates the prize pool for an eSport Event in the database """
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
    """ Updates the winnings for a Player in the database """
    # Get the winnings
    row = {}
    row["PlayerToUpdate"] = input(
        "Enter the Player ID of the Player whose "
        "winnings has to be updated: ") or None
    row["NewWinnings"] = input(
        "Enter the updated winnings of the Player in USD: ") or None

    query = """UPDATE Players
                  SET Winnings = %(NewWinnings)s
                WHERE PlayerID = %(PlayerToUpdate)s
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def UpdateHandler(cur, con):
    # Define Handlers
    handlers = [
        UpdateVideoGameLatestPatch,
        AcquirementOfOrganization,
        UpdateESportEventStartDate,
        UpdateESportEventEndDate,
        UpdateESportEventPrizePool,
        UpdatePlayerWinnings
    ]

    # Get operation to Perform
    print("1. Update VideoGame Latest Patch.")
    print("2. Update that an Organization is Acquired.")
    print("3. Update the start date of an ESportEvent.")
    print("4. Update the end date of an ESportEvent.")
    print("5. Update the prize pool of an ESportEvent.")
    print("6. Update the winnings of a player.")
    print("7. Go Back")

    ch = int(input("Enter choice: "))
    if ch == 7:
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
