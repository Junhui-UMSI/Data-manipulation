# -*- coding: utf-8 -*-      
#!/usr/bin/python -tt

# Lab 2 SI 601: Regular expressions
#
# Written by Kevyn Collins-Thompson.
# Some test framework code used courtesy of Dr. Yuhang Wang.
#
# As with Lab 1, you fill in the missing code for the functions below, and
# main() is already set up to check the output of your functions with a few
# different inputs, printing 'OK' when each function is correct.
# Note that the 'return' in each function will need to be replaced to return
# the (correct) value for the specified problem.

import re

# A. leading_and_trailing
# Compile a regular expression to match strings that satisfy ALL of the following conditions
#    - the first character is NOT alphabetic, i.e. a through z (case-insensitive)
#    - all remaining characters are "word characters", (i.e. letters, numbers, regardless of case, or underscore (_)
#    - the word must end either in the string 'er', or end in 'est' followed by one or more exclamation marks (case-insensitive)
#
# This function should return True if there was a match, and False otherwise.
#
# For example:
# leading_and_trailing('Awesomer') should return False
# leading_and_trailing('5oolest!') should return True
# leading_and_trailing('5oolest and best') should return False
# leading_and_trailing('@_eR') should return True
# leading_and_trailing('@taggest!!!!!!') should return True
# leading_and_trailing('Est') should return False
# leading_and_trailing('#$@eST!') should return False

def leading_and_trailing(s):
    if re.match('^[^a-zA-Z]\w+(er|est!+)', s, re.IGNORECASE):
        return True
    else:
        return False

# B.  parse_counted_words
# Use regular expressions to find strings of the form:
#  <count> <longword>    e.g. 101 Dalmations
# More specifically, the match much follow these conditions
#   - first word (word1) is a count consisting of a natural number
#     (series of one or more digits, with leading and trailing whitespace)
#   - followed immediately by a second, long word2 starting with an optional non-alphabetic character followed by *at least* 7 alphabetic letters
#
#  Your function should return the *last* correctly matching (word1, word2) pair found in the string, if one exists
#  or None if no such strings were found
# HINT:  \b matches the beginning or end of a word
# HINT:  you can use findall to get multiple matches in a string
#
# For example:
# parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') should return ('13', 'pineapples')
# parse_counted_words('101 dalmations!') should return ('101', 'dalmations')
# parse_counted_words('snow white and the 7 #littledwarves') should return ('7', '#littledwarves')
# parse_counted_words('goldilocks and the 3 little pigs') should return None, because 'little' has less
#    than 7 characters
# parse_counted_words('678 1234567 890')  should return None, because the word following the count does
#    not consist of alphabetic characters
def parse_counted_words(s):
    match = re.findall(r'\d+\s[^a-zA-Z]?[a-zA-Z]{7,}', s)

    if (len(match)>0):
        resultpair = match.pop()
        word1 = resultpair.split()[0]
        word2 = resultpair.split()[1]

        return word1,word2
    else:
        return None

# C. find_tag
# Find the first pair of correctly-matched tags that encloses the given text
# string, and return that tagname.  In case of multiple (nested) tags, return
# the outermost tagname.  For example:
# If the string_to_find is "foo", and the input string is
#  <title>some string using foo as an example</title>
# then your function should return 'title'
# The tags must be correctly matched, i.e. this is not a correct match:
#  <title>some string containing foo </titlexyz>
# If there are nested tags like this:
#  <title>some string using <b>foo</b> as an example</title>
# then return the outermost tag 'title'
#
# HINT:  the \1 metacommand can be used to require a match with the results from
#  the first matching group in the regexp
#
# HINT: non-greedy matching wildcards are useful here.

def find_tag(string_to_find, s):
  searchresult = re.search(r'<(.*?)>.*' + string_to_find + r'.*</\1>', s)
  if searchresult:
    tagname = searchresult.group(1)
    return tagname
  else:
    return None

# D. mission_report
# Use regular expressions along with findall to extract all pairs of correctly formatted
# Mission number and status pairs.  A mission's status is either 'failed' or the number of targets found (using digits).
# Sometimes a mission will be called a 'raid'.
# For example:
# test(mission_report('Mission 1 accomplished. Target found: 1.'), [(1,1)])
#  test(mission_report('Note: mission 20 accomplished. Targets found: 500. Mission 21 failed.'), [(20,500), (21, 'failed')])
#  test(mission_report("Yes, mission 3 failed. Mission 48 accomplished. targets found: 23. mission 96 accomplished, targets found: 0"), [(3,'failed'), (48, 23), (96, 0)])
#  test(mission_report("Shopping list: 4 pineapples and 12 eggs."), None)
#
# HINT:
# Use the re.IGNORECASE option for case insensitive matching
# http://docs.python.org/2/library/re.html#re.I
# You may use a couple of regular expressions in this function, or you can use only one.
# Remember that each part of a set of alternatives can contain a regular expression.
# You may find non-capturing groups and/or non-greedy wildcards handy.
# You can use the int() function to convert a string to integer
def mission_report(s):
  searchresult = re.findall(r'mission\s[0-9]+\saccomplished.*?[0-9]+|mission\s[0-9]+\sfailed\b', s, re.IGNORECASE)
  pairresult = []
  if searchresult:
    for item in searchresult:
      if 'failed' in item:
        pairresult.append((int(item.split()[1]),'failed'))
      else:
        pairresult.append((int(item.split()[1]),int(item.split()[-1])))
    return pairresult
  else:
    return None


#######################################################################
# DO NOT MODIFY ANY CODE BELOW
#######################################################################

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s, expected: %s' % (prefix, repr(got), repr(expected))


def main():
  print 'Test results:'

  print 'leading_and_trailing'
  test(leading_and_trailing('Awesomer') , False)
  test(leading_and_trailing('5oolest!') , True)
  test(leading_and_trailing('5oolest and best') , False)
  test(leading_and_trailing('@_eR'), True)
  test(leading_and_trailing('@taggest!!!!!!'), True)
  test(leading_and_trailing('Est'), False)
  test(leading_and_trailing('#$%eST!'), False)

  print 'parse_counted_words'
  test(parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') , ('13', 'pineapples'))
  test(parse_counted_words('101 dalmations!') , ('101', 'dalmations'))
  test(parse_counted_words('snow white and the 7 #littledwarves, with 1 left behind.') , ('7', '#littledwarves'))
  test(parse_counted_words('goldilocks and the 3 little pigs') , None)
  test(parse_counted_words('678 1234567 890') , None)
    
  print 'find_tag'
  test(find_tag('foo', '<image>foobar</image>'), 'image')
  test(find_tag('foo', '<h3>foo</h4>'), None)
  test(find_tag('meta', '<html>meta data<body>some text</body></html>'), 'html')
  test(find_tag('introduction', '<title><b>An introduction</b>to using the title tag</title>'), 'title')

  print 'mission_report'
  test(mission_report('Mission 1 accomplished. Target found: 1.'), [(1,1)])
  test(mission_report('Note: mission 20 accomplished. Targets found: 500. Mission 21 failed.'), [(20,500), (21, 'failed')])
  test(mission_report("Yes, mission 3 failed. Mission 48 accomplished. targets found: 23. mission 96 accomplished, targets found: 0"), [(3,'failed'), (48, 23), (96, 0)])
  test(mission_report("Shopping list: 4 pineapples and 12 eggs."), None)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
