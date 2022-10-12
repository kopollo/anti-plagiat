"""
file that contains custom widgets
"""
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QFileDialog, QLineEdit, QDialog, QPushButton, QWidget, QTextEdit,
    QFontDialog, QFontComboBox, QDialogButtonBox, QPlainTextEdit
)
from PyQt5.QtCore import Qt


class DisplayTextWidget(QWidget):
    """
    Widget that allows to add text from file and to see that text
    """

    def __init__(self, parent):
        """
        Initialize DisplayTextWidget widget
        :param parent: allows to promote QWidget
        """
        super(DisplayTextWidget, self).__init__(parent=parent)

        self.open_file_dialog_btn = QPushButton('Add text from file', self)
        self.open_file_dialog_btn.clicked.connect(self.get_file)

        self.text = QPlainTextEdit(self)
        self.text.setStyleSheet("background-color: #2F3136;")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.open_file_dialog_btn)
        self.layout.addWidget(self.text)

    def get_file(self):
        """
        open text by file dialog and shows it in text widget
        """
        try:
            file = QFileDialog.getOpenFileName(self, 'Open file')
            file_path, file_type = file
            text = open(file_path).read()
            self.text.setPlainText(text)
        except FileNotFoundError:
            # maybe should save that info
            pass


class SettingsWidget(QWidget):
    """
    widget that provides settings options
    - font
    - font size
    - theme
    """
    def __init__(self):
        super().__init__()
        uic.loadUi('style/settings_widget.ui', self)
        self.setWindowTitle("Settings")
        self.setWindowModality(Qt.ApplicationModal)
        self.buttonBox.clicked.connect(self.on_click)

    def on_click(self):
        print('x')
