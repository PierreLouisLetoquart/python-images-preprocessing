# Prétraitement des images avec TensorFlow

Ce code utilise TensorFlow pour charger des images à partir d'un répertoire `dataset` et les prétraiter en les redimensionnant à une taille de **100x100** pixels, en les **normalisant** (en divisant chaque pixel par 255) et en les convertissant en format entier 8 bits non signé (uint8). Les images prétraitées sont ensuite enregistrées dans un répertoire `dataset/preprocessed/`.

## Prérequis

- TensorFlow

Pour installer TensorFlow :

```bash
pip install tensorflow
```

## Exécution

Assurez-vous que vous avez un fichier `labels.json` qui contient des informations sur les images à traiter, avec un format similaire à ceci :

```json
[
    {
        "image": "image1",
        "extension": "jpg"
    },
    {
        "image": "image2",
        "extension": "png"
    },
    ...
]
```

Les images doivent être stockées dans le répertoire `dataset/` et doivent avoir les extensions spécifiées dans le fichier `labels.json`.

**Exécutez le script :**

```bash
python preprocess.py
```

Le code créera automatiquement un répertoire `dataset/preprocessed` pour stocker les images prétraitées.

## Note

Il y a un problème dans le code actuel qui déforme les images lors de leur redimensionnement. Il est donc nécessaire de résoudre ce problème avant d'utiliser ce code en production. Il existe plusieurs méthodes pour redimensionner les images de manière à préserver les proportions, telles que l'utilisation de la méthode `resize` de TensorFlow qui prend en compte les paramètres `method` ou `Preserve_aspect_ratio` ou encore utiliser d'autres libraries.

Il est important de tester le code après avoir réglé ce problème pour vérifier que les images ne sont plus déformées.

### To fix

- Les images sont déformées lors du redimensionnement, il faut utiliser une autre méthode ou des paramètres pour préserver les proportions de l'image pendant le redimensionnement.
