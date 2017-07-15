import logging
logger=logging.getLogger(__file__)

import sqlite3

def createdb_file_integ_check(abs_filename):
    logger.info("Trying to create db for file_watch at {}".format(abs_filename))
    try:
        connection=sqlite3.connect(abs_filename)
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE file_watch (id INTEGER PRIMARY KEY,file TEXT, hash TEXT);")
        connection.commit()
        connection.close()
        logger.info("Database successfully created at {}".format(abs_filename))
    except Exception as e:
        logger.error("Failed to create database, {}".format(e))
