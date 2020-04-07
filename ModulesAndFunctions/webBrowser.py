import webbrowser

webbrowser.open("joshuagato.github.com", new=1)
# #
# # help(webbrowser)

# for i in range(10):
    # print(i)
    # print(1, 2, 3, 4, 5, 6, 7, 8, 9)
    # print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=' : ')
    # print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=' : ')

# chrome = webbrowser.get(using='google-chrome')
chrome = webbrowser.get('chrome %s').open_new_tab("joshuagato.github.com")

