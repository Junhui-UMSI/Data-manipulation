#!/usr/bin/python -tt

# Lab 1 SI 601: Basic Python
#
# Based on an earlier design by Yuhang Wang and code from Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
#
# For each task below, fill in the code for the functions below.
# main() will call the functions with a few different inputs, check
# the results, and print 'OK' when each function's output is correct.
#
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. You need to fill in code
# for the function that returns the correct result as specified.

# Task A. String manipulation (function 'first_last_parts')
#   Remove any leading and trailing spaces from the input string
#   Convert the input string to lowercase
#   Replace any remaining spaces with underscore '_'
#   If the remaining string has 4 characters or less, just return that string.
#   If the remaining string consists entirely of digits (0..9), just return that string.
#   Otherwise, return a string consisting of the first two and last two characters of the remaining string
#   joined together.
#
# HINT - Look up these Python functions:
#     len()
#     str.strip()
#     str.lower()
#     str.replace()
#     str.isdigit()

def first_last_parts(s):
  s = s.strip(' ')
  s = s.lower()
  s = s.replace(' ','_')
  if len(s) < 5:
    return s
  elif s.isdigit():
    return s
  else:
    a = s[0:2]
    b = s[-2:]
    s = a + b
    return s

# Task B. Loops (function 'bananas')
#
# Given an integer count, return a string
# of the form '1 banana, 2 banana, ..., <count> banana', where <count> is the number
# passed in.  There are some special rules:
#   If the count is zero, return 'no bananas'
#   If the count is one, return 'a banana'
# However, if the count is 6 or more, then use the string
# ' and <num> more bananas' as the last item instead of the actual list of bananas,
# where <num> is the number of remaining bananas.  Note that in this case, there should
# be *no comma* between the last numbered banana and the "and <n> more bananas" string.
#
# Examples:
#     bananas(0)  returns 'no bananas'
#     bananas(3)  returns '1 banana, 2 banana, 3 banana'
#     bananas(5)  returns '1 banana, 2 banana, 3 banana, 4 banana, 5 banana'
#     bananas(10) returns '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 5 more bananas'  # note: no final comma
#     bananas(20) returns '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 15 more bananas'
#
# HINT - Look up these Python functions:
#   range()
#   str()

def bananas(count):
  if count == 0:
    return 'no bananas'
  elif count == 1:
    return 'a banana'
  elif count < 6:
    seq = []
    for i in range(1, count+1, 1):
      s = '%s banana' %(i)
      str = ', '
      seq.append(s)
    return str.join(seq)
  else:
    seq = []
    for i in range(1, 6, 1):
      s = '%s banana' %(i)
      str = ', '
      seq.append(s)
      str = str.join(seq)
    newcount = count-5
    str = str + ' and %s more bananas' %(newcount)
    return str

# Task C. Sets and string operations (function 'match_ends')
#
# Given a list of strings, and a starting and ending string to search for,
# return the count of UNIQUE strings in the list that
#      - have string length is 7 or more AND
#      - the string starts with the desired starting string AND
#      - ends with the desired ending string
#
# Example:
#   match_ends(['aerobiology', 'neurology', 'aerogy', 'anthropology', 'aerobiology', 'neurology', 'aerogy', 'anthropology'], 'a', 'ology')
# should return 2
#
# HINT - Look up these Python functions:
#   set()
#   str.startswith()
#   str.endswith()

def match_ends(words, starting, ending):
  words = set(words)
  count = 0
  for word in set(words):
    if len(word)>6:
      if word.startswith(starting):
        if word.endswith(ending):
          count = count +1
  return count



 

# Task D. Dictionaries and sorting (function 'unique_counts')
#
# Given a list of strings, return a list of tuples containing the counts of each of the
# UNIQUE strings. The returned results should be ordered by the counts
# in decreasing order. In case of ties of counts, break the tie by string value in increasing order.
#
# Examples:
#   unique_counts(['Microsoft', 'Intel', 'Intel', 'Intel', 'Apple', 'Apple'])
# should return [('Intel', 3), ('Apple', 2), ('Microsoft', 1)]
#
#   unique_counts(['Apple', 'Google', 'Microsoft', 'Apple', 'Facebook', 'Intel', 'Apple', 'Microsoft'])
# should return [('Apple', 3), ('Microsoft', 2), ('Facebook', 1), ('Google', 1), ('Intel', 1)])
#
# HINT - Look up these Python functions:
#   dict.items()
#   sorted()
#   dict.get() is also helpful
#   You will need to write a helper (key) function to use with sorted()
#   You can either write a named function or an anonymous lambda function

