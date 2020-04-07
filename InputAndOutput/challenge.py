print("*" * 150)    # ==============================================================

# Appending to an existing file
with open("sample.txt", 'a') as tables:
    for i in range(2, 13):
        print("-" * 30, file=tables)
        for j in range(1, 13):
            print("{0} times {1:>2} is {2}".format(i, j, i * j), file=tables)
        print("-" * 30, file=tables)
print("Done appending to file")

print("*" * 150)    # ==============================================================
