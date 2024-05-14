from PyQt5 import QtCore, QtWidgets, QtGui

from bin.FiltersAndGenerations import telemetry_filter, blur_filter

import os
import shutil

from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap

from bin.FiltersAndGenerations.statistics import StatisticsWindow
from settings import SettingsWindow
from error import ErrorWindow

import time

from interface.python_ui.filter_ui import Ui_filter_Window
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog


class GenerationThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.percent = 0
        self.max_height = 5
        self.mydir_telemetry = ''
        self.mydir_img = ''
        self.mydir_save = ''
        self.max_fm = 30

    def getPercent(self):
        return self.percent

    def setPercent(self, percent):
        self.percent = percent
        print(self.percent)


    def init_thread(self, height, mydir_telemetry, mydir_img, mydir_save, max_fm):
        self.max_height = height
        self.mydir_telemetry = mydir_telemetry
        self.mydir_img = mydir_img
        self.mydir_save = mydir_save
        self.max_fm = max_fm

        print("init_thread_________h", self.max_height)


    def run(self):
        print("go")
        print("RUN_thread_________h", self.max_height)

        start_time = time.time()
        pixmax = QPixmap("interface/imges/zelenaja-galochka.png")

        print(self.mainwindow.settings.hight)
        telemetry_filter.start_telemetry_filter(self.mydir_telemetry, self.mydir_img, self.mydir_save, self.max_height, self)
        self.mainwindow.t_f_1.setPixmap(pixmax)
        self.mainwindow.t_f_2.setText(str(time.time() - start_time))
        time.sleep(0.5)
        start_time = time.time()
        blur_filter.start_blur_filter(self.mydir_save, self.max_fm, self)
        self.mainwindow.b_f_1.setPixmap(pixmax)
        self.mainwindow.b_f_2.setText(str(time.time() - start_time))
        time.sleep(0.5)

class MainWindow(QtWidgets.QMainWindow, Ui_filter_Window):
    def __init__(self):
        super().__init__()
        print("init22")
        self.setupUi(self)

        self.max_height = 5
        self.max_fm = 30
        self.stat = StatisticsWindow()
        self.error = ErrorWindow()
        self.mydir_telemetry = ""
        self.mydir_img = ""
        self.mydir_save = ""
        self.currBlur = 300
        self.isGeneration = False
        self.settings = SettingsWindow()
        self.add_functions()

    def setHeight(self, value):
        self.max_height = value
        print("_________h", self.max_height)

    def setFm(self, value):
        self.max_fm = value
        print("_________fm", self.max_fm)
        print("_________fm", self.max_fm)

    def changeEvent(self, event):
        print("1")
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(MainWindow, self).changeEvent(event)


    def setProgressBar(self):
        print('set progress bar')
        currentPercent = self.generation_instance.getPercent()
        print('Progress is :', str(currentPercent))
        self.progressBar.setValue(int(currentPercent))
        print("set")

    def add_functions(self):
        self.generation_instance = GenerationThread(mainwindow=self)

        self.button_telemetry.clicked.connect(self.on_click_select_folder_telemetry)
        self.button_images.clicked.connect(self.on_click_select_folder_img)
        self.button_save.clicked.connect(self.on_click_select_folder_save)
        self.button_generation.clicked.connect(self.launch_generation_thread)
        self.button_generation.clicked.connect(self.style_generetion)
        self.button_satistics.clicked.connect(self.go_stats_window)

    def style_generetion(self):
        self.t_f_1.setPixmap(QtGui.QPixmap(":/images/interface/imges/krestik.png"))
        self.b_f_1.setPixmap(QtGui.QPixmap(":/images/interface/imges/krestik.png"))
        self.t_f_2.setText("-")
        self.b_f_2.setText("-")

    def genThreadFinished(self):
        self.button_generation.setStyleSheet("background-color: rgb(225,225,225);")
        self.button_generation.setText("start")
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
            if os.path.exists(self.mydir_save + "/intermediate data for AP telemetry and blur") != True:
                print("save ---- " + self.mydir_save + "/intermediate data for AP telemetry and blur")
                os.mkdir(self.mydir_save + "/intermediate data for AP telemetry and blur")
            print("ok2")
            if self.mydir_save == "" or self.mydir_telemetry == "" or self.mydir_img == "":
                print("error")
                self.openErrorWindow("One of the paths for generation is not entered")
            else:
                self.timer = QTimer()
                self.timer.timeout.connect(self.setProgressBar)

                self.generation_instance.init_thread(height=self.max_height, mydir_telemetry=self.mydir_telemetry, mydir_img=self.mydir_img, mydir_save=self.mydir_save, max_fm=self.max_fm)
                self.generation_instance.finished.connect(self.genThreadFinished)
                self.generation_instance.start()
                self.button_generation.setStyleSheet("background-color: rgb(240, 100, 100);")
                self.button_generation.setText("Отменить")
                self.isGeneration = True
                self.timer.start(300)
                # self.progressBar_generation.setValue(50)
        else:
            print("delll-----------------------------")
            self.generation_instance.terminate()
            shutil.rmtree(self.mydir_save + '/pictures')
            shutil.rmtree(self.mydir_save + '/statistics')
            shutil.rmtree(self.mydir_save + '/intermediate data for AP telemetry and blur')
            self.progressBar.setValue(0)

    def go_settings_window(self):
        self.settings.show()

    def go_stats_window(self):
        self.stat.setTXT()
        self.stat.show()
        self.hide()
        self.stat.pushButton.clicked.connect(self.go_back_to_main_from_stat)

    def go_back_to_main_from_stat(self):
        self.stat.close()
        self.show()


    def on_click_select_folder_telemetry(self):
        dialog = QFileDialog()
        self.mydir_telemetry = QFileDialog.getOpenFileName()[0]
        print(self.mydir_telemetry)
        self.path_telemetry_text_2.setText(self.mydir_telemetry)

    def on_click_select_folder_img(self):
        dialog = QFileDialog()
        self.mydir_img = dialog.getExistingDirectory()
        self.path_directiry_img_text_2.setText(self.mydir_img)

    def on_click_select_folder_save(self):
        dialog = QFileDialog()
        self.mydir_save = dialog.getExistingDirectory()
        self.path_directiry_save_2.setText(self.mydir_save)
        self.stat.setDirSave(self.mydir_save)



