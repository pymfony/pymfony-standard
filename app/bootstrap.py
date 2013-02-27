# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
"""
"""

import os;
import sys;

__DIR__ = os.path.dirname(os.path.abspath(__file__));

def execfile(pyfile):
    f = open(pyfile);
    code = compile(f.read(), pyfile, 'exec');
    f.close();
    exec(code, dict(__file__=pyfile));

if sys.platform == 'win32': # @see: virtualenv.is_win
    execfile(__DIR__ + "/../vendor/Scripts/activate_this.py");
else:
    execfile(__DIR__ + "/../vendor/bin/activate_this.py");
