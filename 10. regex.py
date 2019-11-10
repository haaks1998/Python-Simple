# regular expression can be used in any programming language
# regex can be used to compare specific pattern of string e.g finding email through its format
# we can create regex for any pattern of string we can think of
# regex are normally used with raw strings i.e strings in which escape sequence are also treated as characters of string
# raw strings can be created by placing r before string e.g    print(r"\nTab")
# each regex MetaStrings compare 1 character eg for phone number we have to write regex as \d\d\d-\d\d\d-\d\d\d\d
# to make regex to be able to compare multiple characters, we use quantifiers

# regex MetaStrings and their comparison.
#   	.       any character except new line
#       \d      digits (0-9)
#       \D      not a digit
#       \w      word characters (a-z, A-Z, 0-9)
#       \W      not a word
#       \s      whitespace (space, tab, new line)
#       \S      not a whitespace
#       \b      word boundry
#       \B      not word boundry
#        ^      start of string
#        $      end of string
#       []      characters set e.g [.+] will search for either . or +
#       [^ ]    characters not in [] brackets
#        |      either or
#       ()      group e.g if we want to compair Mr or Mrs with name we can create regex as:  M(r|rs)\.?\s[A-Z]\w*

# regex Quantifiers
#       *       0 or more
#       +       1 or more
#       ?       0 or 1
#      {3}      exactly 3
#     {3,4}     3 to 4

# regex functions
#   regex.finditer(`string`)       to find the words matching regex with some extra info
#   regex.findall(`string`)        to find the words matching regex without extra information
#   regex.match(`string`)          to find out that if the first word of string matches the regex
#   regex.search(`string`)         to search words matching regex in string

# regex flags
# regex flags are the opyional 2nd parameter in re.compile(regex,flag)
#   re.compile(regex, re.I)        Ignore the (upper/lower)case of string        re.I or re.IGNORECASE 
#   and many more flags
import re

string_to_search = """If you do much work on computers, eventually you find that there’s some task you’d like to automate. 
For example, you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. 
Perhaps you’d like to write a small custom database, or a specialized GUI application, or a simple game.
If you’re a professional software developer, you may have to work with several libraries  (C/C++/Java) but find the usual write/compile/test/re-compile cycle is too slow. 
Perhaps you’re writing a test suite for such a library and find writing the testing code a tedious task. Or maybe you’ve written a program that could use an extension language, and you don’t want to design and implement a whole new language for your application.
Python is just the language for you.
You could write a Unix shell script or Windows batch files for some of these tasks, but shell scripts are best at moving around files and changing text data, not well-suited for GUI applications or games. 
You could write a C/C++/Java program, but it can take a lot of development time to get even a first-draft program. Python is simpler to use, available on Windows, Mac OS X, and Unix operating systems, and will help you get the job done more quickly.
This text is from 2019 official python version 3.0 documention
website: www.python.org
phone: 123-456-7890
       123.456.7890
email: abcd@xyz.com
"""                                             # string in which we have to find the pattern

print(string_to_search)

# First start by searching simple word in the string through regex
#..................................................... finditer() ...........................................
# finditer() will find each iteration of the pattern with some extra info
word = re.compile(r'Python')
results = word.finditer(string_to_search)            
for res in results:
    print(res)

# Characters used in regex expression e.g  .  *  ^  $  +  ?  []  {}  ()  \  |    These characters need to be escaped in compile() if we want to find
# these specific character. Otherwise they will perform their regex function 
print("\nFinding all . in string using \\. regex")
word = re.compile(r"\.")
results = word.finditer(string_to_search)
for res in results:
    print(res)

# To find all the digits in the string, we can write regex as follow
print("\nFinding numbers in string using \\d regex")
word = re.compile(r"\d")
results = word.finditer(string_to_search)
for res in results:
    print(res)

# To find whether the specific pattern lie at the boundry of word or not e.g `Py` is at boundry of Python but `thon` is not
print("\nFinding that whether the specific pattern lie at the boundry of word or not")
word = re.compile(r"\bPy")
results = word.finditer(string_to_search)
for res in results:
    print(res)

# To find whether the specific word lie at the start of string or not e.g `If` lie at the start of string 
print("\nFinding that whether the specific word lie at the start of string or not")
word = re.compile(r"^If")
results = word.finditer(string_to_search)
for res in results:
    print(res)

# To find numbers in the string. Usefull for parsing numbers. Similarly we can create regex for email, websites etc
print("\nFinding phone numbers in the string")
word = re.compile(r"\d\d\d\D\d\d\d\D\d\d\d\d")        # It is regex for phone numbers where \d for digit and \D for any not digit
results = word.finditer(string_to_search)             # The quantifier version of regex is :  \d{3}\D\d{3}\D\d{4}
for res in results:
    print(res)

# If we want to find every 3 digit word ending with at, but not bat. we can do this as
at_strings= "cat bat rat fat "
print(at_strings)
print("\nStrings ending with at except bat")
word = re.compile(r"[^b]at")                        # It means that first character can be any thing but not b, last two will be at
results = word.finditer(at_strings)
for res in results:
    print(res)

# To find email in the string. Usefull for parsing numbers.
print("\nFinding email in the string")
word = re.compile(r"\w*@\w*\.\w*")    
results = word.finditer(string_to_search)             
for res in results:
    print(res)

#................................................ Group function .........................................
print("\nFinding websites and different part of url")
websites = "www.google.com  http://www.youtube.com  http://facebook.com  http://www.instagram.com  www.mit_courses.edu"
word = re.compile(r"(http://)?(www.)?(\w+)(\.\w+)")    
results = word.finditer(websites)             
for res in results:
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
    print("\n")

# if we want to create a new string with only certain groups, we can use sub function
print("\nStoring only domain names of websites (subbed urls)")
websites = "www.google.com  http://www.youtube.com  http://facebook.com  http://www.instagram.com  www.mit_courses.edu"
word = re.compile(r"(http://)?(www.)?(\w+)(\.\w+)")    
web_domains = word.sub(r'\3',websites)                  # where r'\3' means 3rd group in regex i.e domain name         
print(web_domains)

input("\nPress any key to exit")
