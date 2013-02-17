# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from distutils.core import setup;

import os;

"""
"""

realpathfile = os.path.realpath(os.path.dirname(__file__));
os.chdir(realpathfile);

f = open("README.md");
long_description = "\n"+f.read();
f.close();

setup(
    name="pymfony.framework-standard-edition",
    version="0.1.0",
    package_dir={'': 'src'},
    packages=['acme', 'acme.demo_bundle'],
    package_data={'': ["Resources/*/*.*"]},
    author="Alexandre Quercia",
    author_email="alquerci@email.com",
    url="http://github.com/alquerci/pymfony-standard",
    description='The "Pymfony Standard Edition" distribution',
    long_description=long_description,
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
);
