#!/usr/bin/bash

# Do "source develop.bash" to get a working test environment.

SRC=~/test_framework
DEST=~/tests-virtualenv

rm -rf $DEST
mkdir $DEST
virtualenv $DEST/test_framework
source $DEST/test_framework/bin/activate
cd $SRC
python setup.py develop
