# L'objectif de ce programme est de comparer 3 méthodes d'intégration numérique sur un polynome de 3 ème ordre entré
# par l utilisateur du programme

from fonctions import *

plot_init()

print(f"Précisez la valeur des coefficients du polynôme à intégrer")
polynome = [float(input("X0 : ")), float(input("X1 : ")), float(input("X2 : ")), float(input("X3 : "))]
interval = [float(input("Valeur de la borne intégration inférieur : ")), float(input("Valeur de la borne intégration supérieur : "))]
nb_segment = int(input("Précisez le nombre de segment pour l'intégration : "))

# Question 2.1.1.1
print(f"l'intégration analytique nous donne {integrer_analytique(polynome,interval)}")
# Question 2.1.1.2
print(f"l'intégration avec la méthode des rectangles nous donne {integrer_methode_rectangle(polynome,nb_segment,interval)}")
# Question 2.1.1.3
print(f"l'erreur d'intégration est donc {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_rectangle)} % ")
# Question 2.1.1.5

plot_ajouter_erreur(integrer_methode_rectangle, polynome, interval, 'Python de base', 'blue')
plot_afficher_erreur('Graphique montrant la convergence de la méthode des rectangle en fonction du nombre de segments')

# Question 2.1.1.6
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_rectangle(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des rectangles")

# Question 2.1.2.1
print(f"l'intégration avec la méthode des rectangles numpy nous donne {integrer_methode_rectangle_vectorise(polynome,nb_segment,interval)}")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_rectangle_vectorise(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des rectangles numpy")

plot_ajouter_temps(integrer_methode_rectangle, polynome, interval, 'Python de base', 'blue')
plot_ajouter_temps(integrer_methode_rectangle_vectorise, polynome, interval, 'Vectorisée', 'red')
plot_afficher_temps("Temps d'execution de la méthode des rectangles en fonction du nombre de segments")

# Question 2.2.1
print(f"l'intégration avec la méthode des trapezes nous donne {integrer_methode_trapeze(polynome,nb_segment,interval)}")
print(f"l'intégration avec la méthode des trapezes numpy nous donne {integrer_methode_trapeze_vectorise(polynome,nb_segment,interval)}")

# Question 2.2.2
print(f"l'erreur avec la méthode des trapezes est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_trapeze)} % ")
print(f"l'erreur avec la méthode des trapezes numpy est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_trapeze_vectorise)} % ")

print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_trapeze(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des trapezes")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_trapeze_vectorise(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des trapezes numpy")

# Question 2.2.3
plot_ajouter_erreur(integrer_methode_trapeze, polynome, interval, 'Python de base', 'blue')
plot_afficher_erreur('Graphique montrant la convergence de la méthode des trapeze en fonction du nombre de segments')

# Question 2.2.4
plot_ajouter_temps(integrer_methode_trapeze, polynome, interval, 'Python de base', 'blue')
plot_ajouter_temps(integrer_methode_trapeze_vectorise, polynome, interval, 'Vectorisée', 'red')
plot_ajouter_temps(integrer_methode_trapeze_scipy, polynome, interval, 'méthode pré-programmé', 'green')
plot_afficher_temps("Temps d'execution de la méthode des trapeze en fonction du nombre de segments")

# Question 2.3.1
print(f"l'intégration avec la méthode de Simpson nous donne {integrer_methode_simpson(polynome,nb_segment,interval)}")
print(f"l'intégration avec la méthode de Simpson vectorisé nous donne {integrer_methode_simpson_numpy(polynome,nb_segment,interval)}")

# Question 2.3.2
print(f"l'erreur avec la méthode de Simpson est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_simpson)} % ")
print(f"l'erreur avec la méthode des Simpson vectorisé est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_simpson_numpy)} % ")

print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_simpson(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode de Simpson")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_simpson_numpy(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode de Simpson")

# Question 2.3.3
plot_ajouter_erreur(integrer_methode_simpson, polynome, interval, 'Python de base', 'blue')
plot_afficher_erreur('Graphique montrant la convergence de la méthode de Simpson en fonction du nombre de segments')

# Question 2.3.4
plot_ajouter_temps(integrer_methode_simpson, polynome, interval, 'Python de base', 'blue')
plot_ajouter_temps(integrer_methode_simpson_numpy, polynome, interval, 'Vectorisée', 'red')
plot_ajouter_temps(integrer_methode_simpson_scipy, polynome, interval, 'Méthode pré-programmé', 'green')
plot_afficher_temps("Temps d'exécution de la méthode de Simpson en fonction du nombre de segments")

# Comparaison de la complexité des méthodes entre elles
plot_ajouter_temps(integrer_methode_simpson, polynome, interval, 'Simpson en python de base', 'blue')
plot_ajouter_temps(integrer_methode_trapeze, polynome, interval, 'Trapèze en python de base', 'red')
plot_ajouter_temps(integrer_methode_rectangle, polynome, interval, 'Rectangle en python de base', 'green')
plot_ajouter_temps(integrer_methode_simpson_scipy, polynome, interval, 'Simpson pré-programmé', 'orange')
plot_ajouter_temps(integrer_methode_trapeze_scipy, polynome, interval, 'Trapèze pré-programmé','cyan')
plot_ajouter_temps(integrer_methode_rectangle_vectorise, polynome, interval, 'Rectangle vectorisée','yellow')
plot_afficher_temps("Temps d'exécution des 3 méthodes étudiées en fonction du nombre de segments")

# Comparaison de la précision des méthodes entre elles
plot_ajouter_erreur(integrer_methode_simpson, polynome, interval, 'Simpson en python de base', 'blue')
plot_ajouter_erreur(integrer_methode_trapeze, polynome, interval, 'Trapèze en python de base', 'red')
plot_ajouter_erreur(integrer_methode_rectangle, polynome, interval, 'Rectangle en python de base', 'green')
plot_ajouter_erreur(integrer_methode_trapeze_scipy, polynome, interval, 'Trapèze pré-programmé','cyan')
plot_ajouter_erreur(integrer_methode_rectangle_vectorise, polynome, interval, 'Rectangle vectorisée','orange')
plot_afficher_erreur("Graphique montrant la convergence des 3 méthodes étudiées en fonction du nombre de segments")

