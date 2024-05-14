
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMessageBox

from interface.python_ui.start_ui import Ui_MainMainWindow

from map import MapWindow
from filter import MainWindow
from settings import SettingsWindow
from analisys_bug import AnalisysBugWindow
from analisys_diseases import AnalisysDiseasesWindow
from referense import ReferensWindow
from PyQt5.QtWinExtras import QtWin

class StartWindow(QtWidgets.QMainWindow, Ui_MainMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Map = MapWindow()
        self.Main = MainWindow()
        self.settings = SettingsWindow()
        self.AnalysisBug = AnalisysBugWindow()
        self.AnalysisDiseases = AnalisysDiseasesWindow()
        self.Referense = ReferensWindow()

        self.add_func()

        myappid = 'mycompany.myproduct.subproduct.version'  # !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!

    def go_settings_window(self):
        self.settings.show()
    def add_func(self):
        self.pushButton_analiz.clicked.connect(self.go_map_window)
        self.pushButton_generate.clicked.connect(self.go_gen_window)
        self.pushButton_settings.clicked.connect(self.go_settings_window)
        self.pushButton_search_bug.clicked.connect(self.go_search_bug_window)
        self.pushButton_sear_diseases.clicked.connect(self.go_search_diseases_window)
        self.pushButton_2.clicked.connect(self.go_reference_window)


        self.settings.spinBox_hight.valueChanged.connect(self.Main.setHeight)
        self.settings.spinBox_blur.valueChanged.connect(self.Main.setFm)
        self.settings.spinBox_Many.valueChanged.connect(self.Map.setMany)
        self.settings.spinBox_Few.valueChanged.connect(self.Map.setFew)

    def go_search_bug_window(self):
        self.AnalysisBug.show()
        self.hide()
        self.AnalysisBug.pushButton.clicked.connect(self.go_back_to_start_from_analisys_bug)

    def go_reference_window(self):
        self.Referense.show()


    def go_search_diseases_window(self):
        self.AnalysisDiseases.show()
        self.hide()
        self.AnalysisDiseases.pushButton.clicked.connect(self.go_back_to_start_from_analisys_disease)

    def go_back_to_start_from_analisys_bug(self):
        self.AnalysisBug.close()
        self.show()

    def go_back_to_start_from_analisys_disease(self):
        self.AnalysisDiseases.close()
        self.show()
    def go_map_window(self):
        self.Map.show()
        self.hide()
        self.Map.pushButton.clicked.connect(self.go_back_to_start_from_map)

    def go_back_to_start_from_map(self):
        self.Map.close()
        self.show()

    def go_gen_window(self):
        self.Main.show()
        self.hide()
        self.Main.button_map.clicked.connect(self.go_back_to_start_from_main)

    def go_back_to_start_from_main(self):
        self.Main.close()
        self.show()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(StartWindow, self).changeEvent(event)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = StartWindow()
    w.show()
    sys.exit(app.exec_())
