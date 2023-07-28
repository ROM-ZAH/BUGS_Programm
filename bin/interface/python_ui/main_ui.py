from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/imges/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Заголовок
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(40, 20, 641, 31))
        font = QtGui.QFont()
        font.setFamily("News706 BT")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")

        # Кнопка поиска пути к телеметрии
        self.button_telemetry = QtWidgets.QPushButton(self.centralwidget)
        self.button_telemetry.setGeometry(QtCore.QRect(10, 60, 200, 40))
        self.button_telemetry.setObjectName("button_telemetry")
        self.path_telemetry_text_1 = QtWidgets.QLabel(self.centralwidget)
        self.path_telemetry_text_1.setGeometry(QtCore.QRect(250, 60, 71, 40))
        self.path_telemetry_text_1.setObjectName("path_telemetry_text_1")
        self.path_telemetry_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.path_telemetry_text_2.setGeometry(QtCore.QRect(320, 60, 351, 40))
        self.path_telemetry_text_2.setObjectName("path_telemetry_text_2")

        # Кнопка поиска директори к изображениям\
        self.button_images = QtWidgets.QPushButton(self.centralwidget)
        self.button_images.setGeometry(QtCore.QRect(10, 110, 200, 40))
        self.button_images.setObjectName("button_images")
        self.path_directiry_img_text_1 = QtWidgets.QLabel(self.centralwidget)
        self.path_directiry_img_text_1.setGeometry(QtCore.QRect(250, 110, 91, 40))
        self.path_directiry_img_text_1.setObjectName("path_directiry_img_text_1")
        self.path_directiry_img_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.path_directiry_img_text_2.setGeometry(QtCore.QRect(340, 110, 321, 40))
        self.path_directiry_img_text_2.setObjectName("path_directiry_img_text_2")

        # Кнопка поиска директори к сохранению корпуса данных
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(10, 160, 200, 40))
        self.button_save.setObjectName("button_save")
        self.path_directiry_save_2 = QtWidgets.QLabel(self.centralwidget)
        self.path_directiry_save_2.setGeometry(QtCore.QRect(340, 160, 321, 40))
        self.path_directiry_save_2.setObjectName("path_directiry_save_2")
        self.path_directiry_save_1 = QtWidgets.QLabel(self.centralwidget)
        self.path_directiry_save_1.setGeometry(QtCore.QRect(250, 160, 91, 40))
        self.path_directiry_save_1.setObjectName("path_directiry_save_1")

        # Прогресс бар
        self.progressBar_generation = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_generation.setGeometry(QtCore.QRect(10, 210, 671, 41))
        self.progressBar_generation.setProperty("value", 0)
        self.progressBar_generation.setTextVisible(False)
        self.progressBar_generation.setObjectName("progressBar_generation")



        # Кнопка генерации
        self.button_generation = QtWidgets.QPushButton(self.centralwidget)
        self.button_generation.setGeometry(QtCore.QRect(10, 210, 671, 41))
        self.button_generation.setFlat(True)
        self.button_generation.setObjectName("button_generation")

        # Кнопка типо прогрессбара для фильтра телеметрии
        self.telemetry_filtr = QtWidgets.QLabel(self.centralwidget)
        self.telemetry_filtr.setGeometry(QtCore.QRect(10, 260, 90, 30))
        self.telemetry_filtr.setObjectName("telemetry_filtr")
        self.telemetry_filtr = QtWidgets.QLabel(self.centralwidget)
        self.telemetry_filtr.setGeometry(QtCore.QRect(10, 260, 90, 30))
        self.telemetry_filtr.setObjectName("telemetry_filtr")
        self.t_f_1 = QtWidgets.QLabel(self.centralwidget)
        self.t_f_1.setGeometry(QtCore.QRect(150, 260, 21, 21))
        self.t_f_1.setPixmap(QtGui.QPixmap(":/img/zelenaja-galochka.png"))
        self.t_f_1.setScaledContents(True)
        self.t_f_1.setObjectName("t_f_1")
        self.t_f_2 = QtWidgets.QLabel(self.centralwidget)
        self.t_f_2.setGeometry(QtCore.QRect(180, 260, 300, 30))
        self.t_f_2.setObjectName("t_f_2")

        # Кнопка типо прогрессбара для фильтра смазанности
        self.blur_filtr = QtWidgets.QLabel(self.centralwidget)
        self.blur_filtr.setGeometry(QtCore.QRect(10, 290, 91, 31))
        self.blur_filtr.setObjectName("blur_filtr")
        self.b_f_1 = QtWidgets.QLabel(self.centralwidget)
        self.b_f_1.setGeometry(QtCore.QRect(150, 290, 21, 21))
        self.b_f_1.setPixmap(QtGui.QPixmap(":/img/zelenaja-galochka.png"))
        self.b_f_1.setScaledContents(True)
        self.b_f_1.setObjectName("b_f_1")
        self.b_f_2 = QtWidgets.QLabel(self.centralwidget)
        self.b_f_2.setGeometry(QtCore.QRect(180, 290, 300, 30))
        self.b_f_2.setObjectName("b_f_2")

        # Кнопка типо прогрессбара для телеметрии для синтеза данных
        self.data_corpu_generation = QtWidgets.QLabel(self.centralwidget)
        self.data_corpu_generation.setGeometry(QtCore.QRect(10, 320, 121, 31))
        self.data_corpu_generation.setObjectName("data_corpu_generation")
        self.dc_g_1 = QtWidgets.QLabel(self.centralwidget)
        self.dc_g_1.setGeometry(QtCore.QRect(150, 320, 21, 21))
        self.dc_g_1.setPixmap(QtGui.QPixmap(":/img/zelenaja-galochka.png"))
        self.dc_g_1.setScaledContents(True)
        self.dc_g_1.setObjectName("dc_g_1")
        self.dc_g_2 = QtWidgets.QLabel(self.centralwidget)
        self.dc_g_2.setGeometry(QtCore.QRect(180, 320, 300, 30))
        self.dc_g_2.setObjectName("dc_g_2")

        # Кнопка статистики
        self.button_satistics = QtWidgets.QPushButton(self.centralwidget)
        self.button_satistics.setGeometry(QtCore.QRect(10, 360, 331, 31))
        self.button_satistics.setObjectName("button_satistics")

        # Кнопка карты
        self.button_map = QtWidgets.QPushButton(self.centralwidget)
        self.button_map.setGeometry(QtCore.QRect(360, 360, 321, 31))
        self.button_map.setObjectName("button_map")


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BUG"))
        self.Title.setText(_translate("MainWindow", "Data corpus selection and synthesis program for neural networks"))
        self.path_telemetry_text_1.setText(_translate("MainWindow", "Path to file -"))
        self.button_telemetry.setText(_translate("MainWindow", "Selecting a file with telemetry"))
        self.path_directiry_img_text_1.setText(_translate("MainWindow", "Path to directory -  "))
        self.button_images.setText(_translate("MainWindow", "Path to the directory with images"))
        self.button_generation.setText(_translate("MainWindow", "Data generation"))
        self.button_satistics.setText(_translate("MainWindow", "Statistics"))
        self.button_map.setText(_translate("MainWindow", "map"))
        self.button_save.setText(_translate("MainWindow", "Path to save data corpus and statistics"))
        self.path_directiry_save_1.setText(_translate("MainWindow", "Path to directory -  "))
        self.telemetry_filtr.setText(_translate("MainWindow", "Telemetry filter"))
        self.blur_filtr.setText(_translate("MainWindow", "Blur filter"))
        self.data_corpu_generation.setText(_translate("MainWindow", "Data corpus generation"))
        self.b_f_2.setText(_translate("MainWindow", "-"))
        self.dc_g_2.setText(_translate("MainWindow", "-"))
        self.t_f_2.setText(_translate("MainWindow", "-"))
        self.t_f_1.setText("")
        self.b_f_1.setText("")
        self.dc_g_1.setText("")
        self.path_directiry_img_text_2.setText("")
        self.path_directiry_save_2.setText("")
        self.path_telemetry_text_2.setText("")
