import json
import tensorflow as tf

# Charger les étiquettes à partir du fichier labels.json
with open("labels.json", "r") as f:
    labels = json.load(f)

# Boucle pour chaque image
for image_data in labels:
    # Construire le chemin d'accès à l'image
    image_path = "dataset/" + image_data["image"] + "." + image_data["extension"]

    # Charger l'image à l'aide de TensorFlow
    image_string = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image_string)

    # Prétraitement de l'image
    image = tf.image.resize(image, (100, 100))
    image = tf.cast(image, dtype=tf.float32) / 255.0
    image = tf.cast(image * 255, dtype=tf.uint8)
    
    # Enregistrer l'image prétraitée dans le dossier "dataset/preprocessed"
    preprocessed_path = "dataset/preprocessed/" + image_data["image"] + "." + image_data["extension"]
    tf.io.write_file(preprocessed_path, tf.image.encode_jpeg(image))
