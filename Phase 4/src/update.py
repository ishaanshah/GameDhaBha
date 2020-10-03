"""Contains all the functions related to the updation of enitities into the database"""


def UpdateVideoGameLatestPatch(cur, con):
    raise NotImplementedError


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
        print("Insertion Successful.")
    except (IndexError, TypeError):
        print(f"Error: Invalid Option {ch}")
    except Exception as error:
        con.rollback()
        print("Failed to insert into the Database.")
        print(f"Error: {error}")
