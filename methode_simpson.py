import scipy
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

nb_de_segment = []
temps = []
nb_de_segment2 = []
temps2 = []
def f(polynome,x):
    valeur = 0
    for i in range(0,len(polynome)):
        valeur += polynome[i]*x**(i)
    return valeur

def calculer_nombre_echantillon(intervalle,n):
    x = np.linspace(intervalle[0], intervalle[1], n)
    return x

def calculer_simpson(polynome,intervalle,n):
    somme = 0
    pas = (intervalle[1]-intervalle[0])/n
    x1 = intervalle[0]
    x2 = intervalle[0] + pas
    for i in range(n):
        somme += (f(polynome,x1)+4*f(polynome,(x1+x2)/2)+f(polynome,x2))/6
        x1 += pas
        x2 += pas
    return pas*somme

def calculer_simpson_numpy(polynome, intervalle, n):
    x = calculer_nombre_echantillon(intervalle, n)
    y = f(polynome, x)
    resultat = scipy.integrate.simpson(y, x=x)
    return resultat

def calculer_erreur(resulat1, resultat2):
    erreur = abs(resulat1 - resultat2)
    return erreur

def calculer_temps_simpson_numpy(n, polynome, intervalle):
    global nb_de_segment2, temps2
    for i in range(1, n):
        tic2 = perf_counter()
        calculer_simpson_numpy(polynome, intervalle, i)
        toc2 = perf_counter()
        nb_de_segment2.append(i)
        temps2.append(toc2 - tic2)
    temps2.pop(0)
    nb_de_segment2.pop(0)
    return
def calculer_temps_simpson(n, polynome, intervalle):
    global nb_de_segment, temps
    for i in range(1, n):
        tic = perf_counter()
        calculer_simpson(polynome, intervalle, i)
        toc = perf_counter()
        nb_de_segment.append(i)
        temps.append(toc - tic)
    return
# Fonction pour afficher les résultats
def afficher():
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.plot(nb_de_segment, temps, label='Python de base', color='blue')
    plt.plot(nb_de_segment2, temps2, label='NumPy', color='red')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps (secondes)')  # Ajout d'un label pour l'axe des ordonnées
    plt.title("Temps d'execution de la méthode de simpson en fonction du nombre de segments")
    plt.legend()
    plt.show()
    return

polynome = [1,1,1,1]
intervalle = [0,1]
n = 1000

calculer_temps_simpson_numpy(n,polynome,intervalle)
calculer_temps_simpson(n,polynome,intervalle)
afficher()


#print(f"\nRésultat de l'intégration par la méthode de simpson en Python de base est de: {r2}")
#print(f"Résultat de l'intégration par à l'aide de NumPy: {r1}")
#print(f"Erreur = {calculer_erreur(r1, r2)}, soit : {(calculer_erreur(r1, r2)/abs(r1))*100} %")