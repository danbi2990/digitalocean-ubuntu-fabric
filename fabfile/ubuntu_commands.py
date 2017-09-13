#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import run, cd
from fabric.operations import put

APT_GET_PACKAGES = [
    # "build-essential",
    # "git",
    # "vim",
    # "python-dev",
    # "python-virtualenv",
    # "python-pip",
    "nginx",
    "git",
    "python3.6",
]
APT_GET_REPOSITORY = [
    "ppa:jonathonf/python-3.6",
]
GET_PIP = "get-pip.py"


def add_repo():
    "Add repository"
    run("sudo add-apt-repository " + " ".join(APT_GET_REPOSITORY))
    run("sudo apt-get update")


def setup():
    "Install default packages for django"
    run("sudo apt-get install " + " ".join(APT_GET_PACKAGES))


def install_pip():
    "Install PIP"
    # print(GET_PIP)
    # with open(GET_PIP, encoding='utf-8') as pip:
    #     for line in pip:
    #         print(line)
    put(GET_PIP, "~/")
    run("sudo python3.6 ~/get-pip.py")
    run("sudo rm -f ~/get-pip.py")
    # run("")


def setup_webserver():
    "Install default packages for django and NGINX"
    APT_GET_PACKAGES.append("nginx")
    setup()


def create_www():
    "Configure permissions on www"
    run("mkdir -p /www/")
    run("chown -R root:www-data /www/")
    run("chmod 775 -R /www/")
    run("chmod g+s -R /www/")


def create_package(name):
    "Create virtualenv"
    create_www()
    package_name = "/www/%s-package" % str(name)
    run("virtualenv " + package_name)
    with cd(package_name):
        run("mkdir -p logs")
