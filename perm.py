#!/usr/bin/env python
""" Changes Permissoin for all files in the directory to the user """

import os

path = '.'


def cmd(file, user):
    # changing permission
    command = "sudo chown -v {} \"{}\" *".format(user, file)
    os.system(command)


if __name__ == "__main__":
    # getting the username
    user_name = os.popen('whoami').read()[:-1]
    # reading the directory
    walk = os.walk(path)
    # itterating through all files and folders
    print("Be Patient if disk size is large")
    for fo, su, fi in walk:
        cmd(fo, user_name)
        for file in fi:
            file = "{}/{}".format(fo, file)
            cmd(file, user_name)
    print("Done!\n")
