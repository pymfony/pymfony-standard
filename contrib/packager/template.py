#! /usr/bin/env python

sources = """
@SOURCES@"""

import os;
import sys;
import base64;
import zlib;
import tempfile;
import shutil;


def unpack(sources):
    temp_dir = tempfile.mkdtemp('-scratchdir', 'unpacker-');
    for package, content in sources.items():
        filepath = package.split(".");
        dirpath = os.sep.join(filepath[:-2]);
        packagedir = os.path.join(temp_dir, dirpath);
        if not os.path.isdir(packagedir):
            os.makedirs(packagedir);
        mod = open(os.path.join(packagedir, ".".join(filepath[-2:])), 'w');
        try:
            mod.write(content);
        finally:
            mod.close();
    return temp_dir;


if __name__ == "__main__":
    if sys.version_info < (3, 0):
        import cPickle as pickle;
        exec("def do_exec(co, loc): exec co in loc\n");
        sources = pickle.loads(zlib.decompress(base64.decodestring(sources)));
    else:
        exec("def do_exec(co, loc): exec(co, loc)\n");
        import _pickle as pickle;
        sources = sources.encode("ascii");
        sources = pickle.loads(zlib.decompress(base64.decodebytes(sources)));

    try:
        temp_dir = unpack(sources);
        sys.path.insert(0, temp_dir);

        entry = """@ENTRY@""";
        do_exec(entry, locals());
    finally:
        shutil.rmtree(temp_dir);
