#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def get_all_N_states():
    """Method that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

    # Database connection parameters
    host = 'localhost'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306

    # Establish the connection
    conn = MySQLdb.connect(
        host=host,
        user=user,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Perform a SELECT query
    my_query = "SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC"
    cursor.execute(my_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_all_N_states()
