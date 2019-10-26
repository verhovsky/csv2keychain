# сsv2keychain #

[![PyPI](https://img.shields.io/badge/pypi-v0.1.3-blue.svg)](https://pypi.python.org/pypi/cmdline-csv2keychain/0.1.3)
[![Python](https://img.shields.io/badge/python-3.4-green.svg)](https://pypi.python.org/pypi?name=cmdline-csv2keychain&version=0.1.0&:action=display)

## About ##

Small command-line tool for adding exported credentials (login/password pairs) from Chrome to the macOS keychain

**macOS 10.15 Catalina** tested

## Installing ##

You can install the package via *pip*

```bash
pip3 install cmdline-csv2keychain
```

## Preparing credentials from Chrome ##

First, you need to export paswords from Google Chrome to a *.csv* file

1. In Google Chrome, go to Settings (`⌘-,`) → Autofill → Passwords
    - or you can type `chrome://settings/passwords` into the URL bar.
2. Click the triple dot next to "Saved Passwords" → Export passwords... and confirm that you want to export the passwords
3. Type in your password
4. Save As: Chrome Passwords, Where: Downloads

## Running the script on the file you exported from Chrome ##

1. Open up the terminal (`⌘-,` and type "Terminal" and hit Enter)
2. Paste the following command and hit Enter

```bash
csv2keychain "~/Downloads/Chrome Passwords.csv"
```

## Usage ##

```bash
csv2keychain [path.csv] [-u] [-s]
```

- `-u` - update existing password for every account in keychain, if any
- `-s` - display credentials on the screen during the process

## Example ##

```bash
csv2keychain ~/Desktop/credentials.csv -s
```

Now your Chrome passwords are available for Safari & other apps :)
