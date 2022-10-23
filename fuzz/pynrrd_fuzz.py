#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    import nrrd

@atheris.instrument_func
def TestOneInput(data):
   nrrd.read(data)
    


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()