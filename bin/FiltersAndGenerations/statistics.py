
from PyQt5 import QtWidgets, QtCore
from ..interface.python_ui.statistics_ui import Ui_Statistics
class StatisticsWindow(QtWidgets.QMainWindow, Ui_Statistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dirSave = ""

    def setDirSave(self, dir):
        self.dirSave = dir

    def setTXT(self):
        f = open(self.dirSave + "/statistics/statistics.txt")
        text = f.read()
        print("Set txt: OK")
        print("Path: " + self.dirSave + "/statistics/statistics.txt")
        self.textBrowser.setText(text)

    def changeEvent(self, event):
        print("change event stat")
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(StatisticsWindow, self).changeEvent(event)

