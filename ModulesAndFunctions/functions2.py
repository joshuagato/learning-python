print("*" * 150)  # =========================================================================

print("First", "Second", 3, 4, "spam")


def centre_text(*args, end='\n', file=None, flush=False):
    text = " "
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


def centre_text2(*args, end='\n', file=None, flush=False):
    text = " ".join(str(args))
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


def centre_text3(*args, sep=' ', end='\n', file=None, flush=False):
    text = " "
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


print("*" * 150)  # =========================================================================

# with open("centred", node='w') as centered_file:
#     centre_text("First", "Second", 3, 4, "spam", file=centered_file)
centre_text("First", "Second", 3, 4, "spam")

print("*" * 150)  # =========================================================================

centre_text2("First", "Second", 3, 4, "spam")

print("*" * 150)  # =========================================================================

centre_text3("First", "Second", 3, 4, "spam")

print("*" * 150)  # =========================================================================
