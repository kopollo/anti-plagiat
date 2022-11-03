"""Main package, that creates main window with all logic."""
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from custom_widgets import SettingsWidget, HistoryWidget, UserComparisonItem
from algo import get_diff_percent
from antiplagiat_db import UserComparisonStorageDB


class Antiplagiat(QMainWindow):
    """Main class that describe Antiplagiat system."""

    def __init__(self):
        """Initialize main window of Antiplagiat, sets window title."""
        super().__init__()
        uic.loadUi('style/main_widget.ui', self)
        self.setWindowTitle("Antiplagiat")

        self.settings_btn.clicked.connect(self.click_on_settings_btn)
        self.history_btn.clicked.connect(self.click_on_history_btn)
        self.compare_text_btn.clicked.connect(self.click_on_compare_btn)
        self.save_result_btn.clicked.connect(self.click_on_save_result_btn)

        self.settings_window = SettingsWidget(self)
        self.history = HistoryWidget(self)

        self.db_of_compares = UserComparisonStorageDB()
        self.init_storage_by_db()

        self.show_user_warning(False)
        self.was_compare_btn_clicked = False

    def show_user_warning(self, ok: bool):
        """
        Show warning, if user forgot to click compare btn.

        :param ok: should we hide it or show
        """
        self.user_forget_label.setHidden(not ok)

    def click_on_history_btn(self):
        """Open a new window with history of requests."""
        self.history.exec()

    def click_on_settings_btn(self):
        """Open a new window with settings dialog."""
        self.settings_window.exec()

    def click_on_compare_btn(self):
        """Call a compare function for source codes after click."""
        self.show_user_warning(False)
        self.user_click_manager(self.click_on_compare_btn)

        diff = get_diff_percent(
            self.first_compared_text.get_text(),
            self.second_compared_text.get_text()
        )
        self.result_label.setText(str(diff))

    def init_storage_by_db(self):
        """Load user compares from previous sections."""
        for row in self.db_of_compares.get_compare_info():
            self.history.add_item_to_list(UserComparisonItem(*row[1:]))

    def reload_db(self):
        """Delete first element in db queue and updates user history widget."""
        self.db_of_compares.delete_first_elem()
        self.history.clear()
        self.init_storage_by_db()

    def generate_formatted_datetime(self):
        """
        Generate current date time in format '%Y-%m-%d - %H:%M:%S'.

        :return: string
        """
        return datetime.now().strftime('%Y-%m-%d - %H:%M:%S')

    def user_click_manager(self, func_of_click):
        """
        Implement a simple logger to control user.

        :param func_of_click: function what was clicked
        """
        if func_of_click == self.click_on_compare_btn:
            self.was_compare_btn_clicked = True
        elif func_of_click == self.click_on_save_result_btn:
            self.was_compare_btn_clicked = False
        else:
            pass

    def click_on_save_result_btn(self):
        """
        Save current compare attributes
        (source codes, equality percent, request time) to database
        and user local storage.
        """
        if not self.was_compare_btn_clicked:
            self.show_user_warning(True)
            return False

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

        self.user_click_manager(self.click_on_save_result_btn)
