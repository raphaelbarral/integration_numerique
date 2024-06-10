import timeit

import numpy as np
import matplotlib.pyplot as plt
from fonctions import *

#Partie méthode des rectangles
#polynome=[float(input("X0")),float(input("X1")),float(input("X2")),float(input("X3"))]
#interval=[float(input("borne intégration inférieur")),float(input("borne intégration supérieur"))]
#nb_segment=int(input("nombre de segment pour l intégration avec méthode des rectangle"))

polynome = [1, 1, 1, 1]
interval=[0, 10]
nb_segment = 50

#Question 2.1.1.1
print(f"l'intégration analytique nous donne {integrer_analytique(polynome,interval)}")
#Question 2.1.1.2
print(f"l'intégration avec la méthode des rectangles nous donne {integrer_methode_rectangle(polynome,nb_segment,interval)}")
#Question 2.1.1.3
print(f"l'erreur d'intégration est donc {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_rectangle)} % ")
#Question 2.1.1.5
results_rect = []
nb_seg_rect = []
for i in range(10):
    nb_seg_rect.append(2 ** (i + 1))
    results_rect.append(calculer_erreur_integartion(polynome, nb_seg_rect[i], interval, integrer_methode_rectangle))

plt.plot(nb_seg_rect, results_rect)
plt.yscale('log')
plt.xscale('log')
plt.show()
#Question 2.1.1.6
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_rectangle(polynome, nb_segment, interval), number=1000)/1000} secondes pour la méthode des rectangles")

#Queestion 2.1.2.1
print(f"l'intégration avec la méthode des rectangles numpy nous donne {integrer_methode_rectangle_numpy(polynome,nb_segment,interval)}")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_rectangle_numpy(polynome, nb_segment, interval), number=1000)/1000} secondes pour la méthode des rectangles numpy")

temps_rect_numpy = []
temps_rect = []
nb_seg = []
for i in range(10):
    nb_seg.append(2 ** (i + 1))
    temps_rect.append(timeit.timeit(lambda :integrer_methode_rectangle(polynome, nb_seg[i], interval), number=1000)/1000)
    temps_rect_numpy.append(timeit.timeit(lambda :integrer_methode_rectangle_numpy(polynome, nb_seg[i], interval), number=1000)/1000)

results = np.array([temps_rect , temps_rect_numpy]).transpose()
nb_seg = np.array([nb_seg, nb_seg]).transpose()

plt.plot(nb_seg, results)
plt.yscale('log')
plt.xscale('log')
plt.show()

#Question 2.2.1
print(f"l'intégration avec la méthode des trapezes nous donne {integrer_methode_trapeze(polynome,nb_segment,interval)}")
print(f"l'intégration avec la méthode des trapezes numpy nous donne {integrer_methode_trapeze_numpy(polynome,nb_segment,interval)}")

#Question 2.2.2
print(f"l'erreur avec la méthode des trapezes est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_trapeze)} % ")
print(f"l'erreur avec la méthode des trapezes numpy est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_trapeze_numpy)} % ")

print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_trapeze(polynome, nb_segment, interval), number=1000)/1000} secondes pour la méthode des trapezes")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_trapeze_numpy(polynome, nb_segment, interval), number=1000)/1000} secondes pour la méthode des trapezes numpy")

#Question 2.2.3
results_trap = []
nb_seg_trap = []
for i in range(10):
    nb_seg_trap.append(2 ** (i + 1))
    results_trap.append(calculer_erreur_integartion(polynome, nb_seg_trap[i], interval, integrer_methode_trapeze))

results = np.array([results_rect , results_trap]).transpose()
nb_seg = np.array([nb_seg_rect, nb_seg_trap]).transpose()

plt.plot(nb_seg, results)
plt.yscale('log')
plt.xscale('log')
plt.show()

#Question 2.2.4
temps_trap_numpy = []
temps_trap = []
nb_seg = []
for i in range(10):
    nb_seg.append(2 ** (i + 1))
    temps_trap.append(timeit.timeit(lambda :integrer_methode_trapeze(polynome, nb_seg[i], interval), number=1000)/1000)
    temps_trap_numpy.append(timeit.timeit(lambda :integrer_methode_trapeze_numpy(polynome, nb_seg[i], interval), number=1000)/1000)

results = np.array([temps_trap , temps_trap_numpy]).transpose()
nb_seg = np.array([nb_seg, nb_seg]).transpose()

plt.plot(nb_seg, results)
plt.yscale('log')
plt.xscale('log')
plt.show()

