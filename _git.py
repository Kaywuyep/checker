#!/usr/bin/python3
import subprocess


def stage_and_commit(message):
    print("Staging changes...")
    subprocess.run(["git", "add", "."])

    print("Committing changes...")
    subprocess.run(["git", "commit", "-m", message])
    print("Changes committed successfully.")
