# Kullanıcıdan Alınan mestinde en çok tekrar eden harfi ve tekrar sayısını yazan uygulama

text = input("Enter a text: ")
word_repetitions = {}
for word in text:
    if word.isalpha():
        if word in word_repetitions:
            word_repetitions[word] += 1
        else:
            word_repetitions[word] = 1
most_repetiton_word = max(word_repetitions, key=word_repetitions.get)

repetition_number = word_repetitions[most_repetiton_word]

print(most_repetiton_word, repetition_number)
