import os
import datetime
import pymysql

# Get username from workspace if required
# (modify this variable if running on another environment)
username = os.getenv('Gitpod_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
# Run queries
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
        # Note that the above will still display a warning (not error) if the
        # table already exists
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()