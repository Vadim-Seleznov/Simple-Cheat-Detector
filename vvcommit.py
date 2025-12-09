#!/usr/bin/env/python
import subprocess
import sys

def usage() -> None:
    print("ERROR: usage: vvcommit.py commit-message")
    sys.exit(1)

if __name__ == "__main__":
    print("Welcome from vvcommit!")
    if len(sys.argv) < 2:
        usage()

    commit_message = sys.argv[1]

    subprocess.run(["git", "add", "."])

    subprocess.run(["git", "commit", "-m", commit_message])

    subprocess.run(["git", "push", "origin", "main"])

    print(f'Successfull commit: {commit_message}')
