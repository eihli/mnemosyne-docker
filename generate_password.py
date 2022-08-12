#!/usr/bin/env python3
import argparse
from argon2 import PasswordHasher

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a password hash and update config.py to use it."
    )
    parser.add_argument("username", type=str)
    parser.add_argument("password", type=str)
    args = parser.parse_args()

    ph = PasswordHasher()
    hashed = ph.hash(args.password)


    print("Updating the username/password in config.py to the following:")
    print(f"Username: {args.username}\nPassword: {hashed}")

    towrite = []
    with open("config.py", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line.startswith("remote_access_password = "):
                towrite.append(
                    f'remote_access_password = os.environ.get("MNEMOSYNE_REMOTE_ACCESS_PASSWORD", "{hashed}")\n'
                )
            elif line.startswith("remote_access_username = "):
                towrite.append(
                    f'remote_access_username = os.environ.get("MNEMOSYNE_REMOTE_ACCESS_USERNAME", "{args.username}")\n'
                )
            else:
                towrite.append(line)

    with open("config.py", "w", encoding="utf-8") as f:
        f.writelines(towrite)
