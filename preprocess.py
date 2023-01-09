import csv
from skimage import io
from skimage.transform import resize
from sklearn.preprocessing import normalize
from skimage.filters import median_filter
import os

def preprocess_image(image_name, image_label):
    # Charger l'image à partir du fichier
    image = io.imread(f"dataset/{image_name}")

    # Redimensionner l'image à une taille de 200x200 pixels
    image_resized = resize(image, (200, 200))

    # Normaliser les valeurs de pixel de l'image
    image_normalized = normalize(image_resized)

    # Appliquer un filtre de médian pour enlever le bruit de l'image
    image_filtered = median_filter(image_normalized)

    return image_filtered

# Ouvrir le fichier CSV en mode lecture
with open('label.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Créer un dossier pour enregistrer les images nettoyées s'il n'existe pas déjà
    if not os.path.exists("dataset_cleaned"):
        os.makedirs("dataset_cleaned")

    # Ouvrir le fichier CSV pour les étiquettes en mode ajout
    with open("dataset_cleaned/labels.csv", mode='a') as labels_file:
        csv_writer = csv.writer(labels_file)

        # Pour chaque ligne du fichier CSV
        for row in csv_reader:
            # Récupérer le nom de l'image et sa classe
            image_name = row[0]
            image_label = row[1]

            # Prétraiter l'image
            image_processed = preprocess_image(image_name, image_label)

            # Enregistrer l'image nettoyée dans le dossier dataset_cleaned/
            io.imsave(f"dataset_cleaned/{image_name}", image_processed)

            # Enregistrer l'étiquette de l'image dans le fichier CSV des étiquettes
            csv_writer.writerow([image_name, image_label])