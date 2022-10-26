"""
Main package, which unite all widgets and work with them
"""
import sys
from datetime import datetime
from PyQt5 import uic, QtGui

from custom_widgets import *
from algo import *
from antiplagiat_db import *


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

        self.user_forget_label.setHidden(True)

        self.settings_window = SettingsWidget(self)
        self.history = HistoryWidget(self)

        self.db_of_compares = UserComparisonStorageDB()
        self.init_storage_by_db()

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
            self.first_compared_text.get_text(),
            self.second_compared_text.get_text()
        )
        self.result_label.setText(str(diff))

    def init_storage_by_db(self):
        """
        Load user compares from previous sections
        """
        for row in self.db_of_compares.get_compare_info():
            self.history.add_item_to_list(UserComparisonItem(*row[1:]))

    def reload_db(self):
        """
        deletes first element in db queue and updates user history widget
        """
        self.db_of_compares.delete_first_elem()
        self.history.clear()
        self.init_storage_by_db()

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
        self.db_of_compares.add_item_to_db(item)

        if self.db_of_compares.is_too_long_queue():
            self.reload_db()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    antiplagiat = Antiplagiat()
    antiplagiat.show()
    sys.exit(app.exec())
