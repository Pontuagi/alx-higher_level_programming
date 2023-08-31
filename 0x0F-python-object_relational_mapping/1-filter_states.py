#!/usr/bin/python3

"""
This module contains one script
The script lists all state with a name starting with N from a database
It uses the MySQLdb module
"""

import MySQLdb
import sys


def list_states_with_N():
    """
    This function lists all states starting with N
    The database used is hbtn_0e_0_usa
    """
    if len(sys.argv) != 4:
        return

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
    query = "SELECT FROM states  WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch rows
    states_with_N = cursor.fetchall()
    for state in states_with_N:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_with_N()
