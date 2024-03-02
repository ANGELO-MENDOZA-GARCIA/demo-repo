#!/usr/bin/env /usr/bin/python3
from difflib import SequenceMatcher
import subprocess
import re
import os

def run_cmd(cmd, get_output=True, timeout=35, stop_on_error=True):
    "Run cmd logging input and output"
    output = ""
    try:
        if get_output:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
            output, err = p.communicate(timeout=timeout)
            rc = p.returncode
        else:
            subprocess.check_call(cmd, stderr=subprocess.STDOUT, shell=True, timeout=timeout)
    except subprocess.CalledProcessError as e:
        if stop_on_error:
            msg = 'Failed sudo_cmd: %s' % (e.returncode, str(e))
    except Exception as e:
        if stop_on_error:
            msg = 'Failed sudo_cmd: %s' % str(e)
    return output


#proc = lamba x: subprocess.Popen(x, stdout=subprocess:PIPE, stderr=/dev/null)

#Valid chars . a-z 0-9
def check(test_str):
    # pattern = r'[^]'
    # if re.search(pattern, test_str):
    #     print ('Pero se supone que se permiten todos los comandos, ¿no?\n' % (test_str, ))
    #     print('Char not permitted')

    # else:
        try:
            output = run_cmd(test_str, get_output=True, stop_on_error=True)
            print(output)
        except OSError:
            print('Unknown error.')

while True:
    try:
        s = input('Jail sin restricción >> ')
    except EOFError:
        break

    try:
        #cmd = re.split(r'\s+', s)
        cmd = s
        check(cmd)
    except OSError:
        print('Unknown error.')
