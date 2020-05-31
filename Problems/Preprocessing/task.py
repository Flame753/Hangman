text = input()
symbols = [",", ".", "!", "?"]
for x in symbols:
    text = text.replace(x, "")
text = text.lower()
print(text)
