import subprocess

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog

from interface.python_ui.analisys_bug_ui import Ui_analysis_bug_Window
class AnalisysBugWindow(QtWidgets.QMainWindow, Ui_analysis_bug_Window):
    def __init__(self):
        super().__init__()
        self.mydir_weight = ""
        self.mydir_img = ""
        self.mydir_save = ""
        self.setupUi(self)
        self.add_functions()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)
        super(AnalisysBugWindow, self).changeEvent(event)

    def add_functions(self):
        self.button_weight.clicked.connect(self.on_click_select_weight)
        self.button_images.clicked.connect(self.on_click_select_folder_img)
        self.button_save.clicked.connect(self.on_click_select_folder_save)
        self.button_generation.clicked.connect(self.on_click_start)

    def on_click_start(self):
        subprocess.run(['python', '../dummy neural network/neural_network.py', self.mydir_weight, self.mydir_img, self.mydir_save])
    def on_click_select_weight(self):
        self.mydir_weight = QFileDialog.getOpenFileName()[0]
        print(self.mydir_weight)
        self.path_weight_text.setText(self.mydir_weight)

    def on_click_select_folder_img(self):
        dialog = QFileDialog()
        self.mydir_img = dialog.getExistingDirectory()
        self.path_directiry_img.setText(self.mydir_img)

    def on_click_select_folder_save(self):
        dialog = QFileDialog()
        self.mydir_save = dialog.getExistingDirectory()
        self.path_directiry_save.setText(self.mydir_save)