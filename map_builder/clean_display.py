import csv
import time as t
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

def display_2D_map(X, Y, Z):
    start = t.time()

    #====== Create the figure ======
    x_unique = sorted(list(set(X)))
    y_unique = sorted(list(set(Y)))
    X, Y = np.meshgrid(x_unique, y_unique)

    Z = np.array(Z)
    Z = Z.reshape(len(y_unique), len(x_unique))


    plt.pcolormesh(X, Y, Z, cmap='coolwarm')
    plt.colorbar()  


    #====== Save the figure ======
    if not os.path.exists("img"):
        os.makedirs("img")
    
    num = 0
    while os.path.exists("./img/2D_"+str(num)+".png") :
        num += 1  
    plt.savefig("./img/2D_"+str(num)+".png")

    #====== display ======
    print("temps 2D :" + str(round(t.time()-start, 3)) +"\n")
    plt.show()





def extract_csv(file_name):
    with open("./csv"+file_name as f):
        csv_reader = csv.

        data = [[],[],[]]
        for row in csv_reader:
            data[0].append([float(row[0])])
            data[1].append([float(row[1])])
            data[2].append([float(row[2])])
    return np.array(data)


def write_csv(data, filename):
    if not os.path.exists("csv"):
        os.makedirs("csv")

    with open("./csv/" + filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['X', 'Y', 'Z'])  # Écriture de l'en-tête

        for k in range(len(data[0])):
            writer.writerow([data[0,k], data[1,k], data[2,k]])


def generer_points(N):
    points = []
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            z = (max(abs(x),abs(y)))**4  # Exemple de fonction de z
            points.append([x, y, z])
    return points


def concatenate_maps():
    dim = int(input("Insérer le nombre de dimension de la carte (2 pour 2D, 3 pour 3D) : "))
    if dim != 2 and dim != 3:
        print("Erreur : dimension non reconnue")
        return
    
    lst = []
    add = input("Insérer le nom du CSV")
    while (add != "fini"):
        lst.append(add)
        add = (input("Insérer le nom du CSV (fini si aucun rajout): "))
        
    X = []
    Y = []
    Z = []
    
    for k in range(len(lst)):
        with open(lst[k], mode='r', newline='\n') as file:
            reader = csv.reader(file)
            for row in reader:
                X.append(row[0])
                Y.append(row[1])
                Z.append(row[2])
    if dim == 2:
        display_2D_map(X, Y, Z)
    elif dim == 3:
        display_3D_map(X, Y, Z)




# ============= TESTS =============


# Exemple d'utilisation avec un puits de la forme x^4 puis sinus bizarre
N=10#Complexité en O(N^2)

#X = [x for x in range(-N,N)]
#Y = [y for y in range(-N,N)]
#Z1 = [[(max(abs(x),abs(y)))**4 for x in X] for y in Y]
#Z =  [[(max(m.sin(x/10),m.sin(y/10)))**4 for x in X] for y in Y]

#display_2D_map(X, Y, Z)
#display_3D_map(X,Y,Z)

points = generer_points(N)

start = t.time()
#ecrire_points_csv(points, "./img/data.csv")
end = t.time()
print("temps :")
print(end-start)
concatenate_maps()

#Pour écrire un fichier csv:
#Pour N=2000 : 16 000 000pts : 6.2s 
#378Mo pour 16 000 000 points donc x360 pour obtenir les données manipulables en 30min:
#136 080Mo soit 136Go pour 5 740 000 000 points




#Pour (2N)^2 pts : 2D, 3D

#sans save_img:
#Pour 1000 pts : 2.02s, 1.15s | 
#Pour 3000 pts : 4.43s, 6.04s

#avec save_img :
#Pour N=4000 : 64 000 000pts: 19.36, 4.45 | limite des capacités de Matplotlib
#Pour N=3000 : 36 000 000pts: 11.04, 3.7
#Pour N=2000 : 16 000 000pts : 5.63, 1.29
#Pour N=1000 : 4 000 000pts : 4.43s, 1.15s
#Pour N=500  : 1 000 000 pts : 1.66s, 0.718s
#Pour N=100  : 40 000pts     : 0.735, 0.475

#On a intérêt à toujours traiter le maximum de points possibles d'un coup, donc : les carrés le plus grand possible
#Ici, on ferait en 30min : 90 img de 64 000 000pts (on est larges), soit : 5 740 000 000 points!
#on peut changer la taille des carrés à notre convenance aussi
#à vue de pif, en 2D des img de N=50 soit : 10 000 pts sont tout à fait correctes

#Il me faut la fréquence de collecte de données des capteurs pour que je sache s'il faut élaguer des points
#Ce serait bien qu'il y en ait moins de 10 000 000 000. 






#Features
# pouvoir afficher une carte pas nécessairement rectangulaire
# On considère que 30min de calcul c'est fine.
# arriver à traiter les bords? Oui : mettre une hauteur nulle Z=0 


#2D
# Idée : Faire un quadrillage du lac de l'X et traiter rectangle par rectangle puis reconstituer l'image par collage (en 2D)

#   Pour cela, il faut d'abord trier les points dans l'ordre des carrés.
#   On sait plus ou moins qu'on fait des parcours dans la même direction, de gauche à droite puis de droite à gauche
#   l'algorithme peut s'en aider : repérer les demi-tours pour trier les points par lignes (= par ordonnée)
#   puis prendre les bouts de lignes compris entre l'abscisse a et l'abscisse b  
#   Complexité O(n), n : nb de points

#   Les images ont le même format, il faut les découper automatiquement et les recoller. Elles doivent donc être bien nommées
#   Complexité en O(nb_img), négligeable devant la production de ces img


#   La complexité limitante est la génération des img.
#   5s pour 3000pts => 

#3D
#Choisir très basse résolution (4000pts...?)
#On afficherait tout d'un coup