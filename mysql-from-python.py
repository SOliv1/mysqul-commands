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
        rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        # Note that the above will still display a warning (not error) if the
        # table already exists
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()