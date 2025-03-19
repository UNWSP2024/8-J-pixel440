

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    words = []
    word = ""

    for char in sentence:
        if char.isupper() and word:
            words.append(word.lower())
            word = char
        else:
            word += char


    if word:
        words.append(word.lower())

    corrected_sentence = ' '.join([words[0].capitalize()] + [word for word in words[1:]])

    return corrected_sentence.strip()


sentence = input("Please enter a sentence with no spaces and I'll fix it with my magic code (just make sure you capitalize the first letter of each word): ")
result = word_separator(sentence)
print(result)



