# Générateur de Clés RSA et Transfert FTP

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Ce script génère une paire de clés RSA, calcule leur empreinte avec SHA-256, et transfère les clés vers un serveur FTP.

## Table des matières

- [Installation](#installation)
- [Configuration](#configuration)
- [Exécution](#exécution)
- [Fonctionnalités](#fonctionnalités)
- [License](#license)

## Installation

```bash
git clone https://github.com/yugmerabtene/RSA-PPKG.git
cd RSA-PPKG
pip install -r requirements.txt
```

## Configuration

Créez un fichier `.env` à partir de l'exemple :

```bash
cp .env.example .env
```

Puis remplissez les informations de connexion FTP :

```
FTP_HOST=votre-serveur-ftp.com
FTP_USER=votre_utilisateur
FTP_PASS=votre_mot_de_passe
```

## Exécution

```bash
python rsa_keygen.py
```

Le script :
1. Génère une paire de clés RSA 2048 bits
2. Affiche l'empreinte SHA-256 de chaque clé
3. Transfère les clés via FTP
4. Supprime les fichiers locaux

## Fonctionnalités

- Génération de clés RSA sécurisées
- Calcul d'empreinte SHA-256
- Transfert FTP sécurisé (config via variables d'environnement)
- Nettoyage automatique des fichiers locaux
- Gestion basique des erreurs

## License

MIT
