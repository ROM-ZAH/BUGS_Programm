
from PyQt5 import QtWidgets, QtCore
from interface.python_ui.referens_ui import Ui_Referens

class ReferensWindow(QtWidgets.QMainWindow, Ui_Referens):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text_error = ""

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(ReferensWindow, self).changeEvent(event)
