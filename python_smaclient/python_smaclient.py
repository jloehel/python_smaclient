#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import smapi

_version = "0.1.0"


def main():
    name = "python_smaclient"
    usage = "%(prog)s [FUNCTION] [OPTIONS] [PARAMETER]"
    description = "python_smaclient is tool which provides a line-mode interface to \n\
                   the z/VM System Management API (SMAPI). It is based on the great \n\
                   tool smaclient written by Leland Lucius."

    parser = argparse.ArgumentParser(prog=name, usage=usage, description=description)

    # Required Arguments
    parser.add_argument("function_name", nargs=1,
                        help="The SMAPI function name. To see all function names \n\
                              please type: %(prog)s list")
    parser.add_argument("-T", "--target",
                        required=True,
                        dest="target",
                        help="Set the target image or authorization entry name.")

    # Optional Arguments
    parser.add_argument("-H", "--hostname",
                        dest="smhost",
                        help="The hostname of the SMAPI server. Specify IUCV if SMAPI IUCV is desired.")
    parser.add_argument("-p", "--port",
                        dest="smport",
                        help="The port of the SMAPI server.")
    parser.add_argument("-U", "--username",
                        dest="smuser",
                        default="",
                        help="The authorized SMAPI userid.")
    parser.add_argument("-P", "--password",
                        dest="smpass",
                        default="",
                        help = "The authorized SMAPI password.")
    parser.add_argument("-v", "--verbose",
                        action='count')
    parser.add_argument("--version", action="version", version="%(prog)s {}".format(_version))
    args = parser.parse_args()
    r = smapi.send(args.function_name[0],
                   args.target,
                   args.smhost,
                   args.smport,
                   args.smuser,
                   args.smpass,
                   "")

if __name__ == "__main__":
    main()
