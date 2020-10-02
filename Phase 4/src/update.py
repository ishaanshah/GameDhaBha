"""Contains all the functions related to the updation of enitities into the database"""

def UpdateVideoGameLatestPatch(cur, con):
    raise NotImplementedError

def AcquirementOfOrganization(cur, con):
    raise NotImplementedError

def AcquireOrganization(cur, con):
    raise NotImplementedError

def UpdateESportEventStartDate(cur, con):
    raise NotImplementedError

def UpdateESportEventEndDate(cur, con):
    raise NotImplementedError

def UpdateESportEventPrizePool(cur, con):
    raise NotImplementedError

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
        UpdatePlayerWinnings
    ]

    # Get operation to Perform
    print("1. Update VideoGame Latest Patch.")
    print("2. Update that an Organization is Acquired.")
    print("3. Update that an Organization Acquires another Organization.")
    print("4. Update the start date of an ESportEvent.")
    print("5. Update the end date of an ESportEvent.")
    print("6. Update the winnings of a player.")
    print("7. Go Back")

    ch = int(input("Enter choice: "))
    if ch == 9:
        return;

    try:
        handlers[ch - 1] (cur, con)
        con.commit()
        print("Insertion Successful.")
    except (IndexError, TypeError):
        print(f"Error: Invalid Option {ch}")
    except Exception as error:
        con.rollback()
        print("Failed to insert into the Database.")
        print(f"Error: {error}")
