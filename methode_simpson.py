import scipy
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

nb_de_segment = []
temps = []
nb_de_segment2 = []
temps2 = []

def f(polynome, x):
    valeur = 0
    for i in range(0, len(polynome)):
        valeur += polynome[i] * x ** (i)
    return valeur

def calculer_nombre_echantillon(intervalle, n):
    x = np.linspace(intervalle[0], intervalle[1], n)
    return x

def calculer_simpson(polynome, n, intervalle):
    somme = 0
    pas = (intervalle[1] - intervalle[0]) / n
    x1 = intervalle[0]
    x2 = intervalle[0] + pas
    for i in range(n):
        somme += (f(polynome, x1) + 4 * f(polynome, (x1 + x2) / 2) + f(polynome, x2)) / 6
        x1 += pas
        x2 += pas
    return pas * somme

def calculer_simpson_numpy(polynome, n, intervalle):
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
        calculer_simpson_numpy(polynome, i, intervalle)
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
        calculer_simpson(polynome, i, intervalle)
        toc = perf_counter()
        nb_de_segment.append(i)
        temps.append(toc - tic)
    return

def calculer_valeur_polynome(polynome, x):
    valeur = 0
    for i in range(0,len(polynome)):
        valeur+=polynome[i]*x**(i)
    return valeur

def primitiver_polynome(polynome):
    polynome_integre=[0]
    for i in range(len(polynome)):
        polynome_integre.append(polynome[i]/(i+1))
    return polynome_integre

def integrer_analytique(polynome,interval):
    return(calculer_valeur_polynome(primitiver_polynome(polynome),interval[1])-calculer_valeur_polynome(primitiver_polynome(polynome),interval[0]))

def afficher_temps_execution():
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

def afficher_convergence_simpson(polynome, intervalle, n):

    erreurs = []
    nb_de_segments3 = []
    for i in range(4, n, 2):
        val_exact = integrer_analytique(polynome,intervalle)
        err = calculer_erreur(val_exact, calculer_simpson_numpy(polynome, i, intervalle))
        erreurs.append(err)
        nb_de_segments3.append(i)

    erreurs.pop(0)
    nb_de_segments3.pop(0)

    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.plot(nb_de_segments3,erreurs, label="Erreur d'intégration", color='blue')
    plt.xlabel('Nombre de segments')
    plt.ylabel("Valeur de l'erreur")
    plt.title("Graphique montrant la convergence de la méthode de Simpson en fonction du nombre de segments")
    plt.legend()
    plt.show()
    return
