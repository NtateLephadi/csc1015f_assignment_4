def to_pig_latin(sentence):
    pig_latin = ''
    sentence = sentence.split()
    for word in sentence:
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            word = word + 'way '
        else:
            consonant = ''
            for i in word:
                if i in ['a', 'e', 'i', 'o', 'u']:
                    break
                else:
                    consonant += i
            word = word[len(consonant)::] + consonant + 'ay '
        pig_latin += word
    return pig_latin