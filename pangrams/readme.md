# Pangrams
Solution proposal for [Pangrams](https://www.hackerrank.com/challenges/pangrams/problem) challenge from [Hacker Hank](https://www.hackerrank.com/), and, as habitual, the Repl is available at https://repl.it/@vitoralbano/funny-string.

# Function description
It should return the string `pangram` if the input string is a pangram. Otherwise, it should return `not pangram`.

`pangrams` has the following parameter(s):
* `s`: a string to test

# Input format
Input consists of a string `s`.

# Constraints
* 0 < |`s`| <= 10<sup>3</sup>
* Each character of `s`, `s[i]` Exists in  `{a-z, A-Z, space}`

# Output Format
Output a line containing pangram if `s` is a `pangram`, otherwise output `not pangram`. 

# Samples
## Sample input 0
`'We promptly judged antique ivory buckles for the next prize'`

## Sample output 0
`'pangram'`

## Sample explanation 0
All of the letters of the alphabet are present in the string.

## Sample input 1
`'We promptly judged antique ivory buckles for the prize'`

## Sample output 1
`'not pangram'`

## Sample explanation 1
The string lacks an x.
