import numpy as np
import matplotlib.pyplot as plt
import timeit
import time

def integrer_methode_trapeze(polynome, nb_segment, interval)
    x = np.linspace(interval[0], interval[1], nb_segment+1)
    y = x.map(calculer_valeur_polynome())
    return 0