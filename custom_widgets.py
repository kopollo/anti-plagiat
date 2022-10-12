"""
file that contains custom widgets
"""
from PyQt5.QtWidgets import (
    QFileDialog, QLineEdit, QDialog, QPushButton, QWidget, QPlainTextEdit,
    QVBoxLayout
)


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
