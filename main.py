import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QButtonGroup,
    QCalendarWidget,
)


class PlannerWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widget.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    planner = PlannerWidget()
    planner.show()
    sys.exit(app.exec())
