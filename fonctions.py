import numpy as np
import matplotlib.pyplot as plt
import timeit
import time

def calculer_polynome(x):
    return 0

def integrer_methode_trapeze_numpy(polynome, nb_segment, interval):
    x = np.linspace(interval[0], interval[1], nb_segment+1)
    y = polynome[0] + polynome[1]*x + polynome[2]*x**2 + polynome[3]*x**3
    T = ((x[1:]-x[:-1])*(y[1:]+y[:-1])/2).sum()
    return T

def integrer_methode_trapeze(polynome, nb_segment, interval):
    dx = (interval[1]-interval[0])/nb_segment
    x0 = interval[0]
    for i in range(nb_segment):
        T += dx*(calculer_polynome(x0+i*dx)+calculer_polynome(x+(i+1)*dx))/2
    return T
