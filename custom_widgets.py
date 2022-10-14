"""
file that contains custom widgets
"""
from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


# from settings_widget import settings_widget
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


class SettingsWidget(QDialog):
    DEFAULT_FONT_SIZE = 8
    """
    widget that provides settings options
    - font
    - font size
    - theme
    """

    def __init__(self, parent):
        QDialog.__init__(self, parent=parent)
        uic.loadUi('style/settings_widget.ui', self)
        self.setWindowTitle("Settings")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.clicked.connect(self.on_click)

        self.font = self.font_dialog.currentText()
        self.font_size = SettingsWidget.DEFAULT_FONT_SIZE
        self.theme = self.theme_group.checkedButton().objectName()

    def accept(self):
        self.font = self.font_dialog.currentText()
        self.font_size = int(self.font_size_spin_box.text())
        self.theme = self.theme_group.checkedButton().objectName()

    def on_click(self):
        # print(self.font, self.font_size)
        self.close()
