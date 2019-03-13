#!/user/bin/python
# -*- coding: utf-8 -*-

import re

def pangrams(s):
    alphabet = r'abcdefghijklmnopqrstuvwxyz'
    # unique_chars = ''.join(set(s.lower()))
    unique_chars = ''.join(sorted(list(set(s.lower()))))
    print(unique_chars)
    if re.search(alphabet, unique_chars):
        return 'pangram'
    else:
        return 'not pangram'


print(pangrams('The quick brown fox jumps over the lazy dog'))