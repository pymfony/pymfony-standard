# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
"""
"""

from os.path import dirname;

from pymfony.component.kernel.dependency import Extension
from pymfony.component.dependency.loader import JsonFileLoader
from pymfony.component.config import FileLocator

class AcmeDemoExtension(Extension):
    def load(self, configs, container):
        loader = JsonFileLoader(container, FileLocator(dirname(__file__)+'/Resources/config'))
        loader.load("services.json");


    def getAlias(self):
        return "acme_demo";
