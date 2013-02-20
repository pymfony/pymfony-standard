#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from pymfony.component.kernel.bundle import Bundle
from pymfony.component.console.input import InputDefinition
from pymfony.component.console_kernel.routing import Route
from pymfony.component.console.input import InputArgument
from pymfony.component.console.input import InputOption
from pymfony.component.console_kernel.routing import RouteCollection

"""
"""

class AcmeDemoBundle(Bundle):

    def boot(self):

        route = Route('hello', InputDefinition([
            InputArgument("name", InputArgument.OPTIONAL, "Set your name", "Fabien"),
            InputOption("--time", "-t", InputOption.VALUE_NONE, "Show the current timestamp time is it")
        ]));
        route.setDefault('_controller', "AcmeDemoBundle:Demo:hello");
        route.setDescription("Say hello");

        routeCollection = self._container.get('console.route_collection');
        assert isinstance(routeCollection, RouteCollection);
        routeCollection.add('hello', route);