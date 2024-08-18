"""
Module with utilities
"""

import box
import mysql.connector
import yaml


def load_config(config_path: str) -> box.Box:
    """
    Load configuration file

    :param config_path: path to configuration file
    :return: configuration as a box object
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    return box.Box(config)


def truncate_mysql_tables(connection: mysql.connector.connection.MySQLConnection):
    """
    Truncate all tables in the database indicated by the connection

    :param connection: database connection
    """
    # Create a cursor object
    cursor = connection.cursor()

    try:

        # Disable foreign key checks, so we can truncate tables in any order
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

        # Execute the query to retrieve all table names
        cursor.execute("SHOW TABLES")

        # Fetch all table names
        tables = cursor.fetchall()

        # Truncate each table
        for table in tables:

            table_name = table[0]
            cursor.execute(f"TRUNCATE TABLE {table_name}")

    finally:

        # Reenable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        # Close the cursor
        cursor.close()
