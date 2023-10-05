#!/usr/bin/python3
"""
This module contains a function that deploy web static files/folders to our
server"""

from fabric.api import *

env.hosts = ['3.90.82.95', '54.157.156.207']

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

archive_path = do_pack()


def deploy():
    """
    Function that create and distribute an archive to the listed archives
    """
    if not archive_path:
        return False
    return do_deploy(archive_path)
