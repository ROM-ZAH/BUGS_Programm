
from PIL import Image

import os
import cv2

def load_a_start_pic_grass():
    fon = []
    names = []
    dir = "intermediate data for AP telemetry"
    fon_names = os.listdir(dir)
    for i in range(len(fon_names)):
        fon.append(dir + "/" + fon_names[i])
        names.append(fon_names[i])

    return fon, names

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

'''
Входные данные: массив содержущий пути до файлов
Выходные данные: создаёт файл в которые записывает подходяще файлы
'''
def telemetry_and_blur_filter(mas_path ,mas_names, mydir_save, genThred):
    normal = 0
    bad = 0
    max_Laplace_dispersion = 310
    for i in range(len(mas_path)):
        image = cv2.imread(mas_path[i])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)

        if fm > max_Laplace_dispersion:
            normal += 1
            with Image.open(mas_path[i]) as img:
                img.load()
            img.save("intermediate data for AP telemetry and blur/" + mas_names[i])
        else:
            bad += 1
        genThred.setPercent((i + 1) * 100 / len(mas_path))
    f = open(mydir_save + "/statistics/statistics.txt", "a")
    f.write("\n========================BLUR FILTER STATS=========================\n")
    f.write("Number of images including telemetry filter " + str(normal + bad) + "\n")
    f.write("Number of blurry pictures (Laplace dispersion limit " + str(max_Laplace_dispersion) + ") - " + str(bad) + "\n")
    f.write("Number of clear pictures (Laplace dispersion limit " + str(max_Laplace_dispersion) + ") - " + str(normal) + "\n")
    f.write("Percentage of clear pictures - " + str(int((normal / (normal + bad))*100)) + "%\n")
    f.close()

def start_blur_filter(mydir_save, genThred):
    print("start blur")
    Trava, names = load_a_start_pic_grass()
    print(genThred)
    telemetry_and_blur_filter(Trava, names, mydir_save, genThred)