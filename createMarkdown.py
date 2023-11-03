def createMarkdown(date, filename):
    with open(filename, 'w') as f:
        f.write("## " + date + "\n")