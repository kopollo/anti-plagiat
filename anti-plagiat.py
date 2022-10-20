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

        theme_file_name = "style/dark_theme.css"
        self.set_style(theme_file_name)

    def set_style(self, theme_file_name):
        """
        sets theme from css file
        """
        font_size = self.settings_window.font_size
        font = self.settings_window.font
        font_in_css = f'font-size: {font_size}px; font-family: {font};'
        cur_font = f"QWidget {{{font_in_css}}}"

        self.setStyleSheet(open(theme_file_name).read() + cur_font)

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
        theme_file_name = "style/light_theme.css"
        if self.settings_window.theme == "dark":
            theme_file_name = "style/dark_theme.css"

        self.set_style(theme_file_name)

    def click_on_compare_btn(self):
        """
        call a compare function after click
        """

        diff = get_diff_percent(
            self.first_compared_text.text,
            self.second_compared_text.text
        )
        self.result_label.setText(str(diff))

    def click_on_save_result_btn(self):
        """
        saves current compare attributes
        (equality percent, request time) to database
        and user local storage
        """
        # if (not self.first_compared_text.text and
        #         not self.second_compared_text.text):
        #     pass

        txt1 = self.first_compared_text.text  # RENAME RENAME
        txt2 = self.second_compared_text.text
        percent = self.result_label.text()
        date = datetime.now().strftime('%Y-%m-%d - %H:%M:%S')
        item = UserComparisonItem(txt1, txt2, percent, date, self)
        self.history.add_item_to_list(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    antiplagiat = Antiplagiat()
    antiplagiat.show()
    sys.exit(app.exec())
