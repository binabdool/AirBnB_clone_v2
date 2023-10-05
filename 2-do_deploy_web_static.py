#!/usr/bin/python3
"""
This module contains a function used to deploy the archived html scripts to
out server
"""

import os
from fabric.api import *
from pathlib import Path


env.hosts = ['3.90.82.95', '54.157.156.207']


def do_deploy(archive_path):
    """
    Function to respectively deploy the static to their respective locations
    on server
    """
    pathObj = Path(archive_path)
    if not pathObj.exists:
        return False

    tmpDest = f"/tmp/{pathObj.name}"
    destDir = f"/data/web_static/releases/{pathObj.stem}/"
    put(archive_path, tmpDest)
    exec_1 = sudo(f"mkdir -p {destDir}")
    exec_2 = sudo(f"tar -xzf {tmpDest} -C {destDir}")
    exec_3 = sudo(f"rm {tmpDest}")
    exec_4 = sudo(f"mv {destDir}/web_static/* {destDir}")
    exec_5 = sudo(f"rm -rf {destDir}/web_static")
    exec_6 = sudo(f"rm -rf /data/web_static/current")
    exec_7 = sudo(f"ln -s {destDir} /data/web_static/current")
    exec_list = [exec_1, exec_2, exec_3, exec_4, exec_5, exec_6, exec_7]
    return True if all([obj.succeeded for obj in exec_list]) else False
