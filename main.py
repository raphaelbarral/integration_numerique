from fonctions import *

plot_init()

polynome = [float(input("X0")), float(input("X1")), float(input("X2")), float(input("X3"))]
interval = [float(input("borne intégration inférieur")), float(input("borne intégration supérieur"))]
nb_segment = int(input("nombre de segment pour l intégration avec méthode des rectangle"))

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
print(f"l'intégration avec la méthode des rectangles numpy nous donne {integrer_methode_rectangle_numpy(polynome,nb_segment,interval)}")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_rectangle_numpy(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des rectangles numpy")

plot_ajouter_temps(integrer_methode_rectangle, polynome, interval, 'Python de base', 'blue')
plot_ajouter_temps(integrer_methode_rectangle_numpy, polynome, interval, 'numPy', 'red')
plot_afficher_temps("Temps d'execution de la méthode des rectangle en fonction du nombre de segments")

# Question 2.2.1
print(f"l'intégration avec la méthode des trapezes nous donne {integrer_methode_trapeze(polynome,nb_segment,interval)}")
print(f"l'intégration avec la méthode des trapezes numpy nous donne {integrer_methode_trapeze_numpy(polynome,nb_segment,interval)}")

# Question 2.2.2
print(f"l'erreur avec la méthode des trapezes est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_trapeze)} % ")
print(f"l'erreur avec la méthode des trapezes numpy est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_trapeze_numpy)} % ")

print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_trapeze(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des trapezes")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_trapeze_numpy(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode des trapezes numpy")

# Question 2.2.3
plot_ajouter_erreur(integrer_methode_trapeze, polynome, interval, 'Python de base', 'blue')
plot_afficher_erreur('Graphique montrant la convergence de la méthode des trapeze en fonction du nombre de segments')

# Question 2.2.4
plot_ajouter_temps(integrer_methode_trapeze, polynome, interval, 'Python de base', 'blue')
plot_ajouter_temps(integrer_methode_trapeze_numpy, polynome, interval, 'numPy', 'red')
plot_ajouter_temps(integrer_methode_trapeze_scipy, polynome, interval, 'méthode pré-programmé', 'green')
plot_afficher_temps("Temps d'execution de la méthode des trapeze en fonction du nombre de segments")

# Question 2.3.1
print(f"l'intégration avec la méthode de Simpson nous donne {integrer_methode_simpson(polynome,nb_segment,interval)}")
print(f"l'intégration avec la méthode de Simpson numpy nous donne {integrer_methode_simpson_numpy(polynome,nb_segment,interval)}")

# Question 2.3.2
print(f"l'erreur avec la méthode de Simpson est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_simpson)} % ")
print(f"l'erreur avec la méthode des Simpson numpy est {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_simpson_numpy)} % ")

print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_simpson(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode de Simpson")
print(f"Le temps d'exécution est {timeit.timeit(lambda :integrer_methode_simpson_numpy(polynome, nb_segment, interval), number=10)/10} secondes pour la méthode de Simpson")

# Question 2.3.3
plot_ajouter_erreur(integrer_methode_simpson, polynome, interval, 'Python de base', 'blue')
plot_afficher_erreur('Graphique montrant la convergence de la méthode de Simpson en fonction du nombre de segments')

# Question 2.3.4
plot_ajouter_temps(integrer_methode_simpson, polynome, interval, 'Python de base', 'blue')
plot_ajouter_temps(integrer_methode_simpson_numpy, polynome, interval, 'numPy', 'red')
plot_ajouter_temps(integrer_methode_simpson_scipy, polynome, interval, 'methode pré-programmé', 'green')
plot_afficher_temps("Temps d'execution de la méthode de Simpson en fonction du nombre de segments")
