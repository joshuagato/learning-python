print("*" * 150)

jabber = open("d:\HARD-CODING\PYTHON\InputAndOutput\sample.txt", 'r')

# for line in jabber:
#     print(line)

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()

print("*" * 150)    # ==============================================================

# Using the with keyword in this code block means, we dont need to worry about error handling
# since exception handling works under the hood for us with the help of with
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

print("*" * 150)    # ==============================================================

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

print("*" * 150)

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
    print(lines)

print("*" * 150)    # ==============================================================
