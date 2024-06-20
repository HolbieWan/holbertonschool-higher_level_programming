#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is safe from MySQL injections"""

import MySQLdb
import sys


def get_all_N_states():
    """Method that takes in arguments and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument"""

    # Database connection parameters
    host = 'localhost'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
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
    my_query = "SELECT * FROM states WHERE\
        name = %s ORDER BY id ASC"
    cursor.execute(my_query, (state_name,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_all_N_states()
