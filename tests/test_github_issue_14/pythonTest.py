#!/usr/bin/env python
import sys
import os
import local_script

# Ensure that the __real_file__ path ends in .snakemake
dname = os.path.dirname(__real_file__)
print(dname)
if not dname.endswith(os.path.join(".snakemake", "scripts")):
    sys.exit("We're not being written in the output directory!\n")

with open(snakemake.output[0], "w") as of:
    of.write("local_script.contents {}\n".format(local_script.contents))
