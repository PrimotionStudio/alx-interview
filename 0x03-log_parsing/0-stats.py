#!/usr/bin/python3
import sys
import re

for line in sys.stdin:
    match = re.match(r"^[1-254]{1}\d?\d?\.[0-254]{1}\d?\d?\.[0-254]{1}\d?\d? - ", line)
    if match:
        print("Yay Match")