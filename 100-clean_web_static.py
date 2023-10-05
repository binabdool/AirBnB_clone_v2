#!/usr/bin/python3
"""
This module contains a function that deletes out of date archive files on my
local machine as well as server
"""

import os
from fabric.api import cd, env, local, run
from pathlib import Path

env.hosts = ['3.90.82.95', '54.157.156.207']


def do_clean(number=0):
    """
    remove outdated archive files from the versions directory

    @number: number is the number of the archives, including the most recent,
to  keep.
       If number is 0 or 1, keep only the most recent version of your archive.
       if number is 2, keep the most recent, and second most recent versions
        of your archiveetc.
    """
    number = 1 if number == 0 else int(number)

    fileNames = [Path(i) for i in os.listdir("versions")]
    for fullPath in fileNames[:-number]:
        local(f"rm -r versions/{fullPath.name}")

    with cd("/data/web_static/releases"):
        fileNames = [i for i in run("ls").split()
                     if i.startswith("web_static_")]
        for fullPath in fileNames[:-number]:
            run(f"rm -r {fullPath}")
