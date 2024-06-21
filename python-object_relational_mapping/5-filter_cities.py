#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def get_all_cities_by_states():
    """Method that lists all cities from the database hbtn_0e_4_usa"""

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
    my_query = "SELECT cities.name FROM states\
        INNER JOIN cities ON states.id = cities.state_id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC"
    cursor.execute(my_query, (state_name,))
    rows = cursor.fetchall()

    # Manually construct the comma-separated string
    first = True
    city_string = ""
    for row in rows:
        if not first:
            city_string += ", "
        city_string += row[0]
        first = False

    # Print the result
    print(city_string)

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    get_all_cities_by_states()
