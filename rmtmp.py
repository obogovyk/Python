#! /usr/bin/env python

import os
import sys
import shutil


tmpfiles = [
    '~/.adobe',
    '~/Desktop',
    '~/.thumbnails',
    '~/.gconfd',
    '~/.gconf',
    '~/.pulse',
    '~/.dropbox-dist',
    '~/.parallel',
    '~/.dbus',
    '~/.viminfo',
    '~/.npm/',
    '~/.java/',
    '~/.oracle_jre_usage/',
    '~/.pylint.d/',
    '~/.qute_test/',
    '~/.cmake/',
    '~/.gnome/',
    '~/.w3m/',
]


def yesno(question, default="n"):
    """ Asks the user for YES or NO, always case insensitive.
        Returns True for YES and False for NO.
    """
    prompt = "%s (y/[n]) " % question

    ans = input(prompt).strip().lower()

    if not ans:
        ans = default

    if ans == "y":
        return True
    return False


def rmtmp():
    print("Found shittyfiles:")
    found = []
    for f in shittyfiles:
        absf = os.path.expanduser(f)
        if os.path.exists(absf):
            found.append(absf)
            print("    %s" % f)

    if len(found) == 0:
        print("No shitty files found :)")
        return

    if yesno("Remove all?", default="n"):
        for f in found:
            if os.path.isfile(f):
                os.remove(f)
            else:
                shutil.rmtree(f)
        print("All cleaned")
    else:
        print("No file removed")


if __name__ == '__main__':
rmtmp()
