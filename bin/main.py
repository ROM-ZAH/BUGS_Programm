
from PyQt5 import QtCore, QtWidgets

import telemetry_filter
import blur_filter
import data_synthesis
import os

from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap

from statistics import StatisticsWindow
from map import MapWindow
import time

from PyQt5.QtCore import QTimer,QDateTime
from bin.interface.python_ui.main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog

class GenerationThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.percent = 0  

    def getPercent(self):
        return self.percent

    def setPercent(self, percent):
        self.percent = percent
        print(self.percent)

    def run(self):
        print("go")
        start_time = time.time()
        pixmax = QPixmap("interface/imges/zelenaja-galochka.png")
        telemetry_filter.start_telemetry_filter(mydir_telemetry, mydir_img, mydir_save, self)
        self.mainwindow.t_f_1.setPixmap(pixmax)
        self.mainwindow.t_f_2.setText("time - " + str(time.time() - start_time) + " second")
        time.sleep(0.5)
        start_time = time.time()
        blur_filter.start_blur_filter(mydir_save, self)
        self.mainwindow.b_f_1.setPixmap(pixmax)
        self.mainwindow.b_f_2.setText("time - " + str(time.time() - start_time) + " second")
        time.sleep(0.5)
        start_time = time.time()
        data_synthesis.start_data_synthesis(mydir_telemetry, mydir_save, self)
        self.mainwindow.dc_g_1.setPixmap(pixmax)
        self.mainwindow.dc_g_2.setText("time - " + str(time.time() - start_time) + " second")
        time.sleep(0.5)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_functions()
        self.Map = MapWindow()
        self.stat = StatisticsWindow()

    def setProgressBar(self):
        print('set progress bar')
        currentPercent = self.generation_instance.getPercent()
        print('Progress is :', str(currentPercent))

        self.progressBar_generation.setValue(int(currentPercent))

    def add_functions(self):
        self.button_telemetry.clicked.connect(self.on_click_select_folder_telemetry)
        self.button_images.clicked.connect(self.on_click_select_folder_img)
        self.button_save.clicked.connect(self.on_click_select_folder_save)

        self.button_generation.clicked.connect(self.launch_generation_thread)
        self.generation_instance = GenerationThread(mainwindow=self)
        self.generation_instance.finished.connect(self.genThreadFinished)

        self.button_satistics.clicked.connect(self.go_stats_window)
        self.button_map.clicked.connect(self.go_map_window)

    def genThreadFinished(self):
        self.timer.stop()
        self.progressBar_generation.setValue(0)

    def launch_generation_thread(self):
        print("ok")
        self.timer = QTimer()
        self.timer.timeout.connect(self.setProgressBar)
        self.generation_instance.start()
        self.timer.start(300)
        # self.progressBar_generation.setValue(50)

    def go_stats_window(self):
        self.stat.show()
        self.close()
        self.stat.pushButton.clicked.connect(self.go_back_stat)

    def go_back_stat(self):
        self.stat.close()
        self.show()

    def go_back_map(self):
        self.Map.close()
        self.show()

    def go_map_window(self):
        self.Map.show()
        self.close()
        self.Map.pushButton.clicked.connect(self.go_back_map)

    def on_click_select_folder_telemetry(self):
        global mydir_telemetry
        dialog = QFileDialog()
        mydir_telemetry = QFileDialog.getOpenFileNames()[0][0]
        print(mydir_telemetry)
        self.path_telemetry_text_2.setText(mydir_telemetry)
        pass

    def on_click_select_folder_img(self):
        global mydir_img
        dialog = QFileDialog()
        mydir_img = dialog.getExistingDirectory()
        self.path_directiry_img_text_2.setText(mydir_img)

    def on_click_select_folder_save(self):
        global mydir_save
        dialog = QFileDialog()
        mydir_save = dialog.getExistingDirectory()

        if os.path.exists(mydir_save + "/pictures") == False:
            print("save ---- " + mydir_save + "/pictures")
            os.mkdir(mydir_save + "/pictures")
            text_file = open(mydir_save + "/pictures/img.qrc", "w")
        if os.path.exists(mydir_save + "/statistics") != True:
            print("save ---- " + mydir_save + "/statistics")
            os.mkdir(mydir_save + "/statistics")
        self.path_directiry_save_2.setText(mydir_save)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
