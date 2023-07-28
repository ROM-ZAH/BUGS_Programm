
from PyQt5 import QtWidgets
from bin.interface.python_ui.statistics_ui import Ui_Statistics
class StatisticsWindow(QtWidgets.QMainWindow, Ui_Statistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


