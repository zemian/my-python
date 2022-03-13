from english_words import english_words_set

count = 0
for word in english_words_set:
    print(word)
    count += 1
    if count > 10:
        break

print("...")
print("There are total %d words.", len(english_words_set))
