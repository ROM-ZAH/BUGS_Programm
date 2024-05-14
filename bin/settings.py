import os
import shutil
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QFileDialog

from bin import data_synthesis
from bin.FiltersAndGenerations.statistics import StatisticsWindow
from interface.python_ui.settings_ui import Ui_SettingsWindow
from PyQt5 import QtCore, QtWidgets
class GenerationThread_2(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.percent = 0
        self.mydir_telemetry = ''
        self.mydir_img = ''
        self.mydir_save = ''

    def getPercent(self):
        return self.percent

    def setPercent(self, percent):
        self.percent = percent
        print(self.percent)


    def init_thread(self, mydir_telemetry, mydir_img, mydir_save):
        self.mydir_telemetry = mydir_telemetry
        self.mydir_img = mydir_img
        self.mydir_save = mydir_save



    def run(self):
        print("go")
        print("RUN_thread_________")
        data_synthesis.start_data_synthesis(self.mydir_telemetry, self.mydir_img, self.mydir_save, self)
        print("END_thread_________")

class SettingsWindow(QtWidgets.QMainWindow, Ui_SettingsWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.setupUi(self)
        self.want_close = True

        self.stat = StatisticsWindow()
        self.isGeneration = False

        self.hight = 5
        self.blur = 30
        self.many = 8
        self.few = 5
        self.spinBox_hight.setValue(self.hight)
        self.spinBox_blur.setValue(self.blur)
        self.spinBox_Many.setValue(self.many)
        self.spinBox_Few.setValue(self.few)

        self.trans = QtCore.QTranslator(self)

        self.comboBox_Language_settings.currentIndexChanged.connect(self.change_func)

        self.options = ([('English', ''), ('Русский', 'interface/python_ui/eng-ru'),])

        for i, (text, lang) in enumerate(self.options):
            self.comboBox_Language_settings.addItem(text)
            self.comboBox_Language_settings.setItemData(i, lang)

        self.add_funct()

    def add_funct(self):
        self.generation_instance = GenerationThread_2(mainwindow=self)
        self.pushButton_telemetry.clicked.connect(self.on_click_select_folder_telemetry)
        self.pushButton_img.clicked.connect(self.on_click_select_folder_img)
        self.pushButton_save.clicked.connect(self.on_click_select_folder_save)
        self.pushButton_statistics.clicked.connect(self.go_stats_window)
        self.pushButton_start.clicked.connect(self.launch_generation_thread)

    def want_to_close(self):
        if self.few < self.many and self.few >= 0:
            self.want_close = True
        else:
            self.want_close = False
    def change_func(self, index):
        data = self.comboBox_Language_settings.itemData(index)
        print("tut")
        print(data)
        if data:
            print("ok")
            self.trans.load(data)
            QtCore.QCoreApplication.instance().installTranslator(self.trans)
        else:
            QtCore.QCoreApplication.instance().removeTranslator(self.trans)
        print("da")
    def changeEvent(self, event):
        print("change")
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(SettingsWindow, self).changeEvent(event)
        print("ok")
    def closeEvent(self, event: QCloseEvent):
        if self.want_close:
            event.accept()
        else:
            event.ignore()

    def go_stats_window(self):
        self.stat.setTXT()
        self.stat.show()
        self.hide();
        self.stat.pushButton.clicked.connect(self.go_back_to_main_from_stat)
    def go_back_to_main_from_stat(self):
        self.stat.close()
        self.show()
    def on_click_select_folder_telemetry(self):
        dialog = QFileDialog()
        self.mydir_telemetry = QFileDialog.getOpenFileName()[0]
        print(self.mydir_telemetry)
        self.label_telemetry.setText(self.mydir_telemetry)

    def on_click_select_folder_img(self):
        dialog = QFileDialog()
        self.mydir_img = dialog.getExistingDirectory()
        self.label_img.setText(self.mydir_img)

    def on_click_select_folder_save(self):
        dialog = QFileDialog()
        self.mydir_save = dialog.getExistingDirectory()
        self.label_save.setText(self.mydir_save)
        self.stat.setDirSave(self.mydir_save)

    def genThreadFinished(self):
        self.setProgressBar();
        self.pushButton_start.setStyleSheet("background-color: rgb(225,225,225);")
        self.pushButton_start.setText("start")
        self.isGeneration = False
        self.timer.stop()


    def launch_generation_thread(self):
        if self.isGeneration == False:
            if os.path.exists(self.mydir_save + "/pictures") == False:
                print("save ---- " + self.mydir_save + "/pictures")
                os.mkdir(self.mydir_save + "/pictures")
                text_file = open(self.mydir_save + "/pictures/img.qrc", "w")
            if os.path.exists(self.mydir_save + "/statistics") != True:
                print("save ---- " + self.mydir_save + "/statistics")
                os.mkdir(self.mydir_save + "/statistics")
            print("ok2")
            if self.mydir_save == "" or self.mydir_telemetry == "" or self.mydir_img == "":
                print("error")
                self.openErrorWindow("One of the paths for generation is not entered")
            else:
                self.timer = QTimer()
                self.timer.timeout.connect(self.setProgressBar)
                print("Progress bar: OK")
                self.generation_instance.init_thread(mydir_telemetry=self.mydir_telemetry, mydir_img=self.mydir_img, mydir_save=self.mydir_save)
                print("Init thread : OK")
                self.generation_instance.finished.connect(self.genThreadFinished)
                print("Thread connect: OK")
                self.generation_instance.start()
                print("Thread start : OK")
                self.pushButton_start.setStyleSheet("background-color: rgb(240, 100, 100);")
                self.pushButton_start.setText("Отменить")
                self.isGeneration = True
                self.timer.start(300)
                # self.progressBar_generation.setValue(50)
        else:
            print("delll-----------------------------")
            self.generation_instance.terminate()
            shutil.rmtree(self.mydir_save + '/pictures')
            shutil.rmtree(self.mydir_save + '/statistics')
            self.progressBar.setValue(0)

    def setProgressBar(self):
        print('set progress bar')
        currentPercent = self.generation_instance.getPercent()
        print('Progress is :', str(currentPercent))
        self.progressBar.setValue(int(currentPercent))
        print("set")
