#!/bin/sh
#
# Return the part of PYTHONPATH with all source directories.
#

__DIR__="$(realpath "$(dirname "$0")")";

# The absolute path to the application library (default: the directory of this file)
LIB_DIR="$__DIR__/..";

PYTHONPATH="$LIB_DIR/app:$LIB_DIR/src";
VENDOR_DIR="$LIB_DIR/vendor";

# install the Pymfony framework
VENDOR_NAME="alquerci";
PROJECT_NAME="pymfony";
PROJECT_VENSION="v2.2.0-BETA2-r0";
PROJECT_REPOSITORY="http://github.com/alquerci/pymfony.git";
PROJECT_SRC="src"; # directory on relative path to the project must not contains ..

if [ ! -d "$VENDOR_DIR/$VENDOR_NAME/$PROJECT_NAME/$PROJECT_SRC_DIR" ];
then
    mkdir -p "$VENDOR_DIR/$VENDOR_NAME";
    git clone -q "$PROJECT_REPOSITORY" "$VENDOR_DIR/$VENDOR_NAME/$PROJECT_NAME";
    cd "$VENDOR_DIR/$VENDOR_NAME/$PROJECT_NAME";
    git checkout -q "$PROJECT_VENSION";
    cd "$LIB_DIR";
fi;
PYTHONPATH="$VENDOR_DIR/$VENDOR_NAME/$PROJECT_NAME/$PROJECT_SRC:$PYTHONPATH";


echo -n "$PYTHONPATH";

exit 0;
