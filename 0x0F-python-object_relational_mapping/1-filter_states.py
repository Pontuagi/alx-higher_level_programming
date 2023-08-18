#!/usr/bin/python3

"""
This module contains one script
The script lists all state with a name starting with N from a database
It uses the MySQLdb module
"""

import MySQLdb
import sys


def list_states_with_N(username, password, database):
    """
    This function lists all states starting with N
    The database used is hbtn_0e_0_usa
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
# Create cursor
    cursor = db.cursor()

# Execute query
    query = "SELECT FROM states  WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cursor.execute(query)

# Fetch rows
    states_with_N = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    db.close()

    # Display the results
    print("states starting with 'N':")
    for state in states_with_N:
        print(state)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <passwoed> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_with_N(username, password, database)
