#!/user/bin/python
# -*- coding: utf-8 -*-

import re


def pangrams(s):
    alphabet = r'abcdefghijklmnopqrstuvwxyz'
    unique_chars = ''.join(sorted(list(set(s.lower()))))
    
    if re.search(alphabet, unique_chars):
        return 'pangram'
    else:
        return 'not pangram'


print(pangrams('The quick brown fox jumps over the lazy dog'))
