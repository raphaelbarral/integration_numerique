# Ce fichier comporte les fonctions de calcul des différentes méthodes d'intégration ainsi que l'affichage des courbes de comparaison

import matplotlib.pyplot as plt
import numpy as np
import timeit
import scipy


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
    return(calculer_valeur_polynome(primitiver_polynome(polynome), interval[1]) - calculer_valeur_polynome(primitiver_polynome(polynome), interval[0]))


def integrer_methode_simpson_scipy(polynome, n, intervalle):
    x = np.linspace(intervalle[0], intervalle[1], n)  # On calcule le pas pour pouvoir le placer en argument de la fonction scipy
    y = calculer_valeur_polynome(polynome, x)
    resultat = scipy.integrate.simpson(y, x=x)
    return resultat


def integrer_methode_simpson_numpy(polynome, nb_segment, interval):
    x = np.linspace(interval[0], interval[1], nb_segment + 1)
    dx = (interval[1] - interval[0]) / nb_segment
    x_mid = np.linspace(interval[0]+dx/2, interval[1]-dx/2, nb_segment)
    y = polynome[0] + polynome[1] * x + polynome[2] * x ** 2 + polynome[3] * x ** 3
    y_mid = polynome[0] + polynome[1] * x_mid + polynome[2] * x_mid ** 2 + polynome[3] * x_mid ** 3
    T = ((x[1:] - x[:-1]) / 6 * (y[1:] + 4*y_mid + y[:-1])).sum()
    return T

def integrer_methode_simpson(polynome, n, intervalle):
    somme = 0
    pas = (intervalle[1] - intervalle[0]) / n  # Calcul de la longueur d'un segment
    x1 = intervalle[0]
    x2 = intervalle[0] + pas
    for i in range(n):    # On boucle sur le nombre de segment nécessaire pour l'intégration
        somme += (calculer_valeur_polynome(polynome, x1) + 4 * calculer_valeur_polynome(polynome, (x1 + x2) / 2) + calculer_valeur_polynome(polynome, x2)) / 6   # On somme l'aire sous la courbe de chacun des segements pour obtenir l'air totale du polynome
        x1 += pas  # On ajoute le pas pour passer au segement suivant
        x2 += pas
    return pas * somme   # Une fois la somme calculée on la multiplie par le pas


def integrer_methode_trapeze_scipy(polynome, n, intervalle):
    x = np.linspace(intervalle[0], intervalle[1], n)
    y = calculer_valeur_polynome(polynome, x)
    resultat = scipy.integrate.trapezoid(y, x=x)
    return resultat

def integrer_methode_trapeze_vectorise(polynome, nb_segment, interval):
    x = np.linspace(interval[0], interval[1], nb_segment + 1)
    y = polynome[0] + polynome[1] * x + polynome[2] * x ** 2 + polynome[3] * x ** 3
    T = ((x[1:] - x[:-1]) * (y[1:] + y[:-1]) / 2).sum()
    return T


def integrer_methode_trapeze(polynome, nb_segment, interval):
    dx = (interval[1] - interval[0]) / nb_segment
    x0 = interval[0]
    T = 0
    for i in range(nb_segment):
        T += dx * (calculer_valeur_polynome(polynome, x0 + i * dx) + calculer_valeur_polynome(polynome, x0 + (i + 1) * dx)) / 2
    return T


def integrer_methode_rectangle_vectorise(polynome, nb_segment, interval):
    dx = (interval[1] - interval[0]) / nb_segment
    x = np.linspace(interval[0]+dx/2, interval[1]-dx/2, nb_segment)
    y = polynome[0] + polynome[1] * x + polynome[2] * x ** 2 + polynome[3] * x ** 3
    T = (dx*y).sum()
    return T

def integrer_methode_rectangle(polynome,nb_segment,interval):
    longeur_segment=(interval[1]-interval[0])/nb_segment
    integration=0
    for i in range(nb_segment):
        aire_rectangle= (calculer_valeur_polynome(polynome, interval[0] + (i + 1 / 2) * longeur_segment)) * longeur_segment
        integration+=aire_rectangle
    return integration


def calculer_erreur_integartion(polynome, nb_segment, interval, fonction_integral):
    erreur_integartion = (integrer_analytique(polynome, interval) - fonction_integral(polynome, nb_segment,
                                                                                               interval)) / integrer_analytique(
        polynome, interval)
    return abs(erreur_integartion)

def plot_init():
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['font.size'] = 10
    plt.rcParams['figure.figsize'] = (12, 6)

def plot_ajouter_temps(integrer, polynome, interval, label, color):
    temps = []
    nb_seg = []
    for i in range(10):
        nb_seg.append(2 ** (i + 5))
        temps.append(timeit.timeit(lambda: integrer(polynome, nb_seg[i], interval), number=10) / 10)
    plt.plot(nb_seg, temps, label=label, color=color)

def plot_afficher_temps(titre):
    plt.yscale('log')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps (secondes)')  # Ajout d'un label pour l'axe des ordonnées
    plt.grid()
    plt.title(titre)
    plt.legend()
    plt.show()

def plot_ajouter_erreur(integrer, polynome, interval, label, color):
    erreur = []
    nb_seg = []
    for i in range(100):
        nb_seg.append(i + 1)
        erreur.append(calculer_erreur_integartion(polynome, nb_seg[i], interval, integrer))
    plt.plot(nb_seg, erreur, label=label, color=color)

def plot_afficher_erreur(titre):
    plt.yscale('log')
    plt.xlabel('Nombre de segments')
    plt.ylabel("Valeur de l'erreur en %")
    plt.title(titre)
    plt.grid()
    plt.legend()
    plt.show()