import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fonctions import *

#soit la fonction 1 + X + X2 + X3
polynome=[float(input("X0")),float(input("X1")),float(input("X2")),float(input("X3"))]
interval=[float(input("borne intégration inférieur")),float(input("borne intégration supérieur"))]
print(f"l'intégration analytrique entre 0 et 1 nous donne {integrer_analytique(polynome,interval)}")
nb_segment=int(input("nombre de segment pour l intégration avec méthode des rectangle"))
print(f"l'intégration analytrique entre 0 et 1 nous donne {integrer_methode_rectangle(polynome,nb_segment,interval)}")
print(f"l'erreur d'intégration est donc {calculer_erreur_integartion(polynome,nb_segment,interval)*100} % ")