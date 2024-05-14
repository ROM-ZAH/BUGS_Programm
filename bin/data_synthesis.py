
from PIL import Image, ImageFilter
from random import randint
import os
import math
import json
import datetime
import openpyxl as opxl


def some_parametr_of_JILUK(i, img_JILuk):
    if (i >= 0):
        st1 = st2 = cr1 = cr2 = 0
        cr3 = img_JILuk.width
        cr4 = img_JILuk.height
        threshold = 250
        x_start = 0
        x_end = 255
    else:
        st1 = st2 = cr1 = cr2 = cr3 = cr4 = threshold = x_start = x_end = -1

    return st1, st2, cr1, cr2, cr3, cr4, threshold, x_start, x_end
def erode(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MinFilter(3))
    return image
def dilate(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MaxFilter(3))
    return image
def do_a_JILuk(now_type_of_JILuk, number_bug):
    #print(now_type_of_JILuk)
    with Image.open(base_JILuk[now_type_of_JILuk][number_bug]) as img_JILuk:
        img_JILuk.load()
    st1, st2, cr1, cr2, cr3, cr4, threshold, x_start, x_end = some_parametr_of_JILUK(now_type_of_JILuk, img_JILuk)
    if st1 == -1:
        print("Fatal error")
        exit()
    JILuk = img_JILuk.crop((cr1, cr2, cr3, cr4))
    red, green, blue = JILuk.split()
    JILuk_threshold = red.point(
        lambda x: x_start if x > threshold else x_end
    )
    JILuk_threshold = JILuk_threshold.convert("1")
    # JILuk_threshold.show()

    step_1 = erode(st1, JILuk_threshold)
    # step_1.show()

    new_JILuk = dilate(st2, step_1)
    # new_JILuk.show()

    new_JILuk = new_JILuk.convert("L")
    new_JILuk = new_JILuk.filter(ImageFilter.BoxBlur(20))
    return JILuk, new_JILuk
    # new_JILuk.show()
def some_parametr_of_PIC(number_bug, img):
    if number_bug >= 0:
        rnd_x_min = 100
        rnd_x_max = img.width - 100
        rnd_y_min = 100
        rnd_y_max = img.height - 100
    else:
        rnd_x_min = rnd_x_max = rnd_y_min = rnd_y_max = -1
    return rnd_x_min, rnd_x_max, rnd_y_min, rnd_y_max
def do_reduce_0_0(img, img_JILuk, h, number_bug):
    with open("info.json", "r") as read_file:
        data_of_info = json.load(read_file)

    # print("i = ", i)
    max_size = int(data_of_info["classificator"][number_bug]["max_size"] * 2.4 * 1000)
    min_size = int((max_size / 1000 - data_of_info["classificator"][number_bug]["max_size"] + data_of_info["classificator"][number_bug]["min_size"]) * 1000)

    h = h * 1000

    size_of_JILuk = randint(min_size, max_size)
    How_pix_on_JILuk_in_fon = size_of_JILuk**2 * img.width**2 / (4 * math.tan(math.radians(data_of_info["Camera_angle"] / 2))**2 * h**2)
    reduce = img_JILuk.width * img_JILuk.height / How_pix_on_JILuk_in_fon

    if reduce == 0:
        redu = 1
    return int(reduce)
