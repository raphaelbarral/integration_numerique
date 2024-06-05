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
    s = 0
    h = (intervalle[1]-intervalle[0])/n
    x1 = intervalle[0]
    x2 = intervalle[0] + h

    for i in range(n):
        s += (f(polynome,x1)+4*f(polynome,(x1+x2)/2)+f(polynome,x2))/6
        x1 += h
        x2 += h
    return h*s

polynome = [1,1,1,1]
intervalle = [0,1]
n = 10000
dx = calculer_nombre_echantillon(intervalle,n)

print(calculer_simpson(polynome,intervalle,n))
print(scipy.integrate.simpson(polynome, x=None, dx, axis=-1, even=<object object>))