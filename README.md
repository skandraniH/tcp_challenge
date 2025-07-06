
# TCP Challenge Solver

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un outil Python pour résoudre automatiquement les challenges TCP de type "square root and multiply" du site Root-Me.

## Fonctionnalités

- Connexion automatique aux serveurs TCP de Root-Me
- Analyse et parsing des messages du serveur
- Calcul précis des opérations mathématiques demandées
- Réponse en moins de 2 secondes comme exigé
- Gestion robuste des erreurs de connexion

## Prérequis

- Python 3.8+
- Bibliothèques requises :
  ```bash
  pip install socket math re

 Installation 
1.Cloner le dépôt :

git clone https://github.com/skandraniH/tcp_challenge.git

cd tcp_challenge

2.Exécuter le script :
python rootme1.py

Utilisation
Le script fonctionne automatiquement après l'exécution :
# Exemple de sortie
Received: Calculate the square root of 81 and multiply by 8842 =
Numbers extracted: 81, 8842
Sending: 79578.00
Server response: [OK] Valid answer! Flag: CM{Ex3mpl3_Fl4g}

Structure du code
tcp_challenge/
├── rootme1.py            # Script principal
├── README.md             # Documentation
└── requirements.txt      # Dépendances
