# Substring Calculator
Given a string, `s`, a substring is defined as a non-empty string that can be obtained by one of the following means:
* Remove zero or more characters from the left side of s.
* Remove zero or more characters from the right side of s.
* Remove zero or more characters from the left side of s and remove zero or more characters from the right side of s.

For example, let s = abcde. The substrings are:
1. abcde
2. abcd
3. bcde
4. abc
5. bcd
6. cde
7. ab
8. bc
9. cd
10. de
11. a
12. b
13. c
14. d
15. e

## Function Description
The function must return the number of distinct substrings of string `s`. substringCalculator has the following parameter(s):
s: the string to analyze

## Constraints
* String s consists of characters in the range ascii[a-z].
* 0 ≤ |s| ≤ 10
