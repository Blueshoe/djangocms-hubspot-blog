#!/bin/sh

twine upload dist/*
rm -rf dist/*
#rm -rf build/*