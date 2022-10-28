"""File that contains custom widgets."""
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QPlainTextEdit, QVBoxLayout,
    QFileDialog, QDialog, QListWidgetItem
)
from PyQt5.QtCore import QSize


class DisplayTextWidget(QWidget):
    """Widget that allows to add text from file and to see that text."""
    DEFAULT_TAB_SIZE = 4

    def __init__(self, parent):
        """
        Initialize DisplayTextWidget widget.

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

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.open_file_dialog_btn)
        self.layout.addWidget(self.text_widget)

    def text_changed(self):
        """Update attributes when text changed."""
        self.text = self.text_widget.toPlainText()

    def get_text(self):
        """Return text on QPlainTextEdit."""
        return self.text

    def set_text(self, text):
        """Set text on QPlainTextEdit."""
        self.text_widget.setPlainText(text)

    def get_file_by_dialog(self):
        """Open text by file dialog and shows it in text widget."""
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
    Widget that provides settings options
    - font
    - font size
    - theme

    """
    DEFAULT_FONT = "Times"
    DEFAULT_FONT_SIZE = 11
    DEFAULT_THEME = "light"

    def __init__(self, parent):
        """
        Initialize Settings window of Antiplagiat, base font, font size, theme.

        :param parent: widget that promotes settings
        """
        QDialog.__init__(self, parent=parent)
        uic.loadUi('style/settings_widget.ui', self)
        self.setWindowTitle("Settings")

        self.buttonBox.accepted.connect(self.click_accept)
        self.buttonBox.rejected.connect(self.reject)

        self.font = SettingsWidget.DEFAULT_FONT
        self.font_size = SettingsWidget.DEFAULT_FONT_SIZE
        self.theme = SettingsWidget.DEFAULT_THEME

        self.init_user_settings()

    def init_user_settings(self):
        """Initialize settings from earlier sessions."""
        with open("user_settings_info.txt") as fin:
            lines = fin.readlines()
        lines = tuple([line.strip() for line in lines])

        self.font, self.font_size, self.theme = lines
        self.set_style()

    def save_user_settings(self):
        """Save user settings into file."""
        with open("user_settings_info.txt", mode="w") as out:
            print(self.font, file=out)
            print(self.font_size, file=out)
            print(self.theme, file=out)

    def click_accept(self):
        """Change font, font-size, theme."""
        self.font = self.font_dialog.currentText()
        try:
            self.font_size = int(self.font_size_spin_box.text())
        except TypeError:
            # not number
            pass
        self.theme = self.theme_group.checkedButton().objectName()

        self.set_style()
        self.close()

    def set_style(self):
        """Set theme, font, font size."""
        self.parent().setStyleSheet(self.generate_css_for_interface())

        self.save_user_settings()

    def generate_css_for_interface(self):
        """
        Generate css for font, font size, theme.

        :return: css file
        """
        font_size = int(self.font_size)
        font = self.font
        font_in_qss = f'font-size: {font_size}px; font-family: {font};'
        cur_font = f"QWidget {{{font_in_qss}}}"
        return self.theme_file_manager() + cur_font

    def theme_file_manager(self):
        """
        Choose theme file by theme title.

        :return: css file
        """
        theme_file_name = "style/light_theme.css"
        if self.theme == "dark":
            theme_file_name = "style/dark_theme.css"
        return open(theme_file_name).read()


class UserComparisonItem(QWidget):
    """
    Item which provides following attributes:
    - first source code
    - second source code
    - difference percent
    - data & time

    """

    def __init__(self,
                 first_source_code,
                 second_source_code,
                 equality_percent,
                 date_time,
                 parent=None
                 ):
        """
        Initialize object with following attributes.

        :param first_source_code:
        :param second_source_code:
        :param equality_percent:
        :param date_time:
        :param parent:
        """
        super().__init__(parent)
        uic.loadUi('style/user_comparison_widget.ui', self)

        self.first_source_code.setPlainText(first_source_code)
        self.second_source_code.setPlainText(second_source_code)
        self.equality_percent_label.setText(str(equality_percent))
        self.date_time_label.setText(date_time)

    def get_comparison_info(self):
        """
        Get a tuple of attributes of UserComparisonItem.

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
        Initialize History Widget of Antiplagiat, sets window title.

        :param parent: a widget that needs a history window
        """
        super().__init__(parent)
        uic.loadUi('style/user_history_widget.ui', self)
        self.setWindowTitle("User History")
        self.user_compare_list.itemDoubleClicked.connect(self.reproduce_compare)

    def add_item_to_list(self, item: UserComparisonItem):
        """
        Append in list widget item.

        :param item: object that we want to add in list
        """
        list_item = QListWidgetItem(self.user_compare_list)
        list_item.setSizeHint(QSize(*HistoryWidget.LIST_ITEM_SIZE))
        self.user_compare_list.addItem(list_item)
        self.user_compare_list.setItemWidget(list_item, item)

    def get_list_item(self):
        """
        Allow to take widget from QListWidget.

        :return: widget
        """
        item = self.user_compare_list.currentItem()
        widget = self.user_compare_list.itemWidget(item)
        return widget

    def reproduce_compare(self):
        """Transfer source codes from list into main window."""
        widget = self.get_list_item()
        txt1, txt2, percent, datetime = widget.get_comparison_info()

        self.parent().first_compared_text.set_text(txt1)
        self.parent().second_compared_text.set_text(txt2)

        self.close()

    def clear(self):
        """Clear current list items."""
        self.user_compare_list.clear()
