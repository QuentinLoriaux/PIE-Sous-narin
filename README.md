# PIE-Sous-narin

## Arduino

Programmes simples directement issus des exemples des librairies associées au matériel commandé par Arduino que nous avons utilisé. Ils servent de référence pour les programmes qui seront réellement utilisés pour les tests.

## Map Builder

Les programmes permettent d'afficher une carte à gradient de couleur, en 2D ou en 3D, donnant la profondeur du fond d'un lac représenté par une liste de points tridimensionnelle stockée dans un csv. Des fonctions sont disponibles pour générer un jeu de données en attendant d'avoir des mesures réelles.

- display_map.py est le 1er jet de code qui a été utilisé pour réaliser des tests sur les limitations en mémoire et en temps du programme et du jeu de données.
- clean_display.py est une version épurée, commentée et user-friendly pour générer des données, générer des cartes et les sauvegarder dans les dossiers correspondants.