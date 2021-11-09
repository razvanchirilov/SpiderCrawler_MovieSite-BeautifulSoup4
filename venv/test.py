import string

#!/bin/python3

import math
import os
import random
import re
import sys


import string
#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def missingCharacters(s):
    # Write your code here
    letters = string.ascii_lowercase
    digits = string.digits
    correct = ''
    for ch in letters:
        if ch not in s:
            correct = ch + correct
    for ch in digits:
        if ch not in s:
            correct = ch + correct
    print(correct)


missingCharacters('mamaluistefancelmare')
