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

class DemoCommand(ContainerAware):
    def helloAction(self, name, _o_time):

        clock = "";

        if _o_time:
            clock = "{0}: ".format(time.time());

        return Response("{0}Hello <info>{1}</info>!".format(
            clock,
            name,
        ));
