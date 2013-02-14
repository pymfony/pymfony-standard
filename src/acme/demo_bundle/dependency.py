# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
from pymfony.component.console.input import InputDefinition
from pymfony.component.console.input import InputArgument
from pymfony.component.console.input import InputOption
"""
"""

from os import path

from pymfony.component.kernel.dependency import Extension
from pymfony.component.dependency.loader import JsonFileLoader
from pymfony.component.config import FileLocator

class AcmeDemoExtension(Extension):
    def load(self, configs, container):
        loader = JsonFileLoader(container, FileLocator(path.dirname(__file__)+'/Resources/config'))
        loader.load("services.json");

        # command register TODO do a better way

        container.setParameter('console.default_command', 'hello');

        if container.hasParameter('console.commands'):
            commands = container.getParameter('console.commands');
        else:
            commands = dict();

        commands['hello'] = {
            "_description": "Say hello",
            "_controller": "@AcmeDemoBundle:Demo:hello",
            "_definition": InputDefinition([
                InputArgument("name", InputArgument.OPTIONAL, "set your name", "fabien"),
                InputOption("--time", "-t", InputOption.VALUE_NONE, "show the current timestamp time is it")
            ])
        };

        container.setParameter('console.commands', commands);

    def getAlias(self):
        return "acme_demo";
