# Copyright (c) 2018 RoastingMalware
# See the LICENSE file for more information

"""
Misc. functionality used by several modules
"""

from os.path import join
from sys import version
import hashlib
import termcolor
from core import config

def getChecksum(filename: str) -> str:
    """
    Returns the checksum for a given file
    """
    blocksize = 65536
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(blocksize), b''):
            sha256.update(block)
    return sha256.hexdigest()


def branding():
    """
    Prints the logo/ information about the software at startup
    """
    if config.getConfigurationValue("honeypot", "branding"):
        print("Camera Obscura [{0}, Python {1}]".format(
            termcolor.colored(getVersion(), 'yellow'), version))
        print("Hans, get ze {0}".format(
            termcolor.colored("Flammenwerfer", 'red', 'on_white')))
    debugModeEnabled = config.getConfigurationValue("honeypot", "debug")
    if debugModeEnabled is True:
        print(
            termcolor.colored(
                "For god's sake, disable the debug mode!",
                'red'))


def getVersion() -> str:
    """
    Get the version of the software
    """
    versionPath = join(config.ROOT, ".git/refs/heads/master")
    versionString = None
    with open(versionPath, 'r') as file:
        versionString = file.read()

    return versionString.strip()
