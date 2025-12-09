import subprocess
import sys
import os
import shutil
import urllib.request

RED = "\033[31m"
GREEN = "\033[32m"
GREY = "\033[90m"
RESET = "\033[0m"

def update() -> None:
    url = "https://raw.githubusercontent.com/Vadim-Seleznov/vvcommit/main/vvcommit.py"
    script_path = os.path.realpath(sys.argv[0])
    backup_path = script_path + ".bak"

    print("Starting update...")

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode("utf-8")

        shutil.copy2(script_path, backup_path)
        print(f"Backup created at: {backup_path}")

        with open(script_path, "w", encoding="utf-8") as f:
            f.write(data)

        print("Update completed successfully!")
        print("Restart the script to use the new version.")

    except Exception as e:
        print(f"Update failed: {e}")
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, script_path)
            print("Restored backup version.")
        sys.exit(1)

    sys.exit(0)

def usage_general() -> None:
    print(f"{RED}ERROR{RESET}: {GREY}usage: python ./vvcommit.py request commit_message{RESET}")
    print(f"{RED}Request options:{RESET}")
    print(f"{GREEN}curr - git commit and push into current branch{RESET}")
    print(f"{GREEN}main - git commit and push into main{RESET}")
    print(f"{GREEN}branch - git commit and push into specific branch{RESET}")
    printf(f"{GREEN}help - for getting help with tool{RESET}")
    sys.exit(1)

def help() -> None:
    print(f"{GREY}--------------------VV HELP----------{RESET}")
    print(f"{RED}Request options:{RESET}")
    print(f"{GREEN}curr - git commit and push into current branch{RESET}")
    print(f"{GREEN}main - git commit and push into main{RESET}")
    print(f"{GREEN}branch - git commit and push into specific branch{RESET}")
    print(f"{GREEN}If you use branch request you should give extra argument with branch name{RESET}")
    print(f"{GREEN}EXAMPLE:{RESET} python ./vvcommit.py branch \"main\" \"small fix\"")
    sys.exit(0)


def usage_branch() -> None:
    print(f"{RED}ERROR{RESET}: {GREY}usage: python ./vvcommit.py branch branch-name commit_message{RESET}")
    sys.exit(1)

def commit_curr(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)
    subprocess.run(["git", "push"])

    print(f'{GREEN}Successful commit{RESET}: {commit_message}')

def commit_main(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)

    subprocess.run(["git", "push", "origin", "main"])

    print(f'{GREEN}Successful commit: {commit_message}{RESET}')

def commit_branch(branch: str, commit_message) -> None:
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)

    subprocess.run(["git", "push", "origin", branch])

    print(f'{GREEN}Successful commit: {commit_message} into branch: {branch}{RESET}')

if __name__ == "__main__":
    print("Welcome from vvcommit!")
    
    if len(sys.argv) < 2:
        usage_general()

    request = sys.argv[1]


    if request == "help":
        help()
    elif request == "update":
        update()

    if len(sys.argv) < 3:
        usage_general()
        
    commit_message = sys.argv[2]
    
    if request == "branch":
        if len(sys.argv) < 4:
            usage_branch()
        
        branch = sys.argv[2]
        commit_message = sys.argv[3]
        commit_branch(branch, commit_message)
    elif request == "curr":
        commit_curr(commit_message)
    elif request == "main":
        commit_main(commit_message)
    else:
        print(f"{RED}ERROR:{RESET} no such request!")
        usage_general()

