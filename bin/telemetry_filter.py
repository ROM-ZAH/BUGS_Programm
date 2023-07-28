
from PIL import Image, ImageFilter
import os
import openpyxl as opxl

from main import GenerationThread


def load_a_start_pic_grass(mydir_img):
    fon = []
    names = []
    fon_names = os.listdir(mydir_img)
    for i in range(len(fon_names)):
        fon.append(mydir_img + "/" + fon_names[i])
        names.append(fon_names[i])

    return fon, names

'''
Входные данные: массив содержущий пути до файлов
Выходные данные: создаёт файл в которые записывает подходяще файлы
'''
def telemetry_filter(mas_path ,mas_names, sheet, mydir_save, genThred = GenerationThread):
    normal = 0
    bad = 0
    max_height = 3.5
    for i in range(len(mas_path)):
        for j in range(len(mas_names)):
            if mas_names[i] == sheet['A' + str(j + 1)].value:
                number_in_telemetry = j
                break
        if sheet['F' + str(number_in_telemetry + 1)].value < max_height:
            normal += 1
            with Image.open(mas_path[i]) as img:
                img.load()
            img.save("intermediate data for AP telemetry/" + mas_names[i])
        else:
            bad += 1
        genThred.setPercent((i + 1) * 100 / len(mas_path))
    if os.path.isfile(mydir_save + "/statistics/statistics.txt"):
        os.remove(mydir_save + "/statistics/statistics.txt")
    f = open(mydir_save + "/statistics/statistics.txt", "a")
    f.write("\n====================FILTER TELEMETRY STATISTICS===================\n")
    f.write("Number of pictures " + str(normal + bad) + "\n")
    f.write("The number of images with a height of " + str(max_height) + "m and above - " + str(bad) + "\n")
    f.write("The number of images with a height of " + str(max_height) + "m and below - " + str(normal) + "\n")
    f.write("Percentage of images matching telemetry parameters - " + str(int((normal / (normal + bad))*100)) + "%\n")
    f.close()
def start_telemetry_filter(mydir_telemetry, mydir_img, mydir_save, genThred = GenerationThread):
    print("start telemetry")
    Trava, names = load_a_start_pic_grass(mydir_img)
    wb = opxl.load_workbook(mydir_telemetry)
    sheet = wb['Лист1']

    telemetry_filter(Trava, names, sheet, mydir_save, genThred)


