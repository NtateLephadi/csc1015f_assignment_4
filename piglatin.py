# return the Pig Latin sentence for a given English sentence.
def to_pig_latin(sentence):
    pig_latin = ''
    sentence = sentence.split()
    for word in sentence:
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            word = word + 'way'
        else:
            consonant = ''
            for i in word:
                if i in ['a', 'e', 'i', 'o', 'u']:
                    break
                else:
                    consonant += i
            word = word[len(consonant)::] + 'a' + consonant + 'ay'
        pig_latin += word + ' '
    return pig_latin

def remove_way(word):
    word = word[:len(word) - 3]
    return word

def remove_ay(word):
    word = word[:len(word) - 2]
    return word

# return the English sentence for a given Pig Latin sentence.
def to_english(sentence):
    english = ''
    sentence = sentence.split()
    for word in sentence:
        if word[len(word) - 3::] == 'way':
            word = remove_way(word)
        else:
            word = remove_ay(word)
            consonants = word[word.rindex('a') + 1:]
            word = word[:word.rindex('a')]
            word = consonants + word
        english += word + ' '
    return english