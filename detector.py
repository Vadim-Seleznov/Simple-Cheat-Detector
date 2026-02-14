#!/usr/bin/env/python
import os
import zipfile

possible_names = [
    "wurst", "impact", "aristois", "meteor", "future", "sigma", "vape",
    "kronos", "lambda", "rusherhack", "pyro", "seppuku", "konas", "wild",
    "liquidbounce", "horion", "rhack", "pandaware", "expensive", "excellent",
    "nursultan", "celestial", "catlavan", "baritone", "wexside", "topka", "xorek",
    "automyst",
    
    "xray", "autoclicker", "hitbox", "hitboxes", "autobuy", "killaura", "aimassist",
    "triggerbot", "speedhack", "flyhack", "reach", "nofall", "fastplace",
    
    "hack", "bypass", "utility", "modmenu", "injector", "cheatengine"
]


RED = "\033[31m"
GREEN = "\033[32m"
GREY = "\033[90m"
RESET = "\033[0m"

HOME_DIR = os.path.expanduser("~")
DESKTOP_DIR = os.path.join(HOME_DIR, "Desktop")
DOWNLOADS_DIR = os.path.join(HOME_DIR, "Downloads")

LOGS_COUNT = 30

def print_detected(name: str, path: str) -> None: 
    print(f'{RED}CHEAT DETECTED:{RESET} {name} ({path})')

def print_logs(os_name: str) -> None:
    print(f"{GREEN}--------------------------------LOGS---------------------------------{RESET}")
    print(f"{GREEN}LATEST LOG: {RESET}")
    if os_name == "windows":
        path = os.path.join(HOME_DIR, "AppData", "Roaming", ".minecraft", "logs")
    elif os_name == "linux":
        path = os.path.join("/", "root", ".minecraft", "logs")

    for log in os.listdir(path):
        if log == "latest.log":
                with open(os.path.join(path, log)) as f:
                    for i in range(LOGS_COUNT):
                        print(f.readline())

def deep_search_in_mods(os_name: str) -> None:
    if os_name == "windows":
        path = os.path.join(HOME_DIR, "AppData", "Roaming", ".minecraft", "mods")
    elif os_name == "linux":
        path = os.path.join("/", "/root", ".minecraft", "mods")

    SUSPICIOUS_KEYWORDS = [
        "hitbox", "hitboxes", "reach", "killaura", "aimbot", "xray", "wallhack", "autoclicker",
    ]

    if not os.path.exists(path):
        print(f"{GREY}There is no mod path{RESET}")
        return

    # Tuple with (file_name, reason)
    suspicious_mods = []

    for file_name in os.listdir(path):
        if file_name.endswith(".jar"):
            jar_path = os.path.join(path, file_name)
            
            try:
                with zipfile.ZipFile(jar_path, 'r') as jar:
                    for inner_file in jar.namelist():
                        lower_name = inner_file.lower()
                        
                        if any(keyword in lower_name for keyword in SUSPICIOUS_KEYWORDS):
                            suspicious_mods.append((file_name, f"Suspect (name): {inner_file}"))
            except zipfile.BadZipFile:
                print(f"File {file_name} is broken or isn't a .jar")
    
    if suspicious_mods:
        print(f"{RED}Found suspect mods:{RESET}")
        for mod, reason in suspicious_mods:
            print(f"{mod} — {reason}")
    else:
        print(f"{GREEN}No suspect mods.{RESET}")


def deep_search_in_resourcepacks(os_name: str) -> None:
    if os_name == "windows":
        path = os.path.join(HOME_DIR, "AppData", "Roaming", ".minecraft", "resourcepacks")
    elif os_name == "linux":
        path = os.path.join("/", "root", ".minecraft", "resourcepacks")

    if not os.path.exists(path):
        print(f"{GREY}There is no resourcepacks path{RESET}")
        return

    SUSPICIOUS_KEYWORDS = [
        "xray", "cheat", "orefinder", "diamond_ore", "gold_ore", "iron_ore", "emerald_ore",
    ]

    # Also tuple with (file, reason)
    suspicious_packs = []

    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        
        if file_name.endswith(".zip"):
            try:
                with zipfile.ZipFile(full_path, 'r') as pack:
                    for inner_file in pack.namelist():
                        lower_name = inner_file.lower()
                        if any(keyword in lower_name for keyword in SUSPICIOUS_KEYWORDS):
                            suspicious_packs.append((file_name, f"{RED}Suspect (name): {inner_file}{RESET}"))
            except zipfile.BadZipFile:
                print(f'File {file_name} is broken or not an .zip file')
        elif os.path.isdir(full_path):
            for root, _, files in os.walk(full_path):
                for fname in files:
                    lower_name = fname.lower()
                    if any(keyword in lower_name for keyword in SUSPICIOUS_KEYWORDS):
                        suspicious_packs.append((file_name, f"{RED}Suspect (name): {fname}{RESET}"))


    
    if suspicious_packs:
        print(f"{RED}FOUND SUSPECT PACKS{RESET}")
        for pack, reason in suspicious_packs:
            print(f"{pack} - {reason}")
    else:
        print(f"Didn't found any sus packs")

