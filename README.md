# Minecraft Mod Manager

This Python script allows you to quickly switch between different versions of Minecraft mods based on the game version you are using.

## Features
- Automatically removes existing mods in the `mods` folder
- Loads specific mods for a given version
- Simplifies Minecraft mod management without manual file movement

## Prerequisites
- Python 3 installed on your system
- A structured folder with subfolders for each mod version in the directory `C:/Users/YOUR_NAME/AppData/Roaming/.minecraft/mods/ (replace YOUR_NAME with your Windows username)`

## Installation
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/your-username/repository-name.git
   ```
2. Navigate to the project folder:
   ```sh
   cd repository-name
   ```
3. Ensure Python is installed and accessible from your terminal.

## Usage
1. Open `main.py` and modify the `MINECRAFT_MODS_PATH` variable to match your Windows username:
   ```python
   MINECRAFT_MODS_PATH = "C:/Users/YOUR_NAME/AppData/Roaming/.minecraft/mods"
   ```
2. Run the script using the following command:
   ```sh
   python main.py
   ```
3. Enter the Minecraft version for which you want to activate mods.
4. The script will delete old mods and copy the ones corresponding to the specified version.

## `mods` Folder Structure
The `mods` folder should be structured as follows:
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

The script ensures that only the mods for the selected version are present in the main `mods` folder.

## Warning
- Make sure to back up your mods before using the script.
- Verify that `.jar` files are correctly placed in their respective folders.

## License
This project is licensed under the MIT license. You are free to modify and redistribute it.
