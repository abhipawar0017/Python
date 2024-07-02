def remove_Strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "  Abhi is   a good"
n = remove_Strip(this, "Abhi")
print(n)
