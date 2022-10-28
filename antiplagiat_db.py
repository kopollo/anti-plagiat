"""
package that contains database of user comparisons.

"""
import sqlite3
from custom_widgets import UserComparisonItem


class UserComparisonStorageDB:
    """class that provides work with database."""

    def __init__(self):
        """Initialize UserComparisonStorageDB."""
        self.dbname = "user_comparison_storage.db"

    def get_compare_info(self):
        """
        Get user compare information from db.

        :return: following attributes from database
        - first source code
        - second source code
        - difference percent
        - data & time
        """
        connection = sqlite3.connect(self.dbname)
        cursor = connection.cursor()
        query = '''
            SELECT *
            FROM comparison
        '''
        cursor.execute(query)
        return cursor.fetchall()

    def is_too_long_queue(self):
        """
        Check if we have more than 10 saves.

        :return: True if we have, False if not
        """
        if self.get_db_size() > 10:
            return True
        return False

    def add_item_to_db(self, item: UserComparisonItem):
        """
        Add item to database of user compares.

        :param item: what we will insert
        """
        connection = sqlite3.connect(self.dbname)
        cursor = connection.cursor()
        query = '''
        INSERT INTO comparison(
            first_compared_source,
            second_compared_source,
            similarity_percentage,
            date_time)
        VALUES(?,?,?,?)
        '''
        cursor.execute(query, item.get_comparison_info())
        connection.commit()
        connection.close()

    def delete_first_elem(self):
        """Delete first record from db."""
        connection = sqlite3.connect(self.dbname)
        cursor = connection.cursor()
        query = '''
            DELETE FROM comparison
            WHERE rowid IN
        (SELECT rowid FROM comparison limit 1);
        '''
        cursor.execute(query)
        connection.commit()
        connection.close()

    def get_db_size(self):
        """
        Get number of rows in db.

        :return: db size
        """
        connection = sqlite3.connect(self.dbname)
        cursor = connection.cursor()
        query = '''
          SELECT COUNT(*) FROM comparison
        '''
        cursor.execute(query)
        size = cursor.fetchall()[0][0]
        return size
