# Hello everyone!    

This is a simple Python project I personally made in my free time in about ~2 hours.  
It detects all basic cheats, including Xray.  

> 💡 P.S. Initially, I wanted to mark all resource packs that somehow affect the alpha channel of `.png` images as suspicious, but I decided to remove this since almost all resource packs do this.  
> Xray is not the kind of cheat to really fear in the modern world, especially on servers like RW and HW.  

---

## VVCOMMIT
VVCOMMIT - project powered by vvcommit https://github.com/Vadim-Seleznov/vvcommit

## ⚠️ IMPORTANT

This program mainly detects cheats **by names**.  

Some might ask: "What stops someone from renaming the cheat folder?"  
Actually, it’s not that simple 🙂  

For example, if you rename the folder `Nursultan` on drive C, the cheat itself will no longer be able to find it and:  
- either it won’t start,  
- or it will crash.  

(*I haven’t played Minecraft in a long time, so I might be wrong. You can correct me on Discord: `vadeicy`.*)  

---

## 🔍 What does the program do?

- Scans the computer for cheats (by folder/file names and sometimes by class names inside mods).  
- Checks:  
  - Desktop,  
  - Downloads,  
  - All drives,  
  - Home directory,  
  - `AppData/Roaming`,  
  - Minecraft itself.  
- At the end, it outputs logs from `.minecraft/logs` (helpful to see when the player last played and if they rejoined during the scan).  

All suspicious names can be found at the start of the code in the `possible_names` variable and sometimes inside functions (you can also add your own there).  

---

## 🚀 How to use?

**CURRENTLY, THE .EXE FILE USES AN OLD VERSION OF THE PROGRAM:**  
IT IS RECOMMENDED TO BUILD THE PROGRAM MANUALLY (IF YOU ARE ON LINUX, it’s simple: `chmod +x detector` then `./detector`)  

1. In the project’s `dist` folder, there is a ready-made `.exe` file.  
   - You can download it yourself.  
   - Or give it to the "cheater".  
   - If you don’t trust the `.exe`, build the project yourself.  

2. The program code is in a single file, so Git is not required.  
   - Just copy and paste into a file (`main.py` or `detector.py`).  

3. Install Python and PyInstaller:  
   ```bash
   pip install pyinstaller

4. Build the project:

pyinstaller --onefile {your_filename}

## LICENSE
MIT
