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
        self.open_file_dialog_btn.clicked.connect(self.get_file_by_dialog)

        self.text_widget = QPlainTextEdit(self)
        self.text_widget.textChanged.connect(self.text_changed)
        self.text_widget.setTabStopWidth(
            self.text_widget.fontMetrics().width(' ')
            * DisplayTextWidget.DEFAULT_TAB_SIZE
        )
        self.text = self.text_widget.toPlainText()

        self.is_text_changed = True

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.open_file_dialog_btn)
        self.layout.addWidget(self.text_widget)

    def text_changed(self):
        self.is_text_changed = True
        self.text = self.text_widget.toPlainText()

    def get_text(self):
        """
        :return: text on QPlainTextEdit
        """
        return self.text

    def set_text(self, text):
        """
        sets text on QPlainTextEdit
        """
        self.text_widget.setPlainText(text)

    def get_file_by_dialog(self):
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
    DEFAULT_FONT = "Times"
    DEFAULT_FONT_SIZE = 11
    DEFAULT_THEME = "light"

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

        self.font = SettingsWidget.DEFAULT_FONT
        self.font_size = SettingsWidget.DEFAULT_FONT
        self.theme = SettingsWidget.DEFAULT_THEME

        self.init_user_settings()

    def init_user_settings(self):
        with open("user_settings_info.txt") as fin:
            lines = fin.readlines()
        lines = tuple([line.strip() for line in lines])

        self.font, self.font_size, self.theme = lines
        self.set_style()

    def save_user_settings(self):
        with open("user_settings_info.txt", mode="w") as out:
            print(self.font, file=out)
            print(self.font_size, file=out)
            print(self.theme, file=out)

    def click_accept(self):
        """
        changes font, font-size, theme
        """
        self.font = self.font_dialog.currentText()
        self.font_size = int(self.font_size_spin_box.text())
        self.theme = self.theme_group.checkedButton().objectName()

        self.set_style()
        self.close()

    def set_style(self):
        """
        sets theme from css file
        """
        theme_file_name = "style/light_theme.css"
        if self.theme == "dark":
            theme_file_name = "style/dark_theme.css"

        font_size = int(self.font_size)
        font = self.font
        font_in_qss = f'font-size: {font_size}px; font-family: {font};'
        cur_font = f"QWidget {{{font_in_qss}}}"
        self.parent().setStyleSheet(open(theme_file_name).read() + cur_font)

        self.save_user_settings()


class UserComparisonItem(QWidget):
    """
    Item which provides following attributes:
    - first source code
    - second source code
    - difference percent
    - data & time
    """

    def __init__(self, txt, txt2, percent, datetime,
                 parent=None):  # сдлать **kwargs
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
        self.equality_percent_label.setText(str(percent))
        self.date_time_label.setText(datetime)

    def get_comparison_info(self):
        """
        gets a tuple of attributes of UserComparisonItem
        :return: tuple
        """
        return (
            self.first_source_code.toPlainText(),
            self.second_source_code.toPlainText(),
            self.equality_percent_label.text(),
            self.date_time_label.text(),
        )


class HistoryWidget(QDialog):
    """
    Widget which provides user saved compares with the following fields:
    - first source code
    - second source code
    - difference percent
    - data & time
    """
    LIST_ITEM_SIZE = (200, 70)

    def __init__(self, parent):
        """
        Initialize History Widget of Antiplagiat, sets window title
        :param parent: a widget that needs a history window
        """
        super().__init__(parent)
        uic.loadUi('style/user_history_widget.ui', self)
        self.setWindowTitle("User Histore")
        self.listWidget.itemDoubleClicked.connect(self.reproduce_compare)

    def add_item_to_list(self, item: UserComparisonItem):
        """
        appends in list widget item
        :param item: object that we want to add in list
        """
        list_item = QListWidgetItem(self.listWidget)
        list_item.setSizeHint(QSize(*HistoryWidget.LIST_ITEM_SIZE))
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, item)

    def get_list_item(self):
        """
        allows us to take widget from QListWidget
        :return: widget
        """
        item = self.listWidget.currentItem()
        widget = self.listWidget.itemWidget(item)
        return widget

    def reproduce_compare(self):
        """
        transfer source codes from list into main window
        """
        widget = self.get_list_item()

        txt1, txt2, percent, datetime = widget.get_comparison_info()

        self.parent().first_compared_text.set_text(txt1)
        self.parent().second_compared_text.set_text(txt2)

        self.close()
