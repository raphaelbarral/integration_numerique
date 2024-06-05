def calculer_valeur_polynome(polynome,x):
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
    return(calculer_valeur_polynome(primitiver_polynome(polynome),interval[1])*interval[1]-calculer_valeur_polynome(primitiver_polynome(polynome),interval[0])*interval[0])

def integrer_methode_rectangle(polynome,nb_segment,interval):
    longeur_segment=((interval[1]-interval[0])/nb_segment)
    integration=0
    for i in range(nb_segment-1):
        aire_rectangle=(calculer_valeur_polynome(polynome,(i+1/2)*longeur_segment))*longeur_segment
        integration+=aire_rectangle
    return integration

def calculer_erreur_integartion(polynome,nb_segment,interval):
    erreur_integartion=(integrer_analytique(polynome,interval)-integrer_methode_rectangle(polynome,nb_segment,interval))/integrer_analytique(polynome,interval)
    return (f"l'erreur d'intégration est de {erreur_integartion*100} %")

print(integrer_analytique([1,1,1,1],[0,1]))
print(integrer_methode_rectangle([1,1,1,1],100,[0,1]))
print(calculer_erreur_integartion([1,1,1,1],100,[0,1]))