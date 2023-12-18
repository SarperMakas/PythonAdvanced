"""
Regular expression
MetaCharacters => . ^ $ * + ? { } [ ] \ | ( )

.           - Any Character Except New Line
\d          - Digit (0-9)
\D          - Not a Digit (0-9)
\w          - Word Character (a-z, A-Z, 0-9, _)

\W          - Not a Word Character
\s          - Whitespace (space, tab, newline)
\S          - Not Whitespace (space, tab, newline)

\b          - Word Boundary (Matches, without consuming any characters, immediately between a character matched by \w and a character not matched by \w (in either order). It cannot be used to separate non words from words.)
\B          - Not a Word Boundary
^           - Beginning of a String
$           - End of a String

[]          - Matches Characters in brackets
[^abc]      - Characters except a, b, c
[a-z]       - Characters in the range a-z
[^a-z]      - A character not in the range a-z
[a-zA-Z]    - A character in the range a-z or A-Z
[a|b]       - Alternate match either a or b

(?:...)     - Match everything enclosed
(...)       - Capture everything enclosed

a?          - Zero or none of a
a*          - Zero or more of a
a+          - Only one or more of a
a{3}        - Exactly 3 of a
a{3,}       - Exactly 3 or more of a
a{3,6}      - Between 3 and 6 of a

\n          - new line
\r          - carriage return
\t          - tab
\0          - null character
"""

import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHİJKLMNOPQURTUVWXYZ
1234567890

Ha HaH

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr Schafer
Mr Smith
Ms Davis
Mrs. Robinson

"""

pattern = re.compile(r'\n')
matches = pattern.finditer(text_to_search)

for match in matches:
    # span is beginning and end index
    # match is matched sub-string
    print(match)

# print(text_to_search[1:4])  # span=(1, 4) => 'abc'
