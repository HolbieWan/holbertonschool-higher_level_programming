#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb

def get_all_states():
    """Method that lists all states from the database hbtn_0e_0_usa"""

    # Database connection parameters
    host = 'localhost'
    user = ''
    password = ''
    database = 'hbtn_0e_0_usa'
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
    my_query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(my_query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_all_states()
