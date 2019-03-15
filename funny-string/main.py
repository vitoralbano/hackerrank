#!/user/bin/python
# -*- coding: utf-8 -*-


def funnyString(s):
    r = s[::-1]
    ascii_forward, ascii_reverse = [], []
    result_forward, result_reverse = [], []

    for index in range(0, len(s)):

        ascii_forward.append(ord(s[index]))
        ascii_reverse.append(ord(r[index]))
        if index > 0:
            result_forward.append(abs(ascii_forward[index] - ascii_forward[index - 1]))
            result_reverse.append(abs(ascii_reverse[index] - ascii_reverse[index - 1]))
            
            if not(result_forward[-1] is result_reverse[-1]):
                return 'Not Funny'
    return 'Funny'


print(funnyString('acxz'))
print(funnyString('bcxz'))