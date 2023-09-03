#!/usr/bin/python3

"""
a script that takes in an argument
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb


if __name__ == "__main__":
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
        )

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()

    for state in states:
        print(state)
