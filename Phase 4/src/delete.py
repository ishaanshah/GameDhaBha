""" Contains all the functions related to insertion of entities into the database """


def DeleteESportEvent(cur, con):
    """ Deletes a new ESportEvent from the database """
    # Get EventID of the event to delete
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the ESportEvent to delete: ") or None

    # Query to be executed
    query = """DELETE FROM ESportEvents
                     WHERE EventID = %(EventID)s
            """

    print("\nExecuting")
    print(query)

    # Execute Query
    cur.execute(query, row)


def DeleteHandler(cur, con):
    # Define handlers
    handlers = [
        DeleteESportEvent
    ]

    # Get operation to perform
    print("1. Delete ESport Event")
    print("2. Go Back")
    ch = int(input("Enter choice: "))
    if ch == 2:
        return

    try:
        handlers[ch-1](cur, con)
        con.commit()
        print("Deletion successful")
    except (IndexError, TypeError):
        print(f"Error: Invalid option {ch}")
    except Exception as error:
        con.rollback()
        print("Failed to delete from the Database")
        print(f"Error: {error}")
