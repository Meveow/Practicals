
words_in_text = {}

text = input("Enter a text: ")
print(f"Text: {text}")
words = text.split()


for word in words:
    try:
        words_in_text[word] += 1
    except KeyError:
        words_in_text[word] = 1

for words, count in sorted(words_in_text.items()):
    print(f"{words:10} : {count:1}")

