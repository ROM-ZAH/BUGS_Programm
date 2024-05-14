# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MapWindow(object):
    def setupUi(self, MapWindow):
        MapWindow.setObjectName("MapWindow")
        MapWindow.resize(1350, 832)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/interface/imges/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MapWindow.setWindowIcon(icon)
        MapWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MapWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 921, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_map = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_map.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_map.setObjectName("verticalLayout_map")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_map.addWidget(self.label_8)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(951, 90, 140, 221))
        self.scrollArea.setMinimumSize(QtCore.QSize(140, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(181, 16777215))
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setToolTip("")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 138, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 561, 21))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 1071, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(861, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(140, 20))
        self.label_7.setMaximumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 305, 921, 41))
        self.label_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 370, 924, 451))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_pic = QtWidgets.QVBoxLayout()
        self.verticalLayout_pic.setObjectName("verticalLayout_pic")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMinimumSize(QtCore.QSize(777, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_pic.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_pic)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(950, 370, 142, 451))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_all_bugs = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_all_bugs.setMinimumSize(QtCore.QSize(140, 0))
        self.comboBox_all_bugs.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_all_bugs.setFocusPolicy(QtCore.Qt.TabFocus)
        self.comboBox_all_bugs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_all_bugs.setObjectName("comboBox_all_bugs")
        self.verticalLayout_2.addWidget(self.comboBox_all_bugs)
        self.listWidget_bugs = QtWidgets.QListWidget(self.layoutWidget2)
        self.listWidget_bugs.setProperty("showDropIndicator", True)
        self.listWidget_bugs.setProperty("isWrapping", False)
        self.listWidget_bugs.setUniformItemSizes(False)
        self.listWidget_bugs.setWordWrap(False)
        self.listWidget_bugs.setSelectionRectVisible(False)
        self.listWidget_bugs.setObjectName("listWidget_bugs")
        self.verticalLayout_2.addWidget(self.listWidget_bugs)
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(590, 330, 231, 21))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setText("")
        self.label_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 10, 1321, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_select_folder = QtWidgets.QPushButton(self.layoutWidget3)
        self.button_select_folder.setMinimumSize(QtCore.QSize(100, 22))
        self.button_select_folder.setMaximumSize(QtCore.QSize(22, 22))
        self.button_select_folder.setObjectName("button_select_folder")
        self.horizontalLayout.addWidget(self.button_select_folder)
        self.pushButton_telem = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_telem.setObjectName("pushButton_telem")
        self.horizontalLayout.addWidget(self.pushButton_telem)
        self.pushButton_delet_all = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_delet_all.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton_delet_all.setMaximumSize(QtCore.QSize(22, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_delet_all.setFont(font)
        self.pushButton_delet_all.setText("X")
        self.pushButton_delet_all.setObjectName("pushButton_delet_all")
        self.horizontalLayout.addWidget(self.pushButton_delet_all)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(22, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setText("<-")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1100, 50, 241, 21))
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1120, 80, 201, 231))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1100, 310, 241, 61))
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.textBrowser_Flight_statistic = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Flight_statistic.setGeometry(QtCore.QRect(1110, 80, 231, 231))
        self.textBrowser_Flight_statistic.setObjectName("textBrowser_Flight_statistic")
        self.textBrowser_disease_and_recom = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_disease_and_recom.setGeometry(QtCore.QRect(1110, 370, 231, 451))
        self.textBrowser_disease_and_recom.setObjectName("textBrowser_disease_and_recom")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.layoutWidget.raise_()
        self.scrollArea.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.layoutWidget.raise_()
        self.label_name.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_10.raise_()
        self.textBrowser_Flight_statistic.raise_()
        self.textBrowser_disease_and_recom.raise_()
        MapWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MapWindow)
        QtCore.QMetaObject.connectSlotsByName(MapWindow)

    def retranslateUi(self, MapWindow):
        _translate = QtCore.QCoreApplication.translate
        MapWindow.setWindowTitle(_translate("MapWindow", "MapWindow"))
        self.pushButton_2.setText(_translate("MapWindow", "1"))
        self.label_3.setText(_translate("MapWindow", "Image with beetles highlighted"))
        self.label_4.setText(_translate("MapWindow", "Map with highlighted semi-half points"))
        self.label_7.setText(_translate("MapWindow", "Buttons"))
        self.button_select_folder.setText(_translate("MapWindow", "Путь до изобр."))
        self.pushButton_telem.setText(_translate("MapWindow", "телеметрия"))
        self.label_9.setText(_translate("MapWindow", "Статистика по полёту"))
        self.label_10.setText(_translate("MapWindow", "Отчёт и рекомендации"))
        self.textBrowser_Flight_statistic.setHtml(_translate("MapWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Здесь должна быть статистика полетов</p></body></html>"))
        self.textBrowser_disease_and_recom.setHtml(_translate("MapWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Должны быть предположения о заболеваниях и рекомендации по их лечению.</p></body></html>"))
import foto_rc
