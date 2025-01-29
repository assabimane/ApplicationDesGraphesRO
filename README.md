1. Description du Projet

Ce projet est une application Python avec interface graphique permettant de visualiser des graphes et d'appliquer plusieurs algorithmes classiques sur ceux-ci. L'application utilise Tkinter pour l'interface utilisateur et NetworkX pour la gestion des graphes. Elle permet de :

Générer un graphe connexe aléatoire.

Visualiser plusieurs algorithmes sur graphes (à savoir Dijkstra, Kruskal, Bellman-Ford, etc.).

Offrir une interface utilisateur intuitive avec des boutons pour chaque algorithme.

Fournir une page d'accueil avec un titre et des options d'entrée et de sortie.
2. Explication du Code

a) Structure du Code

Le projet est composé d'une classe GraphVisualizerApp qui gère l'interface et la logique des graphes.

Interface utilisateur :

Une fenêtre principale avec un champ pour entrer le nombre de sommets et des boutons pour générer le graphe.

Une sélection d'algorithmes disponibles pour l'affichage.

Génération d'un graphe connexe aléatoire :

Un arbre couvrant est d'abord créé pour assurer la connexivité.

Des arêtes supplémentaires sont ajoutées avec une probabilité de 30% pour complexifier le graphe.

Affichage des graphes :

Utilisation de NetworkX et Matplotlib pour dessiner les graphes.

Les poids des arêtes sont affichés pour une meilleure compréhension.

Page d'accueil :

Un premier écran avec un titre principal et un sous-titre.

Deux boutons : Entrer dans le programme et Quitter.

3. Conversion en Fichier Exécutable

a) Prérequis :

Vous utilisez Anaconda et Spyder pour exécuter votre code Python. Pour transformer votre script en fichier .exe, vous devez utiliser pyinstaller.

b) Installation de PyInstaller :

Ouvrir l'Invite de Commande Anaconda :

Cherchez "Anaconda Prompt" dans le menu Démarrer et ouvrez-le.

Installer PyInstaller :

conda install pyinstaller

c) Compilation du Script :

Naviguer jusqu'au dossier contenant votre script (ProjectRo.py) :

cd C:\Users\PC\Desktop\pro

Générer l'exécutable :

pyinstaller --onefile ProjectRo.py

Le fichier exécutable sera généré dans le dossier dist/.

