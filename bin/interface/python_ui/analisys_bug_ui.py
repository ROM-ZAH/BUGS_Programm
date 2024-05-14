# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analisys_bug.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analysis_bug_Window(object):
    def setupUi(self, analysis_bug_Window):
        analysis_bug_Window.setObjectName("analysis_bug_Window")
        analysis_bug_Window.resize(713, 173)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/interface/imges/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        analysis_bug_Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(analysis_bug_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout.addWidget(self.Title)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.button_weight = QtWidgets.QPushButton(self.centralwidget)
        self.button_weight.setMinimumSize(QtCore.QSize(22, 22))
        self.button_weight.setMaximumSize(QtCore.QSize(22, 22))
        self.button_weight.setObjectName("button_weight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.button_weight)
        self.path_weight_text = QtWidgets.QLabel(self.centralwidget)
        self.path_weight_text.setObjectName("path_weight_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.path_weight_text)
        self.button_images = QtWidgets.QPushButton(self.centralwidget)
        self.button_images.setMinimumSize(QtCore.QSize(22, 22))
        self.button_images.setMaximumSize(QtCore.QSize(22, 22))
        self.button_images.setObjectName("button_images")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.button_images)
        self.path_directiry_img = QtWidgets.QLabel(self.centralwidget)
        self.path_directiry_img.setObjectName("path_directiry_img")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.path_directiry_img)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setMinimumSize(QtCore.QSize(22, 22))
        self.button_save.setMaximumSize(QtCore.QSize(22, 22))
        self.button_save.setText("...")
        self.button_save.setObjectName("button_save")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.button_save)
        self.path_directiry_save = QtWidgets.QLabel(self.centralwidget)
        self.path_directiry_save.setObjectName("path_directiry_save")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.path_directiry_save)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_generation = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.button_generation.sizePolicy().hasHeightForWidth())
        self.button_generation.setSizePolicy(sizePolicy)
        self.button_generation.setMinimumSize(QtCore.QSize(54, 22))
        self.button_generation.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_generation.setFont(font)
        self.button_generation.setAutoFillBackground(False)
        self.button_generation.setFlat(False)
        self.button_generation.setObjectName("button_generation")
        self.horizontalLayout.addWidget(self.button_generation)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        analysis_bug_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(analysis_bug_Window)
        QtCore.QMetaObject.connectSlotsByName(analysis_bug_Window)

    def retranslateUi(self, analysis_bug_Window):
        _translate = QtCore.QCoreApplication.translate
        analysis_bug_Window.setWindowTitle(_translate("analysis_bug_Window", "Analysis of auto discovery results"))
        self.Title.setText(_translate("analysis_bug_Window", "Automatic search for beetles"))
        self.button_weight.setText(_translate("analysis_bug_Window", "..."))
        self.path_weight_text.setText(_translate("analysis_bug_Window", "Choose the path to the file with weights artificial neural network"))
        self.button_images.setText(_translate("analysis_bug_Window", "..."))
        self.path_directiry_img.setText(_translate("analysis_bug_Window", "Select the path to the input files directory"))
        self.path_directiry_save.setText(_translate("analysis_bug_Window", "Select path to output directory"))
        self.button_generation.setText(_translate("analysis_bug_Window", "Start"))
        self.pushButton.setText(_translate("analysis_bug_Window", "Back to main menu"))
import foto_rc