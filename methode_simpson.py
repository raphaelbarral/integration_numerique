import scipy
import numpy as np

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

polynome = [1,1,1,1]
intervalle = [0,1]
n = 10000

r1 = calculer_simpson(polynome,intervalle,n)
r2 = calculer_simpson_numpy(polynome,intervalle,n)

print(f"\nRésultat de l'intégration par la méthode de simpson en Python de base est de: {r2}")
print(f"Résultat de l'intégration par à l'aide de NumPy: {r1}")
print(f"Erreur = {calculer_erreur(r1, r2)}, soit : {(calculer_erreur(r1, r2)/abs(r1))*100} %")