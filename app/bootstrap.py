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

def execfile(pyfile):
    f = open(pyfile);
    code = compile(f.read(), pyfile, 'exec');
    f.close();
    exec(code, dict(__file__=pyfile));

execfile(os.path.dirname(__file__)+"/../vendor/bin/activate_this.py");
