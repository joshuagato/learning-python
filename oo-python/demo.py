a_string = "this is \n a string split\t\tand tabbed"
print(a_string)

print()

raw_string = r"this is \n a string split\t\tand tabbed"
print(raw_string)

print()

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

print()

l_string = """
this is
a string split		and tabbed
"""
print(l_string)

print()

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)
backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)
