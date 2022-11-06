"""Entry file for project to run by console."""
import sys
from sqlite3 import OperationalError

from PyQt5.QtWidgets import QApplication

from antiplagiat import Antiplagiat
from error_widgets import FileNotFoundWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    err = FileNotFoundWidget()
    try:
        antiplagiat = Antiplagiat()
        antiplagiat.show()
        sys.exit(app.exec())
    except FileNotFoundError:
        err.exec()
    except OperationalError:
        err.exec()
