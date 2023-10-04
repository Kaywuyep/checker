#!/usr/bin/env python3
import argparse
from checker import (
    get_files_with_supported_extensions,
    check_style,
    format_code,
)
from _git import stage_and_commit


def main():
    parser = argparse.ArgumentParser(
        description="Code formatting and style checking script.")
    parser.add_argument("filenames",
                        nargs="*",
                        help="List of filenames to format and check.")
    parser.add_argument("directory",
                        nargs="?",
                        default=".",
                        help="Directory to search for files.")
    parser.add_argument("commit_message",
                        help="Commit message for the changes.")
    args = parser.parse_args()

    filenames = get_files_with_supported_extensions(args.directory)

    if not filenames:
        print(f"No supported files found in {args.directory}. Exiting.")
    else:
        format_code(filenames)
        check_style(filenames)
        stage_and_commit(args.commit_message)


if __name__ == "__main__":
    main()
