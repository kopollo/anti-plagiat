"""File that contains error widgets"""
from PyQt5.QtWidgets import QMessageBox


class FileNotFoundWidget(QMessageBox):
    """Widget shows error message"""
    def __init__(self):
        """Load message that user delete some files"""
        super().__init__()
        self.setWindowTitle("Antiplagiat")
        self.setText('Looks like you delete something important\n'
                     'Return file or reload app')
