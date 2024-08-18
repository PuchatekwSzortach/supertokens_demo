"""
Invoke commands to be run inside the backend container
"""

import invoke


@invoke.task
def clean_state(_context, config_path):
    """
    Command to clean system state

    Args:
        _context (invoke.Context): context instance
        config_path: path to configuration file
    """

    import mysql.connector

    import utilities

    config = utilities.load_config(config_path)

    mysql_connection = mysql.connector.connect(
        host=config.database.docker_network.host,
        port=config.database.docker_network.port,
        user=config.database.username,
        password=config.database.password,
        database=config.database.supertokens_database
    )

    utilities.truncate_mysql_tables(mysql_connection)
