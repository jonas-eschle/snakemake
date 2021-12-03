#!/usr/bin/env python
import sys
import os
import local_script
from pathlib import Path

# Ensure that the __real_file__ path ends in .snakemake
dname = Path(__real_file__).parent
print(dname)
if dname.parts[-2:] != (".snakemake", "scripts"):
    sys.exit("We're not being written in the output directory!\n")

with open(snakemake.output[0], "w") as of:
    of.write("local_script.contents {}\n".format(local_script.contents))