def name_matches(name: str) -> bool:
    lower_name = name.lower()
    return any(keyword in lower_name for keyword in possible_names)

def check_path(path: str) -> None:
    counter: int = 0

    try:
        for item in os.listdir(path):
            if name_matches(item):
                print_detected(item, path)
                counter += 1
    except FileNotFoundError:
        print(f"{GREY}Path not found: {path}{RESET}")
        counter = -1
    except PermissionError:
        print(f"{GREY}No access to: {path}{RESET}")
        counter = -1

    if counter == 0:
        print(f'{GREEN}PATH: {path} is clear{RESET}')
    elif counter > 0:
        print(f'{GREY}summary{RESET}: {RED}{counter}{RESET} suspect files in {GREY}\"{path}\"{RESET}')
    else:
        return

def check_disk(disk_letter: str) -> None:
    try:
        for item in os.listdir(f"{disk_letter}:/"):
            if name_matches(item):
                print_detected(item, f"{disk_letter}:/")
    except FileNotFoundError:
        print(f"{GREY}User doesn't have this disk: {disk_letter}{RESET}")

def appdata_check() -> None:
    roaming_path = os.path.join(HOME_DIR, "AppData", "Roaming")
    check_path(roaming_path)
    check_path(f"{HOME_DIR}/AppData/Local/Temp")
    check_path(os.path.join(roaming_path, ".minecraft"))
    check_path(os.path.join(roaming_path, ".minecraft", "config"))
    check_path(os.path.join(roaming_path, ".minecraft", "mods"))
    check_path(os.path.join(roaming_path, ".minecraft", "resourcepacks"))
    check_path(os.path.join(roaming_path, ".minecraft", "versions"))

def windows_logic() -> None:
    print(f'{GREY}USER IS RUNNING ON WINDOWS{RESET}')
    check_disk("C")
    check_disk("D")
    check_disk("E")
    appdata_check()
    check_path(DESKTOP_DIR)
    check_path(DOWNLOADS_DIR)
    print(f'{GREY}Deep search in mods (this is probably not cheats): {RESET}')
    deep_search_in_mods("windows")
    print(f'{GREY}Deep search in resource packs (this is probably not cheats){RESET}') 
    deep_search_in_resourcepacks("windows")
    print_logs("windows")
    input(f"\n{GREY}Click any button to close{RESET}\n")

def linux_logic() -> None:
    #GREETING
    print(f'{GREY}USER IS RUNNING ON LINUX OR MACOS{RESET}')
    
    # ROOT "/"
    print(f'{GREY}CHECK IN ROOT FOLDER...{RESET}')
    check_path(HOME_DIR)
    check_path("/root")

    # .minecraft
    check_path(os.path.join("/", "root", ".minecraft"))
    check_path(os.path.join(HOME_DIR, ".minecraft"))

    check_path(os.path.join("/", "root", ".minecraft", "config"))
    check_path(os.path.join(HOME_DIR, ".minecraft", "config"))

    check_path(os.path.join("/", "root", ".minecraft", "mods"))
    check_path(os.path.join(HOME_DIR, ".minecraft", "mods"))

    check_path(os.path.join("/", "root", ".minecraft", "resourcepacks"))
    check_path(os.path.join(HOME_DIR, ".minecraft", "resourcepacks"))

    check_path(os.path.join("/", "root", ".minecraft", "versions"))
    check_path(os.path.join(HOME_DIR, ".minecraft", "versions"))

    print(f'{GREY}Deep search in mods (this is probably not cheats): {RESET}')
    deep_search_in_mods("linux")


    print(f'{GREY}Deep search in resource packs (this is probably not cheats){RESET}') 
    deep_search_in_resourcepacks("linux")
    
    print_logs("linux")

    input(f"\n{GREY}Click any button to close{RESET}\n")

if __name__ == "__main__":
    print(f'{GREEN}Program has started{RESET}')
    if os.name == "nt":
        windows_logic()
    elif os.name == "posix":
        linux_logic()

