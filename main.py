"""Entry file for project to run by console."""
import sys

from PyQt5.QtWidgets import QApplication

from antiplagiat import Antiplagiat

if __name__ == '__main__':
    app = QApplication(sys.argv)
    antiplagiat = Antiplagiat()
    antiplagiat.show()
    sys.exit(app.exec())
