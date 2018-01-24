#!/bin/python

import subprocess

#code = subprocess.call(['ls', '-l'])
#if code == 0:
#    print("command finished successfully")
#else:
#    print("failed with code : %i"  %code)
tru:
    (['ls', '-l'])output = subprocess.check_output(['ls', '-l'])
print(output)

