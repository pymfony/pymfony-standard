# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
"""
"""

from __future__ import absolute_import;

import time

from pymfony.component.console import Response
from pymfony.component.dependency import ContainerAware
from pymfony.component.console import Request

class DemoController(ContainerAware):
    def helloAction(self, request):
        assert isinstance(request, Request);

        clock = "";

        if request.getOption('time'):
            clock = "{0}: ".format(time.time());


        return Response("{0}Hello <info>{1}</info>!".format(
            clock,
            request.getArgument('name'),
        ));
