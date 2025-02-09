# Gestionnaire de Mods Minecraft

Ce script Python permet de basculer rapidement entre différentes versions de mods pour Minecraft en fonction de la version du jeu utilisée.

## Fonctionnalités
- Suppression automatique des mods existants dans le dossier `mods`
- Chargement des mods spécifiques à une version donnée
- Gestion simplifiée des mods Minecraft sans devoir les déplacer manuellement

## Prérequis
- Python 3 installé sur votre système
- Un dossier organisé avec des sous-dossiers pour chaque version de mods dans le répertoire `C:/Users/VOTRE_NOM/AppData/Roaming/.minecraft/mods/ (remplacez VOTRE_NOM par votre nom d'utilisateur Windows)`

## Installation
1. Clonez ce dépôt sur votre machine locale :
   ```sh
   git clone https://github.com/votre-utilisateur/nom-du-repo.git
   ```
2. Accédez au dossier du projet :
   ```sh
   cd nom-du-repo
   ```
3. Assurez-vous que Python est installé et accessible depuis votre terminal.

## Utilisation
1. Ouvrez `main.py` et modifiez la variable `MINECRAFT_MODS_PATH` pour qu'elle corresponde à votre nom d'utilisateur Windows :
   ```python
   MINECRAFT_MODS_PATH = "C:/Users/VOTRE_NOM/AppData/Roaming/.minecraft/mods"
   ```
2. Exécutez le script avec la commande suivante :
   ```sh
   python main.py
   ```
3. Entrez la version de Minecraft pour laquelle vous souhaitez activer les mods.
4. Le script supprimera les anciens mods et copiera les mods correspondants à la version spécifiée.

## Structure du dossier `mods`
Le dossier `mods` doit être organisé de la manière suivante :
```
.minecraft/
  ├── mods/
  │   ├── 1.16.5/
  │   │   ├── mod1.jar
  │   │   ├── mod2.jar
  │   ├── 1.18.2/
  │   │   ├── mod3.jar
  │   │   ├── mod4.jar
```

Le script s'assurera que seuls les mods de la version sélectionnée sont présents dans le dossier `mods` principal.

## Avertissement
- Assurez-vous de sauvegarder vos mods avant d'utiliser le script.
- Vérifiez que les fichiers `.jar` sont bien placés dans les dossiers respectifs.

## Licence
Ce projet est sous licence MIT. Vous êtes libre de le modifier et de le redistribuer.