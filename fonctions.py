import numpy as np
import matplotlib.pyplot as plt
import timeit
import time


def integrer_methode_trapeze_numpy(polynome, nb_segment, interval):
    x = np.linspace(interval[0], interval[1], nb_segment + 1)
    y = polynome[0] + polynome[1] * x + polynome[2] * x ** 2 + polynome[3] * x ** 3
    T = ((x[1:] - x[:-1]) * (y[1:] + y[:-1]) / 2).sum()
    return T


def integrer_methode_trapeze(polynome, nb_segment, interval):
    dx = (interval[1] - interval[0]) / nb_segment
    x0 = interval[0]
    T = 0
    for i in range(nb_segment):
        T += dx * (calculer_valeur_polynome(polynome, x0 + i * dx) + calculer_valeur_polynome(polynome,
                                                                                              x0 + (i + 1) * dx)) / 2
    return T


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

def integrer_methode_rectangle(polynome,nb_segment,interval):
    longeur_segment=(interval[1]-interval[0])/nb_segment
    integration=0
    for i in range(nb_segment):
        aire_rectangle=(calculer_valeur_polynome(polynome,interval[0]+(i+1/2)*longeur_segment))*longeur_segment
        integration+=aire_rectangle
    return integration


def integrer_methode_rectangle_numpy(polynome, nb_segment, interval):
    dx = (interval[1] - interval[0]) / nb_segment
    x = np.linspace(interval[0]+dx/2, interval[1]-dx/2, nb_segment)
    y = polynome[0] + polynome[1] * x + polynome[2] * x ** 2 + polynome[3] * x ** 3
    T = (dx*y).sum()
    return T


def calculer_erreur_integartion(polynome, nb_segment, interval, fonction_integral):
    erreur_integartion = (integrer_analytique(polynome, interval) - fonction_integral(polynome, nb_segment,
                                                                                               interval)) / integrer_analytique(
        polynome, interval)
    return (f"l'erreur d'intégration est de {erreur_integartion * 100} %")


print(integrer_methode_trapeze([1, 1, 1, 1], 100000,[0, 1]))
print(integrer_methode_trapeze_numpy([1, 1, 1, 1], 100000, [0, 1]))
print(calculer_erreur_integartion([1, 1, 1, 1], 100000, [0, 1], integrer_methode_trapeze))