# Substring Calculator
This is a solution for a [HackerHank](https://www.hackerhank.com) challenge that asked to found out the number of substrings in a given `string`. This approuch was developed as first solution, that means that it can be refactored and the use of recursivity could be a good idea. 

You can see this code running on https://repl.it/@vitoralbano/substring-calculator

# Challenge statement

Given a string, `s`, a substring is defined as a non-empty string that can be obtained by one of the following means:
* Remove zero or more characters from the left side of `s`.
* Remove zero or more characters from the right side of `s`.
* Remove zero or more characters from the left side of `s` and remove zero or more characters from the right side of `s`.

For example, let `s` = abcde. The substrings are:

| Line  | Substring |
| :---  | :---  |
| 1			|	abcde	|
| 2			|	abcd	|
| 3			|	bcde	|
| 4			|	abc		|
| 5			|	bcd		|
| 6			|	cde		|
| 7			|	ab		|
| 8			|	bc		|
| 9			|	cd		|
| 10		|	de		|
| 11		|	a		  |
| 12		|	b		  |
| 13		|	c		  |
| 14		|	d		  |
| 15		|	e		  |

# Function Description
The function must return the number of distinct substrings of string `s`. substringCalculator has the following parameter(s):
* **`s`:** the string to analyze

# Constraints
A single line with string `s`.
* String `s` consists of characters in the range ascii[a-z].
* 0 ≤ | `s` | ≤ 10

# Samples
## Sample Input 0
`'kincenvizh'`

## Sample Output 0
`53`

## Explanation 0
String `s = 'kincenvizh'` has the following distinct substrings:

| Line  | Substring |
| :---: | :---  |
| 1			|	kincenvizh	|
| 2			|	kincenviz	|
| 3			|	kincenvi	|
| 4			|	kincenv	|
| 5			|	kincen	|
| 6			|	kince	|
| 7			|	kinc	|
| 8			|	kin	|
| 9			|	ki	|
| 10		|	k	|
| 11		|	incenvizh	|
| 12		|	incenviz	|
| 13		|	incenvi	|
| 14		|	incenv	|
| 15		|	incen	|
| 16		|	ince	|
| 17		|	inc	|
| 18		|	in	|
| 19		|	i	|
| 20		|	ncenvizh	|
| 21		|	ncenviz	|
| 22		|	ncenvi	|
| 23		|	ncenv	|
| 24		|	ncen	|
| 25		|	nce	|
| 26		|	nc	|
| 27		|	n	|
| 28		|	cenvizh	|
| 29		|	cenviz	|
| 30		|	cenvi	|
| 31		|	cenv	|
| 32		|	cen	|
| 33		|	ce	|
| 34		|	c	|
| 35		|	envizh	|
| 36		|	enviz	|
| 37		|	envi	|
| 38		|	env	|
| 39		|	en	|
| 40		|	e	|
| 41		|	nvizh	|
| 42		|	nviz	|
| 43		|	nvi	|
| 44		|	nv	|
| 45		|	vizh	|
| 46		|	viz	|
| 47		|	vi	|
| 48		|	v	|
| 49		|	izh	|
| 50		|	iz	|
| 51		|	zh	|
| 52		|	z	|
| 53		|	h	|

## Sample Input 1
`'banana'`

## Sample Output 1
`15`

## Explanation 1
String `s = 'banana'` has the following distinct substrings:

| Line  | Substring |
| :---: | :---  |
| 1			|	banana	|
| 2			|	banan	|
| 3			|	bana	|
| 4			|	ban	|
| 5			|	ba	|
| 6			|	b	|
| 7			|	anana	|
| 8			|	anan	|
| 9			|	ana	|
| 10		|	an	|
| 11		|	a	|
| 12		|	nana	|
| 13		|	nan	|
| 14		|	na	|
| 15		|	n	|

## Sample Input 2
`'ghaqjdrmnegmrlrlfpjmnnngpwalzknsencuzwsnhfltwohdgbmvfuwtquosrnyerucntxxkfqehjqygcarxogvcfkljzbzutxphpyykapncjfclnhndzxghelyvzpylazhuutmcquusexzbhsfsmbnlvnlemzvfqbfzwquairhpylnbvyhiyamztlhfchhbwrqddmuzsprfdwuqqchcpeakkexackwwzihkfenwzwckynymgqydvjtovaoezkjjurylqcuonsujycziobnfnmuwnoxcdtahpituykvgpyyshvukrstcbmnsqtjseflwywnslmvnqrtnzkyaddkjamrezprqgoenzsdryygbkeahfiduozpwkrgmatszaxmwodsqiocvagbvxyqotpaujnqvqgjmfxnxhfbwqjpgodlxdrxpjpmzeabpgqrzpxomniknjkdiwtfgyvwvekrnoupwkcbtmpcfamzrghgrznuedkybmfwctdghcfawajlxfkzhdamuygjbcwnyglkjlfmpxfdtovkqbshhrfrnyjrgxgiozsuuncnwofkqzsypwgeikpfbhryhpszegdfajzvqlwwqlnvdtdiuckcvvosrdweohnmawqonjbxyjjhlccuteeshfrxxdhzgakwjqbymnaeudcmibsytyajsgdpfvrutcpglzxdevenevmkgalcrpknuvcrnkuboennhyzirfwvtozzijujsckbxqpocakzrbwgpqgjjmsrtwmvhwyraukbuxfvebeylfpipzwjdzlmgslbtwzataxgqpasrssnfwndldwkdutdqcmcpyanrbdsxrvcvpsywjambtbzlcrvzesuhvyvwwuwwdznigxjxknfajpknqutfvvqynkpvkzgypasevrpxofbymdzcitoqolwqegocuyqsexhumzmckzuuwkamolbltlifongpvkcnrnnuplftqbxpdnegdqlymftqyrxcnzmu'`

## Sample Output 2
As this `string` generate a great number of substrings, it won't be listed here, only the method return:

`499011`