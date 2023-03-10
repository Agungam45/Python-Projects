#This application allows a user to find the reading level of a given text using the Flesch readability test
#The Flesh Readability test uses a reading ease formula of 206.835 - 1.015 (total words/total sentences) - 84.6(total syllables/total words)
# I utilize functions to gather total words, total sentences, and total syllables, then pass them into a function to ultimately determine the Flesch reading level.

import ch1text

def count_sentences(text):

    count = 0

    terminal = '.;?!'

    for char in text:
        
        if char in terminal:
                
                count = count + 1

    return count

def count_syllables(words):

    #count variable holds the total number of syllables 
    count = 0

    for word in words:

        word_count = count_syllables_in_word(word)

        count = count + word_count    

    return count


def count_syllables_in_word(word):

    count = 0

    endings = ".,;!?:"

    last_char = word[-1]

    if last_char in endings:

        processed_word = word[0:-1]

    else:

        processed_word = word

    if len(processed_word) <= 3:

        return 1

    vowels = "aeiouAEIOU"

    prev_char_was_vowel = False
    

    for char in processed_word:

        if char in vowels:

            if not prev_char_was_vowel:

                count = count + 1

            prev_char_was_vowel = True

        else:

            prev_char_was_vowel = False

    if processed_word[-1] in 'yY':

        count = count + 1

    return count


def compute_readability(text):

    total_words = 0

    total_sentences = 0

    total_syllables = 0

    score = 0


    words = text.split()

    total_words = len(words)

    total_sentences = count_sentences(text)

    total_syllables = count_syllables(words)

    score = (206.835 - 1.015 * (total_words / total_sentences)
                     - 84.6 * (total_syllables / total_words))


    print(total_words, 'words')

    print(total_sentences, 'sentences')

    print(total_syllables, 'syllables')

    print(score, 'reading ease score')

    reading_level(score)

def reading_level(score):

    if score >= 90.0:

        print('Reading level of 5th Grade')

    elif score >= 80.0:

        print('Reading level of 6th Grade')

    elif score >= 70.0:

        print('Reading level of 7th Grade')

    elif score >= 60.0:

        print('Reading level of 8th Grade')

    elif score >= 50.0:

        print('Reading level of 9th Grade')

    elif score >= 30.0:

        print('Reading level of College Student')

    else:

        print('Reading level of College Graduate')

    
compute_readability(ch1text.text)
    
