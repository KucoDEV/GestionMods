<h1 align="center">Minecraft Mod Manager</h1>

<div align="center">
    <p>Script Python pour basculer rapidement entre différentes versions de mods Minecraft selon la version du jeu utilisée.</p>
    <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/Python/python3.svg">
</div>

<br>

# Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Pré-requis](#pré-requis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du dossier mods](#structure-du-dossier-mods)
- [Avertissements](#avertissements)

# Fonctionnalités

- Suppression automatique des mods existants dans le dossier `mods`
- Chargement des mods correspondant à une version spécifiée de Minecraft
- Gestion simplifiée des mods sans manipulation manuelle

# Pré-requis

- Python 3 installé
- Structure de dossier correcte dans `C:/Users/VOTRE_NOM/AppData/Roaming/.minecraft/mods/`  
  *(Remplacez `VOTRE_NOM` par votre nom d’utilisateur Windows)*

# Installation

1. Cloner ce dépôt :
   ```bash
   git clone https://github.com/KucoDEV/GestionMods.git
   ```

2. Se déplacer dans le dossier :

   ```bash
   cd GestionMods
   ```

3. Vérifier que Python est bien installé et accessible.

# Utilisation

1. Modifier la variable `MINECRAFT_MODS_PATH` dans `main.py` :

   ```python
   MINECRAFT_MODS_PATH = "C:/Users/VOTRE_NOM/AppData/Roaming/.minecraft/mods"
   ```

2. Lancer le script :

   ```bash
   python main.py
   ```

3. Entrer la version de Minecraft voulue (ex: `1.16.5`).

Le script supprimera les mods actuels puis copiera ceux de la version demandée.

# Structure du dossier `mods`

Organisez vos mods ainsi :

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

Seuls les mods de la version sélectionnée seront présents dans le dossier `mods` après exécution.

# Avertissements

* Sauvegardez vos mods avant utilisation.
* Assurez-vous que les `.jar` sont bien dans les bons sous-dossiers.
* 
# Contributeurs

Merci aux personnes et ressources ayant contribué au projet :

- [KucoDEV](https://github.com/KucoDEV) — Développement principal, conception et maintenance.
- [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) — Sécurité et bonnes pratiques.

Vous souhaitez contribuer ? Consultez le [guide de contribution](CONTRIBUTING.md) ou ouvrez une *issue* pour proposer des améliorations.

<p align="center">
    <img alt="Footer" src="https://i.imgur.com/9Ojjug7.png">
    <br><br>
    <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/LicenceMIT/licencemit3.svg">
</p>
