#!/usr/bin/python3

"""
This module contains one script
The script lists all state with a name starting with N from a database
It uses the MySQLdb module
"""

import MySQLdb
import sys

if __name__ == '__main__':
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
    query = "SELECT * FROM states  WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch rows
    states_with_N = cursor.fetchall()
    for state in states_with_N:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
