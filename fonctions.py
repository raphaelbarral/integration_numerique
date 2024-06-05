def calculer_valeur_polynome(polynome,x):
    valeur = 0
    for i in range(0,len(polynome)):
        valeur+=polynome[i]*x**(i)
    return valeur

def integrer_methode_rectangle(polynome, nb_segment,interval):
    longeur_segment=interval/nb_segment
    integration=0
    for i in range(nb_segment):
        aire_rectangle=calculer_valeur_polynome(polynome,)

