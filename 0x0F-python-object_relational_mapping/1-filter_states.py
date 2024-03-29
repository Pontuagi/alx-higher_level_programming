#!/usr/bin/python3

"""
This module contains one script
The script lists all state with a name starting with N from a database
It uses the MySQLdb module
"""

import MySQLdb

if __name__ == '__main__':
    import sys

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    # Create cursor
    cursor = db.cursor()

    # Execute query
    query = "SELECT * FROM states;"
    cursor.execute(query)

    # Fetch rows
    states_with_N = cursor.fetchall()
    for state in states_with_N:
        if state[1][0] == 'N':
            print(state)

    db.close()
