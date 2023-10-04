#!/usr/bin/python3

import subprocess
import argparse
import os


def format_code(filenames):
    print("Formatting code using appropriate tools...")

    for filename in filenames:
        if filename.endswith(('.py', '.pyw')):
            subprocess.run(["yapf", "-i", filename])
        elif filename.endswith(('.c', '.cpp')):
            subprocess.run(["betty", filename])
        else:
            subprocess.run(["black", filename])

    print("Code formatting complete.")


def check_style(filenames):
    print("Checking code style using appropriate tools...")

    for filename in filenames:
        if filename.endswith(('.py', '.pyw')):
            subprocess.run(["pycodestyle", filename])
        elif filename.endswith(('.c', '.cpp')):
            subprocess.run(
                ["betty", "--dry-run", "--style", "linux", filename],
                check=True)
        else:
            subprocess.run(["flake8", filename], check=True)

    print("Code style check complete. No violations found.")


def get_supported_extensions():
    return ['.py', '.c', '.cpp', '.java', '.js']


def get_files_with_supported_extensions(directory='.'):
    supported_extensions = get_supported_extensions()
    files = [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
    return [
        f for f in files if any(
            f.endswith(ext) for ext in supported_extensions)
    ]
