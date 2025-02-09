import os
import shutil

MINECRAFT_MODS_PATH = "C:/Users/VOTRE_NOM/AppData/Roaming/.minecraft/mods"

def switch_mods(version):
    version_path = os.path.join(MINECRAFT_MODS_PATH, version)
    
    if not os.path.exists(version_path):
        os.makedirs(version_path)
    
    for file in os.listdir(MINECRAFT_MODS_PATH):
        file_path = os.path.join(MINECRAFT_MODS_PATH, file)
        if os.path.isfile(file_path) and file.endswith(".jar"):
            os.remove(file_path)
    
    version_mods = [f for f in os.listdir(version_path) if f.endswith(".jar")]
    for mod in version_mods:
        shutil.copy(os.path.join(version_path, mod), os.path.join(MINECRAFT_MODS_PATH, mod))

def main():
    version = input("Entrez la version de Minecraft pour laquelle vous voulez activer les mods : ")
    switch_mods(version)

if __name__ == "__main__":
    main()