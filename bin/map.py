import json

from PyQt5 import QtCore, QtWidgets, QtGui
import io
import folium
import openpyxl as opxl

from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtWebEngineWidgets import QWebEngineView
from os import listdir
from os.path import isfile, join
from bin.interface.python_ui.map_ui import Ui_MapWindow

class ContextTest:
    instructions = []
class Label(QtWidgets.QLabel):
    def __init__(self, parent = None):
        super(Label, self).__init__(parent=parent)
        self.name_pic = "../output data/pictures/DJI_0415.jpg"

    def setName(self, name):
        print("set")
        self.name_pic = name
        print(self.name_pic)
        #self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        print("paintEvent")
        print(self.name_pic[:-4] + ".json")

        with open(self.name_pic[:-4] + ".json", "r") as read_file:
            data_now_pic = json.load(read_file)
        print("1")
        painter = QPainter(self)
        painter.begin(self)  # +++


        painter.setPen(QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine))
        print("go - ", len(data_now_pic["targets"]))
        for i in range(len(data_now_pic["targets"])):
            print(i)
            self.paintAll(self.name_pic, painter)

        painter.end()  # +++

    def paintAll(self, name_pic, painter):

        print("rect")
        print(name_pic[:-4] + ".json")

        with open(name_pic[:-4] + ".json", "r") as read_file:
            data_now_pic = json.load(read_file)
        for i in range(len(data_now_pic["targets"])):
            x = data_now_pic["targets"][i]["polygon"]
            cords = []
            num = ''
            for i in x:
                if i.isdigit():
                    num += i
                else:
                    if num != '':
                        cords.append(int(num))
                        num = ''
            print(data_now_pic)
            print(x)
            print(cords)

            w_s = cords[0]
            h_s = cords[1]
            w_e = cords[4] - cords[0]
            h_e = cords[5] - cords[1]

            self.k_w = 741 / 4000
            self.k_h = 481 / 2250
            print(self.k_w, self.k_h)
            print(int(w_s), int(h_s), int(w_e), int(h_e))
            print(int(w_s) * self.k_w, int(h_s) * self.k_h, int(w_e) * self.k_w, int(h_e) * self.k_h)
            painter.drawRect(int(w_s * self.k_w), int(h_s * self.k_h), int(w_e * self.k_w), int(h_e * self.k_h))
            print("paint")

class MapWindow(QtWidgets.QMainWindow, Ui_MapWindow):

    def __init__(self):
        super(MapWindow, self).__init__()
        print("init")
        self.setupUi(self)



        self.label = Label(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 348, 741, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/DJI_0295.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.add_functions()
        self.do_buttons()


        self.qpixmax = QPixmap("../output data/pictures/DJI_0415.jpg")
    def add_functions(self):
        print("add")
        self.map_coords(48.03089, 37.68103)

    def do_buttons(self):
        print("ee")
        mypath = "intermediate data for AP telemetry and blur"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        for i in range(len(onlyfiles)):
            x = onlyfiles[i]
            print(x)
            self.x = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            self.x.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.x.setObjectName("x")
            self.x.setText(x)
            self.verticalLayout.addWidget(self.x)
            self.x.clicked.connect(lambda state, x = x: self.chek_img(x))

    def chek_img(self, name):
        print("start", name)

        wb = opxl.load_workbook("D:/BUGS_Programm/input data/telemetry/05.10.2022.xlsx")
        sheet = wb['Лист1']
        onlyfiles2 = [f for f in listdir("../input data/aerial photography") if isfile(join("../input data/aerial photography", f))]
        for i in range(len(onlyfiles2)):
            if name == sheet['A' + str(i + 1)].value:
                number_in_telemetry = i
                break

        x = sheet['B' +  str(number_in_telemetry + 1)].value
        y = sheet['C' +  str(number_in_telemetry + 1)].value

        name_pic = "../output data/pictures/" + name


        print(x, y, name_pic, name)

        self.qpixmax = QPixmap(name_pic)
        self.map_coords(x, y)
        self.label.setName(name_pic)

        self.label.setPixmap(self.qpixmax)


    def map_coords(self, x, y):
        coords = (x, y)

        m = folium.Map(
            title="lol",
            zoom_start=20,
            location=coords
        )

        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        for i in reversed(range(self.verticalLayout_map.count())):
            self.verticalLayout_map.itemAt(i).widget().setParent(None)
        self.verticalLayout_map.addWidget(webView)





