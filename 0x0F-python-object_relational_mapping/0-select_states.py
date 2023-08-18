#!/usr/bin/python3

"""
This module contains a single script
The script lists all states from a database
It uses the MySQLdb module
"""
import MySQLdb

def list_states(username, password, database):
    """
    This function lists all states from the database hbtn_0e_0_usa
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
    passwd=password, db=database)

    #create cursor
    cursor = db.cursor()

    # Execute the query
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch the rows
    states = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    db.close()

    # Display the results
    print("States:")
    for state in states:
        print(state)


if __name__ == "__main__":
    username = 'Pontuagi'
    password = '@Pass017'
    database = 'hbtn_0e_0_usa'

    list_states(username, password, database)
