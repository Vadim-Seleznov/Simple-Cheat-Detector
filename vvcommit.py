import subprocess
import sys
import os
import shutil
import urllib.request

# CONSTANTS WITH CONSOLE COLORS
RED = "\033[31m"
GREEN = "\033[32m"
GREY = "\033[90m"
RESET = "\033[0m"

# UPDATE FUNCTION
# With this function you can get newest version of script from github with only 1 command
# also it has --no-backup flag if you dont want to save backup for older version
def update(flag: str) -> None:
    url = "https://raw.githubusercontent.com/Vadim-Seleznov/vvcommit/main/vvcommit.py"
    script_path = os.path.realpath(sys.argv[0])
    backup_path = script_path + ".bak"

    print("Starting update...")

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode("utf-8")

        if flag == "backup":
            shutil.copy2(script_path, backup_path)
            print(f"{GREY}Backup created at: {backup_path}{RESET}")

        with open(script_path, "w", encoding="utf-8") as f:
            f.write(data)

        print(f"{GREEN}Update completed successfully!{RESET}")

    except Exception as e:
        print(f"{RED}ERROR Update failed {RESET}: {e}")
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, script_path)
            print(f"{GREEN}Restored backup version.{RESET}")
        sys.exit(1)

    sys.exit(0)

def help() -> None:
    print(f"{GREY}--------------------VV HELP----------{RESET}")
    print(f"{RED}Request options:{RESET}")
    print(f"{GREEN}curr - git commit and push into current branch{RESET}")
    print(f"{GREEN}main - git commit and push into main{RESET}")
    print(f"{GREEN}branch - git commit and push into specific branch{RESET}")
    print(f"{GREEN}pull - git pull or git pull origin \"branch-name\" if you provide an argument (python ./vvcommit.py pull (optional branch name)){RESET}")
    print(f"{GREEN}init - to init github repo in current directory from scratch with github-login and repo-name{RESET}")
    print(f"{GREEN}push-ex - pushing stuff into existing github repo using github-login and repo-name{RESET}")
    print(f"{GREEN}update - for getting newest version of tool from github! (--no-backup for not creating .bak file){RESET}")
    print(f"{GREEN}If you use branch request you should give extra argument with branch name{RESET}")
    print(f"{GREEN}EXAMPLE:{RESET} python ./vvcommit.py branch \"main\" \"small fix\"")
    sys.exit(0)

def usage(message: str) -> None:
    print(f'{RED}ERROR{RESET}: {GREY}usage: python ./vvcommit.py {message}{RESET}')
    sys.exit(1)

# ADD AND COMMIT + PUSH STUFF INTO CURRENT BRANCH WITH SIMPLE COMMAND
def commit_curr(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)
    subprocess.run(["git", "push"])

    print(f'{GREEN}Successful commit{RESET}: {commit_message}')

# ADD + COMMIT + PUSH STUFF INTO MAIN BRANCH
def commit_main(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)

    subprocess.run(["git", "push", "origin", "main"])

    print(f'{GREEN}Successful commit: {commit_message}{RESET}')

# ADD + COMMIT + PUSH STUFF INTO SPECIFIC BRANCH
def commit_branch(branch: str, commit_message) -> None:
    subprocess.run(["git", "add", "."])

    result = subprocess.run(["git", "commit", "-m", commit_message])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)

    subprocess.run(["git", "push", "origin", branch])

    print(f'{GREEN}Successful commit: {commit_message} into branch: {branch}{RESET}')

# PULL STUFF FROM CURRENT OR SPECIFIC BRANCH
def pull(branch: str = "none") -> None:
    if branch == "none":
        subprocess.run(["git", "pull"])
    else:
        subprocess.run(["git", "pull", "origin", branch])

    sys.exit(0)

# INIT GIT REPO FROM ABSOLUTELY FROM SCRATCH
# to use it just go to github website create new repo
# then use init command with yours username + repo-name
def init(login: str, repo: str) -> None:
    subprocess.run(["git", "init", "."])
    subprocess.run(["git", "add", "."])
    result = subprocess.run(["git", "commit", "-m", "Initial commit"])
    if result.returncode != 0:
        print(f"{RED}Commit failed!{RESET}")
        sys.exit(1)
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin", f'https://github.com/{login}/{repo}.git'])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    sys.exit(0)

# PUSH STUFF INTO EXISTING GITHUB REPO (also using username and repo-name)
def push_ex(login: str, repo: str) -> None:
    subprocess.run(["git", "remote", "add", "origin", f'https://github.com/{login}/{repo}.git'])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    sys,exit(0)

# MAIN FUNCTION
def main() -> None:
    print(f"{GREEN}Welcome from vvcommit!{RESET}")
    
    if len(sys.argv) < 2:
        usage("request")

    request = sys.argv[1]

    if request == "init":
        if len(sys.argv) != 4:
            usage("init github-login repo-name")

        user_login = sys.argv[2]
        repo = sys.argv[3]
        init(user_login, repo)

    if request == "push-ex":
        if len(sys.argv) != 4:
            usage("push-ex github-login repo-name")

        user_login = sys.argv[2]
        repo = sys.argv[3]
        push_ex(user_login, repo)

    if request == "help":
        help()
    elif request == "update" and len(sys.argv) > 2:
        if sys.argv[2] == "--no-backup":
            update("no-backup")
        else:
            print(f"{RED}ERROR:{RESET} no such flag: {sys.argv[2]}")
            help()
    elif request == "update":
        update("backup")
    elif request == "pull":
        pull()

    if len(sys.argv) < 3:
        help()
        
    commit_message = sys.argv[2]
    
    if request == "branch":
        if len(sys.argv) < 4:
            usage("branch branch-name commit-message")
        
        branch = sys.argv[2]
        commit_message = sys.argv[3]
        commit_branch(branch, commit_message)
    if request == "pull":
        branch = sys.argv[2]
        pull(branch)
    elif request == "curr":
        commit_curr(commit_message)
    elif request == "main":
        commit_main(commit_message)
    else:
        print(f"{RED}ERROR:{RESET} no such request!")
        help()

if __name__ == "__main__":
    main()

