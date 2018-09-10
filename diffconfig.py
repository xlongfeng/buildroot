#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

if __name__ == '__main__':

    import sys

    with open("configs/imx6-skynet_defconfig") as f:
        file_content = "[Default]\n" + f.read()
    formatConfig = configparser.ConfigParser()
    formatConfig.read_string(file_content)

    with open("configs/imx6-skynet_raw_defconfig") as f:
        file_content = "[Default]\n" + f.read()
    rawConfig = configparser.ConfigParser()
    rawConfig.read_string(file_content)

    print("")
    print("== Only in imx6-skynet_defconfig ==")
    print("")
    for key in formatConfig["Default"]:
        if key not in rawConfig["Default"]:
            print(key.upper())

    print("")
    print("== Only in imx6-skynet_raw_defconfig ==")
    print("")
    for key in rawConfig["Default"]:
        if key not in formatConfig["Default"]:
            print(key.upper())

    print("")
