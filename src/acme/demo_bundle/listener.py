# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
"""
"""

from pymfony.component.dependency.interface import ContainerInterface
from pymfony.component.console_kernel.event import GetResponseEvent

class ControllerListener():
    def __init__(self, container):
        assert isinstance(container, ContainerInterface);

        self._container = container;

    def onKernelRequest(self, event):
        assert isinstance(event, GetResponseEvent);

        request = event.getRequest();
