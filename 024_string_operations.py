# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=760

from lib.helpers import check_that_these_are_equal

# We're going to show you some more things you can do with strings.

# == Length ==

# Strings contain characters. We can find the number of characters a string has.
# This is called the length.

# You can get the length using a function pre-loaded into Python called `len`

# Here's an example:

length = len("Hello!")
print(f"The string is {length} characters long")

# @TASK: Try it out yourself by changing the string "Hello!" above, and then
# running this code with:
#
#   python 024_string_operations.py
#
# You'll see some other test output at the bottom. You can ignore this until
# later in the exercise.

# == Replace ==

# Let's say you wanted to turn this:

"Hello, YOUR_NAME!"

# Into this:

"Hello, Kay!"

# For this, you could use the `replace` function:

old_string = "Hello, YOUR_NAME!"
new_string = old_string.replace("YOUR_NAME", "Kay")

# Uncomment this next line to see the result
# print(new_string)

# You'll notice here that the function is coming in a different place. Let's
# compare `len` and `replace`:

my_string = "hello"

len(my_string)              # <-- Independent Function
my_string.replace("h", "w") # <-- Method Function

# Why the difference? It's a little complicated.
#
# What you need to know for now is that some functions come in one style like
# `len`, and some come in the other style like `replace`. The latter are called
# 'methods'.

# == Upper and Lowercase ==

# When you're doing the Makers assessment, you're quite likely to be asked to do
# something you've not done before. This is very normal.

# In an engineering job, and increasingly in any job, you have to get
# comfortable with looking up how to do things.

# We'll practice this here.

# @TASK Complete these exercises:

# == Exercise One ==

print("")
print("Function: uppercase")

# Search for 'python make string uppercase'

def make_uppercase(string):
  # Return the string in uppercase
  pass

check_that_these_are_equal(
  make_uppercase("hello"), "HELLO")

check_that_these_are_equal(
  make_uppercase("World"), "WORLD")

# == Exercise Two ==

print("")
print("Function: lowercase")

# Search for 'python make string lowercase'

def make_lowercase(string):
  # Return the string in lowercase
  pass

check_that_these_are_equal(
  make_lowercase("HELLO"), "hello")

check_that_these_are_equal(
  make_lowercase("World"), "world")

# == Exercise Three ==

print("")
print("Function: strip_whitespace")

# Search for 'python remove whitespace from string'

def strip_whitespace(string):
  # Return the string with any whitespace removed from the start and end
  pass

check_that_these_are_equal(
  strip_whitespace("hello "), "hello")

check_that_these_are_equal(
  strip_whitespace(" hello world "), "hello world")

# When you're done, move on to 025_string_concatenation.py
