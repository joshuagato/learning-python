def python_food():
    print("spam and eggs")


def python_food2():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
# python_food()
# print()
# print(python_food())

python_food()
python_food2()
centre_text("spam, spam and eggs")
centre_text("spam, spam, spam and spam")

print("*" * 150)  # =========================================================================

