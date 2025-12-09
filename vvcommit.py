import subprocess
import sys

RED = "\033[31m"
GREEN = "\033[32m"
GREY = "\033[90m"
RESET = "\033[0m"

def usage_general() -> None:
    print(f"{RED}ERROR{RESET}: {GREY}usage: vvcommit.py request commit_message{RESET}")
    print(f"{RED}Request options:{RESET}")
    print(f"{GREEN}curr - git commit and push into current branch{RESET}")
    print(f"{GREEN}main - git commit and push into main{RESET}")
    print(f"{GREEN}branch - git commit and push into specific branch{RESET}")
    sys.exit(1)

def usage_branch() -> None:
    print(f"{RED}ERROR{RESET}: {GREY}usage: vvcommit.py request branch-name commit_message{RESET}")
    sys.exit(1)

def commit_curr(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])

    subprocess.run(["git", "commit", "-m", commit_message])

    subprocess.run(["git", "push"])

    print(f'{GREEN}Successfull commit{RESET}: {commit_message}')

def commit_main(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])

    subprocess.run(["git", "commit", "-m", commit_message])

    subprocess.run(["git", "push", "origin", "main"])

    print(f'{GREEN}Successfull commit: {commit_message}{RESET}')

def commit_branch(branch: str, commit_message) -> None:
    subprocess.run(["git", "add", "."])

    subprocess.run(["git", "commit", "-m", commit_message])

    subprocess.run(["git", "push", "origin", branch])

    print(f'{GREEN}Successfull commit: {commit_message} into branch: {branch}{RESET}')

if __name__ == "__main__":
    print("Welcome from vvcommit!")
    if len(sys.argv) < 3:
        usage_general()
    
    request = sys.argv[1]
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
