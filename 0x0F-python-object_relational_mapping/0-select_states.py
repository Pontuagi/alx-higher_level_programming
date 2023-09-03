#!/usr/bin/python3

"""
This module contains a single script
The script lists all states from a database
It uses the MySQLdb module
"""
import MySQLdb

if __name__ == "__main__":
    import sys

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
