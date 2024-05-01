import os
import csv
import time as t
import numpy as np
import matplotlib.pyplot as plt

import math as m
from scipy.interpolate import griddata
# from mpl_toolkits.mplot3d import Axes3D

# =================================================== 3D DISPLAY ===================================================

def display3D(data, res = 500):
    start = t.time()



    #====== Create the figure ======
    x_interp = np.linspace(data[0].min(), data[0].max(), res) 
    y_interp = np.linspace(data[1].min(), data[1].max(), res)
    X,Y = np.meshgrid(x_interp, y_interp)
    Z_interp = griddata((data[0], data[1]), data[2], (X,Y), method='linear')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z_interp, cmap='coolwarm')


    #====== display ======
    print("temps 3D :" + str(round(t.time()-start, 3)) +"\n")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Profondeur')
    fig1 = plt.gcf()
    plt.show()

    #====== Save the figure ======
    ask = input("Save the image? (y/n) : ")
    if ask == "y":
        if not os.path.exists("img"):
            os.makedirs("img")
        
        num = 0
        while os.path.exists("./img/3D_"+str(num)+".png") :
            num += 1  
        fig1.savefig("./img/3D_"+str(num)+".png")

# =================================================== 2D DISPLAY ===================================================


def display2D(data, res = 500):
    start = t.time()

    #====== Create the figure ======
    x_interp = np.linspace(data[0].min(), data[0].max(), res) 
    y_interp = np.linspace(data[1].min(), data[1].max(), res)
    X,Y = np.meshgrid(x_interp, y_interp)
    Z_interp = griddata((data[0], data[1]), data[2], (X,Y), method='linear')

    plt.pcolormesh(X, Y, Z_interp, cmap = 'coolwarm')
    plt.colorbar()  

    #====== display ======
    print("temps 2D :" + str(round(t.time()-start, 3)) +"\n")
    fig1 = plt.gcf()
    plt.show()

    #====== Save the figure ======
    ask = input("Save the image? (y/n) : ")
    if ask == "y":
        if not os.path.exists("img"):
            os.makedirs("img")
        
        num = 0
        while os.path.exists("./img/2D_"+str(num)+".png") :
            num += 1  
        fig1.savefig("./img/2D_"+str(num)+".png")



# =================================================== CSV STUFF ===================================================


def extract_csv(file_name):
    with open("./csv/"+file_name+".csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)

        data = [[],[],[]]
        for row in csv_reader:
            data[0].append(float(row[0]))
            data[1].append(float(row[1]))
            data[2].append(float(row[2]))
    return np.array(data)




def write_csv(data, filename):
    if not os.path.exists("csv"):
        os.makedirs("csv")

    nb = 0
    while os.path.exists("./csv/" + filename + "_" + str(nb) + ".csv"):
        nb += 1

    name = "./csv/" + filename + "_" + str(nb) + ".csv"
    with open(name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for k in range(len(data[0])):
            writer.writerow([data[0,k], data[1,k], data[2,k]])


# =================================================== Generation of data for tests ===================================================

def func1(x,y):
    return (max(abs(x),abs(y)))**4




def generate_data(N, func):
    data = [[],[],[]]
    n = round(m.sqrt(N))
    for x in range(n):
        for y in range(n):
            z = func(x,y)
            data[0].append(x)
            data[1].append(y)
            data[2].append(func(x,y))
    return np.array(data)



# ============= MAIN =============


#Choose Data to treat
ask = input("Do you want to load a csv file? (y/n) : ")
if ask == "y":
    ask = input("name of the csv file : ")
    while not os.path.exists("./csv/" + ask + ".csv"):
        print("The file does not exist. (press Ctrl+C if you want to exit)")
        ask = input("name of the csv file : ")
    data = extract_csv(ask)


else:
    N = int(input("How many points of data to generate? : "))
    data = generate_data(N, func1)
    ask = input("Do you want to save the generated data? (y/n) : ")
    if ask == "y":
        write_csv(data, "test")



#Choose display mode and resolution
ask = input("Choose the display mode(2D/3D) : ")
ask2 = int(input("Resolution chosen (int) : "))
if ask == "3D":
    print("3D mode selected")
    display3D(data, max(ask2,1000))

else:
    print("2D mode selected")
    display2D(data, max(ask2,1000))



