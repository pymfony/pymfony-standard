Pymfony Standard Edition
========================

[![Build Status][0]][1]

Welcome to the Pymfony Standard Edition - a fully-functional Pymfony
application that you can use as the skeleton for your new applications.

This document contains information on how to download, install, and start
using Pymfony.

1) Installing the Standard Edition
----------------------------------

When it comes to installing the Pymfony Standard Edition, you have the
following options.

### Use Virtualenv (*recommended*)

As Pymfony uses [Virtualenv][2] to manage its dependencies, the recommended way
to create a new project is to use it.

If you don't have Virtualenv yet, download it following the instructions on
http://www.virtualenv.org/ or just run the following command:

    curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py

Then, use following commands to generate a new Pymfony application:

    python virtualenv.py path/to/install/vendor
    path/to/install/vendor/bin/pip install pymfony.framework-standard-edition
    path/to/install/vendor/bin/pip install -r requirements.txt

Virtualenv will install Pymfony and all its dependencies under the
`path/to/install` directory.

### Download an Archive File

To quickly test Pymfony, you can also download an [archive][3] of the Standard
Edition and unpack it somewhere.

Download virtualenv (see above) and run the following commands:

    python virtualenv.py vendor
    vendor/bin/pip install . -r requirements.txt

2) Running the Demo Application
-------------------------------

Congratulations! You're now ready to use Pymfony.

To see a real-live Pymfony in action, type the following command:

    app/console hello Fabien


3) Getting started with Pymfony
-------------------------------

This distribution is meant to be the starting point for your Pymfony
applications, but it also contains some sample code that you can learn from
and play with.

A default bundle, `AcmeDemoBundle`, shows you Pymfony in action. After
playing with it, you can remove it by following these steps:

  * delete the `src/acme` directory;

  * remove the AcmeBundle from the registered bundles in `app/app_kernel.py`;


What's inside?
--------------

The Pymfony Standard Edition is configured with the following defaults:

It comes pre-configured with the following bundles:

  * **FrameworkBundle** - The core Pymfony framework bundle

  * **AcmeDemoBundle** (in dev/test env) - A demo bundle with some example
    code



[0]: https://travis-ci.org/alquerci/pymfony-standard.png?branch=master
[1]: https://travis-ci.org/alquerci/pymfony-standard
[2]: http://www.virtualenv.org
[3]: https://github.com/alquerci/pymfony-standard/archive/master.zip
