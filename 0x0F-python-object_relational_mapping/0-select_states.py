#!/usr/bin/python3

"""
This module contains a single script
The script lists all states from a database
It uses the MySQLdb module
"""
import MySQLdb
import sys


def list_states():
    """
    This function lists all states from the database hbtn_0e_0_usa
    """
    if len(sys.argv) != 4:
        return

    # username = sys.argv[1]
    # password = sys.argv[2]
    # database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # create cursor
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

    if __name == "__main__":
        list_states()