from operator import itemgetter, attrgetter
def unique_counts(words):
  wordset = set(words)
  worddict = dict.fromkeys(wordset)
  for key in worddict:
    a = words.count(key)
    worddict[key] = a
  result = sorted(worddict.items(), key = itemgetter(0))
  result = sorted(result, key= lambda x: x[1],reverse=True)
  return result









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
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print
  print 'Task A:  middle_part'
  """ If this is what you get, you are good. Each OK is worth one point.
 OK  got: 'fren' expected: 'fren'
 OK  got: '2_es' expected: '2_es'
 OK  got: '8675309' expected: '8675309'
 OK  got: 'z86' expected: 'z86'
 OK  got: '' expected: ''
  """
  test(first_last_parts(' Friedrichshafen   '), 'fren')
  test(first_last_parts('2 mercedes'), '2_es')
  test(first_last_parts('8675309'), '8675309')
  test(first_last_parts('z86'), 'z86')
  test(first_last_parts(''), '')


  print 'Task B: bananas'
  # Each line calls bananas, compares its result to the expected for that call.
  """ If this is what you get, you are good. Each OK is worth one point.
 OK  got: 'no bananas' expected: 'no bananas'
 OK  got: 'a banana' expected: 'a banana'
 OK  got: '1 banana, 2 banana, 3 banana, 4 banana, 5 banana' expected: '1 banana, 2 banana, 3 banana, 4 banana, 5 banana'
 OK  got: '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 5 more bananas' expected: '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 5 more bananas'
 OK  got: '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 94 more bananas' expected: '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 94 more bananas'
  """
  test(bananas(0), 'no bananas')
  test(bananas(1), 'a banana')
  test(bananas(5), '1 banana, 2 banana, 3 banana, 4 banana, 5 banana')
  test(bananas(10), '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 5 more bananas')
  test(bananas(99), '1 banana, 2 banana, 3 banana, 4 banana, 5 banana and 94 more bananas')


  print 'Task C: match_ends'
  """ If this is what you get, you are good. Each OK is worth one point.
 OK  got: 1 expected: 1
 OK  got: 2 expected: 2
 OK  got: 3 expected: 3
 OK  got: 5 expected: 5
 OK  got: 0 expected: 0
  """
  test(match_ends(['aerobiology', 'neurology', 'aerology', 'anthropology'], 'n', 'ology'), 1)
  test(match_ends(['aerobiology', 'neurology', 'Battlestar Galactica', 'aerogy', 'aerogy', 'aerobiology', 'anthropology'], 'a', ''), 2)
  test(match_ends(['aerobiology', 'neurology', 'aerogy', 'anthropology', 'aerobiology', 'neurology', 'aerology', 'anthropology'], 'a', 'ology'), 3)
  test(match_ends(['anthropology', 'anthropology', 'aerobiology', 'neurology', 'Battlestar', 'Galactica', 'aerology', 'anthropology', 'antitechnology'], '', 'y'), 5)
  test(match_ends([], '',''), 0)

  print 'Task D: unique_counts'
  """ If this is what you get, you are good. Each OK is worth one point.
 OK  got: [] expected: []
 OK  got: [('Intel', 1)] expected: [('Intel', 1)]
 OK  got: [('Intel', 3)] expected: [('Intel', 3)]
 OK  got: [('Apple', 3), ('Intel', 3), ('Microsoft', 1)] expected: [('Apple', 3), ('Intel', 3), ('Microsoft', 1)]
 OK  got: [('Apple', 3), ('Microsoft', 2), ('Facebook', 1), ('Google', 1), ('Intel', 1), ('Yahoo!', 1)] expected: [('Apple', 3), ('Microsoft', 2), ('Facebook', 1), ('Google', 1), ('Intel', 1), ('Yahoo!', 1)]
  """
  test(unique_counts([]), [])
  test(unique_counts(['Intel']), [('Intel', 1)])
  test(unique_counts(['Intel', 'Intel', 'Intel']), [('Intel', 3)])
  test(unique_counts(['Microsoft', 'Apple', 'Intel', 'Intel', 'Intel', 'Apple', 'Apple']), [('Apple', 3), ('Intel', 3), ('Microsoft', 1)])
  test(unique_counts(['Apple', 'Google', 'Microsoft', 'Apple', 'Facebook', 'Intel', 'Apple', 'Microsoft', 'Yahoo!']), [('Apple', 3), ('Microsoft', 2), ('Facebook', 1), ('Google', 1), ('Intel', 1), ('Yahoo!', 1)])
  
  
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
