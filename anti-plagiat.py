import sys

from custom_widgets import SettingsWidget

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QFileDialog, QLineEdit, QDialog, QPushButton, QWidget, QTextEdit,
    QFontDialog, QFontComboBox, QDialogButtonBox
)


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

        self.settings_window = SettingsWidget()
        self.set_dark_theme()

    def set_dark_theme(self):
        self.settings_window.setStyleSheet(open('style/dark_theme.css').read())
        self.setStyleSheet(open('style/dark_theme.css').read())

    def set_light_theme(self):
        self.settings_window.setStyleSheet(open('style/light_theme.css').read())
        self.setStyleSheet(open('style/light_theme.css').read())

    def click_on_history_btn(self):
        """
        open a new window with history of requests
        """

    def click_on_settings_btn(self):
        """
        open a new window with settings dialog
        """
        self.settings_window.show()

    def click_on_compare_btn(self):
        """
        call a compare function after click
        """

    def click_on_save_result_btn(self):
        """
        saves current compare attributes
        (equality percent, request time) to database
        """

    def levenshtein_distance(self, text1, text2):
        """
        finds levenshtein distance of two texts
        :param text1: first text
        :param text2: second text
        :return: levenshtein distance
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    antiplagiat = Antiplagiat()
    antiplagiat.show()
    sys.exit(app.exec())
