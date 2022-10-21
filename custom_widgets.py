"""
file that contains custom widgets
"""
import csv

from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize


class DisplayTextWidget(QWidget):
    """
    Widget that allows to add text from file and to see that text
    """
    DEFAULT_TAB_SIZE = 4

    def __init__(self, parent):
        """
        Initialize DisplayTextWidget widget
        :param parent: allows to promote QWidget
        """
        super(DisplayTextWidget, self).__init__(parent=parent)

        self.open_file_dialog_btn = QPushButton('Add text from file', self)
        self.open_file_dialog_btn.clicked.connect(self.get_file)

        self.text_widget = QPlainTextEdit(self)
        self.text_widget.textChanged.connect(self.text_changed)
        self.text_widget.setTabStopWidth(
            self.text_widget.fontMetrics().width(' ')
            * DisplayTextWidget.DEFAULT_TAB_SIZE
        )
        self.text = self.text_widget.toPlainText()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.open_file_dialog_btn)
        self.layout.addWidget(self.text_widget)

    def text_changed(self):
        self.text = self.text_widget.toPlainText()

    def get_file(self):
        """
        open text by file dialog and shows it in text widget
        """
        try:
            file = QFileDialog.getOpenFileName(self, 'Open file')
            file_path, file_type = file
            text = open(file_path).read()
            self.text_widget.setPlainText(text)
            self.text = self.text_widget.toPlainText()
        except FileNotFoundError:
            # maybe should save that info
            pass


class SettingsWidget(QDialog):
    """
    widget that provides settings options
    - font
    - font size
    - theme
    """
    DEFAULT_FONT_SIZE = 11

    def __init__(self, parent):
        """
        Initialize Settings window of Antiplagiat, base font, font size, theme
        :param parent: widget that promotes settings
        """
        QDialog.__init__(self, parent=parent)
        uic.loadUi('style/settings_widget.ui', self)
        self.setWindowTitle("Settings")

        self.buttonBox.accepted.connect(self.click_accept)
        self.buttonBox.rejected.connect(self.reject)

        self.font = self.font_dialog.currentText()
        self.font_size = SettingsWidget.DEFAULT_FONT_SIZE
        self.theme = self.theme_group.checkedButton().objectName()

    def click_accept(self):
        """
        changes font, font-size, theme
        """
        self.font = self.font_dialog.currentText()
        self.font_size = int(self.font_size_spin_box.text())
        self.theme = self.theme_group.checkedButton().objectName()
        self.close()


class HistoryWidget(QDialog):
    """
    Widget which provides user saved compares with the following fields:
    - first source code
    - second source code
    - difference percent
    - data & time
    """
    def __init__(self, parent):
        """
        Initialize History Widget of Antiplagiat, sets window title
        :param parent: a widget that needs a history window
        """
        super().__init__(parent)
        uic.loadUi('style/user_history_widget.ui', self)
        self.setWindowTitle("User Histore")
        self.listWidget.itemDoubleClicked.connect(self.reproduce_compare)

    def add_item_to_list(self, item):
        """
        appends in list widget item
        :param item: object that we want to add in list
        """
        list_item = QListWidgetItem(self.listWidget)
        list_item.setSizeHint(QSize(200, 70))
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, item)

    def reproduce_compare(self):
        """
        transfer source codes from list into main window
        """
        # for ch in self.listWidget.currentItem.listWidget().children():
        #     pass
        # print()
        # item = self.listWidget.currentItem()
        # QListWidgetItem.
        # print(item.listWidget())
        # print(self.parent().first_compared_text.setPlain)
        self.close()


class UserComparisonItem(QWidget):
    """
    Item which provides following attributes:
    - first source code
    - second source code
    - difference percent
    - data & time
    """
    def __init__(self, txt, txt2, percent, datetime, parent=None): #WILL RENAME
        """
        Initialize object with following attributes:
        :param txt:
        :param txt2:
        :param percent:
        :param datetime:
        :param parent:
        """
        super().__init__(parent)
        uic.loadUi('style/user_comparison_widget.ui', self)

        self.first_source_code.setPlainText(txt)
        self.second_source_code.setPlainText(txt2)
        self.equality_percent_label.setText(percent)
        self.date_time_label.setText(datetime)