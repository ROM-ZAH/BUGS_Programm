
from PyQt5 import QtWidgets, QtCore
from interface.python_ui.error_ui import Ui_ErrorWindow

class ErrorWindow(QtWidgets.QMainWindow, Ui_ErrorWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text_error = ""
        self.label_error.setText(self.text_error)

    def setTextError(self, text):
        self.text_error = text

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(ErrorWindow, self).changeEvent(event)
