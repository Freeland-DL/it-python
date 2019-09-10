def banner(title, author):
    title_length = len(title)
    byline = f"By {author}"
    byline_length = len(byline)
    banner_length = max(title_length, byline_length) + 8

    print("=" * banner_length)
    print(f"{title:^{banner_length}}")
    print(f"{byline:^{banner_length}}")
    print("=" * banner_length)
    print("")

banner("BANNER", "Collin Freeland")

name = input ("What is your name? ")
quest = input("What is your Quest? ")
print("")
banner(quest,name)