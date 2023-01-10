# Pretraitement

Ce code a pour but de pretraiter un ensemble d'images en vue de leur utilisation pour l'entrainement d'un modele de classification d'images.

## Prerequis

- Avoir Python 3 installe sur votre ordinateur
- Avoir installe les bibliotheques `skimage`, `sklearn`, et `csv` en utilisant la commande `pip install scikit-image sklearn csv`

## Comment utiliser ce code

1. Placez vos images dans le dossier `dataset/`
2. Placez les etiquettes des images dans un fichier CSV nomme `label.csv`. Chaque ligne du fichier doit contenir le nom de l'image et sa classe, separes par une virgule.
3. Executez le code en utilisant la commande `python preprocess.py` dans votre terminal. Le code creera un dossier `dataset_cleaned/` et y enregistrera les images pretraitees ainsi que les etiquettes dans un fichier CSV nomme `labels.csv`.

## Fonctionnement du code

Le code commence par definir une fonction `preprocess_image` qui prend en entree le nom de l'image et son etiquette et renvoie l'image pretraitee. La fonction effectue les etapes suivantes :

4. Chargement de l'image a partir du fichier
5. Redimensionnement de l'image a une taille de 200x200 pixels
6. Normalisation des valeurs de pixel de l'image
7. Appliquer un filtre de median pour enlever le bruit de l'image

Le code principal ouvre ensuite le fichier CSV des etiquettes en mode lecture et lit chaque ligne du fichier. Pour chaque ligne, il recupere le nom de l'image et son etiquette, puis appelle la fonction `preprocess_image` pour pretraiter l'image. Le code enregistre ensuite l'image pretraitee dans le dossier `dataset_cleaned/` et enregistre l'etiquette de l'image dans le fichier CSV `labels.csv`.