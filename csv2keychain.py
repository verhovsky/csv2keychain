#!/usr/bin/env python3

import argparse
import csv
import subprocess
from sys import argv
from urllib.parse import urlparse

__version__ = "0.2.0"


def addkey(name, url, username, password, *, update=False):
    url = urlparse(url)
    domain = url.netloc
    path = url.path

    syscall = [
        "security",
        "add-internet-password",
        "-l",
        f"{domain} ({username})",
        "-s",
        domain,
        "-p",
        path,
        "-a",
        username,
        "-t",
        "form",
        "-r",
        "{:<4}".format(url.scheme[0:4]),
        "-T",
        "/Applications/Safari.app",
        "-w",
        password,
    ]
    if update:
        syscall.append("-U")

    subprocess.run(syscall)


def display_row(row):
    print(row)


def main():
    parser = argparse.ArgumentParser(description=f"csv2keychain version {__version__}.")
    parser.add_argument(
        "-s",
        "--show-passwords",
        action="store_true",
        help="display each password before adding it",
    )
    parser.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="update existing passwords. Any password that you already have in the key "
        "chain that are also in the file exported from Chrome will be overwritten.",
    )
    parser.add_argument("csv_file", help="the path to the csv file to process")
    args = parser.parse_args()

    with open(args.csv_file) as csvfile:
        reader = csv.reader(csvfile)
        print("File opened")
        next(reader)  # Skip header
        for counter, row in enumerate(reader, start=1):
            print(f"Copying item #{counter}...")
            if args.show_passwords:
                display_row(row)
            addkey(*row, update=args.update)
            print(f"#{counter} complete")


if __name__ == "__main__":
    main()
