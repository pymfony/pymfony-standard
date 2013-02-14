# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
"""
"""

from os import path;

from pymfony.component.kernel import Kernel;
from pymfony.bundle.framework import FrameworkBundle;
from acme.demo_bundle import AcmeDemoBundle;

class AppKernel(Kernel):
    def registerBundles(self):
        bundles = [
            FrameworkBundle(),
        ];

        if self.getEnvironment() in ['dev', 'test']:
            bundles.append(AcmeDemoBundle());

        return bundles;

    def registerContainerConfiguration(self, loader):
        loader.load("{0}/Resources/config/config_{1}.json".format(
            path.dirname(__file__),
            self.getEnvironment()
        ));