def do_a_pic(Tr, JIL, mas_names):
    print(mas_names)
    x = []
    y = []
    k = 0
    H = 0
    while sheet['A' + str(k + 1)].value != None:
        k += 1
    print(mas_names[Tr-1])
    for j in range(k):
        if mas_names[Tr-1] == sheet['A' + str(j + 1)].value:
            H = sheet['F' + str(j + 1)].value
            break

    data = data_z
    with Image.open(Trava[Tr - 1]) as img:
        img.load()
 
    kol_vo = randint(4, 19)
    tr_n = []
    for _ in range(kol_vo):
        tr_n.append({})
    for i in range(kol_vo):

        if Tr == 0:
            now_type_of_JILuk = randint(0, len(base_JILuk) - 1)
            number_bug = randint(0, len(base_JILuk[now_type_of_JILuk]) - 1)

            JILuk, new_JILuk = do_a_JILuk(now_type_of_JILuk, number_bug)

            rnd_x_min, rnd_x_max, rnd_y_min, rnd_y_max = some_parametr_of_PIC(randint(0, len(Trava)), img)
        elif JIL == -1:
            now_type_of_JILuk = randint(0, len(base_JILuk) - 1)
            number_bug = randint(0, len(base_JILuk[now_type_of_JILuk]) - 1)
            JILuk, new_JILuk = do_a_JILuk(now_type_of_JILuk, number_bug)
            rnd_x_min, rnd_x_max, rnd_y_min, rnd_y_max = some_parametr_of_PIC(Tr - 1, img)
        else:
            print("Fatal error!!!!")
            break

        reduce = do_reduce_0_0(img, JILuk, H, now_type_of_JILuk)
        if reduce == 0:
            continue
        JILuk_1 = JILuk.reduce(reduce)
        X = randint(rnd_x_min, rnd_x_max)
        Y = randint(rnd_y_min, rnd_y_max)
        tr = "{(" + str(X) + ";" + str(Y) + ");" \
             + "(" + str(X + JILuk_1.width) + ";" + str(Y) + ");" \
             + "(" + str(X + JILuk_1.width) + ";" + str(Y + JILuk_1.height) + ");" \
             + "(" + str(X) + ";" + str(Y + JILuk_1.height) + ")}"
        #print(str(1001 + now_type_of_JILuk))
        tr_n[i]["class_id"] = str(1001 + now_type_of_JILuk)
        tr_n[i]["polygon"] = tr
        x.append(X)
        y.append(Y)
        img.paste(
            JILuk.reduce(reduce),
            (X, Y),
            new_JILuk.reduce(reduce),
        )
        if now_type_of_JILuk == 0:
            statistic_gen[0] += 1
        elif now_type_of_JILuk == 1:
            statistic_gen[1] += 1
        elif now_type_of_JILuk == 2:
            statistic_gen[2] += 1
        elif now_type_of_JILuk == 3:
            statistic_gen[3] += 1
    data["modification_time"] = str(datetime.datetime.now())
    data["selected_targets"] = str(kol_vo)
    data["rect"] = "(0;0)(" + str(img.size[0]) + "x" + str(img.size[1]) + ")"
    data["targets"] = tr_n
    data["type_photo"] = "nadir"
    if JIL != -1:
        img.show()
    return x, y, img, data
def load_a_start_pic_grass(mydir_img):
    fon = []
    names = []
    dir = mydir_img
    fon_names = os.listdir(dir)
    print("Start load PIC")
    for i in range(len(fon_names)):
        fon.append(dir + "/" + fon_names[i])
        names.append(fon_names[i])

    print("Load PIC: OK")
    return fon, names
def load_a_start_pic_bug():
    IOO1 = []
    IOO2 = []
    IOO3 = []
    IOO4 = []
    print("Start load BUG")
    dir = '../database/bug base/1001'
    print(os.listdir(dir))
    IOO1_names = os.listdir(dir)
    for i in range(len(IOO1_names)):
        IOO1.append(dir + "/" + IOO1_names[i])
    dir = "../database/bug base/1002"
    print("1")
    IOO2_names = os.listdir(dir)
    for i in range(len(IOO2_names)):
        IOO2.append(dir + "/" + IOO2_names[i])
    dir = "../database/bug base/1003"
    print("2")
    IOO3_names = os.listdir(dir)
    for i in range(len(IOO3_names)):
        IOO3.append(dir + "/" + IOO3_names[i])
    dir = "../database/bug base/1004"
    print("3")
    IOO4_names = os.listdir(dir)
    for i in range(len(IOO4_names)):
        IOO4.append(dir + "/" + IOO4_names[i])
    print("4")
    print("Load BUG: OK")
    return IOO1, IOO2, IOO3, IOO4
