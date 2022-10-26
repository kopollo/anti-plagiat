import sqlite3
import sys
from datetime import datetime
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
)

from custom_widgets import *
from algo import *


class Antiplagiat(QMainWindow):
    """
    Main class that describe Antiplagiat system
    """

    def __init__(self):
        """
        Initialize main window of Antiplagiat, sets window title
        """
        super().__init__()
        uic.loadUi('style/main_widget.ui', self)
        self.setWindowTitle("Antiplagiat")

        self.settings_btn.clicked.connect(self.click_on_settings_btn)
        self.history_btn.clicked.connect(self.click_on_history_btn)
        self.compare_text_btn.clicked.connect(self.click_on_compare_btn)
        self.save_result_btn.clicked.connect(self.click_on_save_result_btn)

        self.settings_window = SettingsWidget(self)

        self.history = HistoryWidget(self)

        self.dbname = "user_comparison_storage.db"

        self.init_storage_by_db()

    def init_storage_by_db(self):
        """
        Load user compares from previous sections
        """
        connection = sqlite3.connect(self.dbname)
        cursor = connection.cursor()
        query = '''
            SELECT *
            FROM comparison
        '''
        cursor.execute(query)
        for row in cursor.fetchall():
            self.history.add_item_to_list(UserComparisonItem(*row[1:]))

    def click_on_history_btn(self):
        """
        open a new window with history of requests
        """
        self.history.exec()

    def click_on_settings_btn(self):
        """
        open a new window with settings dialog
        """
        self.settings_window.exec()

    def click_on_compare_btn(self):
        """
        call a compare function for source codes after click
        """

        diff = get_diff_percent(
            self.first_compared_text.text,
            self.second_compared_text.text
        )
        self.result_label.setText(str(diff))

    def generate_formatted_datetime(self):
        """
        generates current date time by
        expression '%Y-%m-%d - %H:%M:%S'
        :return: string
        """
        return datetime.now().strftime('%Y-%m-%d - %H:%M:%S')

    def click_on_save_result_btn(self):
        """
        saves current compare attributes
        (source codes, equality percent, request time) to database
        and user local storage
        """
        percent = self.result_label.text()
        date = self.generate_formatted_datetime()
        item = UserComparisonItem(
            self.first_compared_text.get_text(),
            self.second_compared_text.get_text(),
            percent,
            date,
            self)

        self.history.add_item_to_list(item)
        self.add_item_to_db(item)

    def add_item_to_db(self, item: UserComparisonItem):
        """
        adds item to database of user compares
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    antiplagiat = Antiplagiat()
    antiplagiat.show()
    sys.exit(app.exec())
