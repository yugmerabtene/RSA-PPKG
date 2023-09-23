# Générateur de Clés RSA et Transfert vers un Serveur FTP

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Ce script génére une paire de clés RSA, de calculer leur empreinte (fingerprint) en utilisant l'algorithme de hachage SHA-256, et de transférer les clés vers un serveur FTP distant.

## Table des matières

- [Introduction](#introduction)
- [Exécution](#exécution)
- [Configuration FTP](#configuration-ftp)
- [Empreinte des clés](#empreinte-des-clés)
- [Contribuer](#contribuer)
- [License](#license)

## Introduction

Ce script utilise les bibliothèques Python suivantes :
- `os` pour la gestion des fichiers et la suppression locale des clés après le transfert.
- `ftplib` pour établir une connexion FTP avec un serveur distant et transférer les clés.
- `hashlib` pour calculer l'empreinte (fingerprint) des clés en utilisant l'algorithme de hachage SHA-256.
- `Crypto` pour générer une paire de clés RSA sécurisée.

## Exécution

Pour exécuter le script, assurez-vous d'avoir Python 3.8 ou une version ultérieure installée. Suivez ces étapes :

1. Clonez ce dépôt sur votre machine :

    ```bash
    git clone https://github.com/yugmerabtene/RSA-PPKG.git
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd RSA-PPKG
    ```

3. Exécutez le script :

    ```bash
    python nom_du_script.py
    ```

Le script générera une paire de clés RSA, calculera leur empreinte, les transférera vers le serveur FTP configuré, puis supprimera les fichiers locaux des clés.

## Configuration FTP

Pour configurer la connexion FTP, ouvrez le script et définissez les variables suivantes :

```python
FTP_HOST = ""  # Adresse du serveur FTP
FTP_USER = ""  # Nom d'utilisateur FTP
FTP_PASS = ""  # Mot de passe FTP