def statistics_pic(names, mydir_save):
    way = mydir_save + "/pictures/"
    min_bug = 1000000
    max_bug = 0
    max_lenght = 0
    min_lenght = 100000
    count_bug = [0, 0, 0, 0]
    total_number = 0
    local_k = 0
    with open("info.json", "r") as read_file:
        data_of_info = json.load(read_file)
    for i in range(len(names)):
        with open(way + names[i][:-4] + ".json", "r") as read_file:
            data_now_pic = json.load(read_file)

        total_number += int(data_now_pic["selected_targets"])

        for j in range(len(data_now_pic["targets"])):
            for k in range(len(data_of_info["classificator"])):
                if data_now_pic["targets"][j]["class_id"] == data_of_info["classificator"][k]["id"]:
                    count_bug[k] += 1
                    local_k += 1
        min_bug = min(min_bug, local_k)
        max_bug = max(max_bug, local_k)
        local_k = 0




    f = open(mydir_save + "/statistics/statistics.txt", "a")
    f.write("\n==================STATISTICS OF SYNTHESIZED DATA==================\n")
    f.write("Number of pictures - " + str(len(names)) + "\n")
    f.write("How many beetles were inserted - " + str(total_number) + "\n")
    f.write("The number of beetles type 1001 (Bedbug evil turtle) in the pictures - " + str(count_bug[0]) + "\n")
    f.write("The number of beetles type 1002 (Bread striped flea) in the pictures - " + str(count_bug[1]) + "\n")
    f.write("The number of beetles type 1003 (Bread beetles) in the pictures - " + str(count_bug[2]) + "\n")
    f.write("The number of beetles type 1004 (meadow moth) in the pictures - " + str(count_bug[3]) + "\n")
    f.write("The maximum number of bugs in one picture - " + str(max_bug) + "\n")
    f.write("The minimum number of bugs in one picture - " + str(min_bug) + "\n")
    f.write("Average number of beetles in each picture - " + str(total_number / len(names)) + "\n")
    f.write("Average number of beetles type 1001 (Bedbug evil turtle) per picture - " + str(int(count_bug[0] / len(names))) + "\n")
    f.write("Average number of beetles type 1002 (Bread striped flea) per picture - " + str(int(count_bug[1] / len(names))) + "\n")
    f.write("Average number of beetles type 1003 (Bread beetles) per picture - " + str(int(count_bug[2] / len(names))) + "\n")
    f.write("Average number of beetles type 1004 (meadow moth) per picture - "  + str(int(count_bug[3] / len(names))) + "\n")
    f.close()
def start_data_synthesis(mydir_telemetry, mydir_img, mydir_save, genThred):
    print("start syntes")
    global data_z
    data_z = {
        "ipd": "0.00   30303030",
        "is_done": "true",
        "modification_by": "89213748002t@gmail.com",
        "modification_time": "",
        "rect": "(0;0)(4000x2250)",
        "selected_targets": "",
        "sensor_type": "VD",
    }
    global target_z
    target_z = {
        "class_id": "",
        "polygon": ""
    }

    IOO1 = []
    IOO2 = []
    IOO3 = []
    IOO4 = []
    global Trava
    Trava = []
    global statistic_gen

    statistic_gen = [0, 0, 0, 0]

    Trava, names = load_a_start_pic_grass(mydir_img)

    wb = opxl.load_workbook(mydir_telemetry)
    global sheet
    sheet = wb['Лист1']

    IOO1, IOO2, IOO3, IOO4 = load_a_start_pic_bug()

    global base_JILuk
    base_JILuk = [IOO1, IOO2, IOO3, IOO4]
    list(reversed(Trava))

    x = []
    y = []
    k = 0
    answ = 0

    count = 0

    for i in range(len(Trava)):
        count += 1
        x, y, final_img, finale_data = do_a_pic(i + 1, -1, names)
        k += 1
        final_img.save(mydir_save + "/pictures/" + names[i][:-4] + ".jpg")
        with open(mydir_save + "/pictures/" + names[i][:-4] + ".json", "w") as write_file:
            json.dump(finale_data, write_file)
        genThred.setPercent((i + 1) * 100 / len(Trava))
    statistics_pic(names, mydir_save)


