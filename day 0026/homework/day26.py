def sentence_to_list(sentence):
    # წინადადებას ვყოფთ სიტყვებად და ვაბრუნებთ სიად
    words = sentence.split()
    return words

def list_to_sentence(word_list):
    # სიტყვის სიას ვაქცევთ წინადადებად, სიტყვებს შორის ", " (დაშორებით)
    return ', '.join(word_list)

# მაგალითი
sentence = "This is an example sentence"
words = sentence_to_list(sentence)
print(list_to_sentence(words))  # "This, is, an, example, sentence"

def print_word_lengths(sentence):
    # სიტყვებს ვყოფთ და თითოეულ სიტყვაში სიმბოლოების რაოდენობას ვბეჭდავთ
    words = sentence.split()
    for word in words:
        print(f"{word}: {len(word)} characters")

# მაგალითი
print_word_lengths("This is an example sentence")  # Output: This: 4, is: 2, an: 2, example: 7, sentence: 8

def remove_extra_spaces(sentence):
    # წინადადებას ვცვლით, ყოველი ზედმეტი space-ის მაგივრად ვსვამთ მხოლოდ ერთ სივრცეს
    return ' '.join(sentence.split())

# მაგალითი
sentence = "This   is   an    example   sentence."
print(remove_extra_spaces(sentence))  # "This is an example sentence."


def replace_spaces_with_hyphen(sentence):
    # წინადადების სიტყვებს შორის spaces ვცვლით ტირეში
    return sentence.replace(" ", "-")

# მაგალითი
sentence = "This is an example sentence"
print(replace_spaces_with_hyphen(sentence))  # "This-is-an-example-sentence"

def reverse_words_in_sentence(sentence):
    # წინადადებაში სიტყვებს ვაბრუნებთ, მაგრამ სიტყვების შიგნით სიმბოლოები უცვლელი რჩება
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

# მაგალითი
sentence = "Hello World!"
print(reverse_words_in_sentence(sentence))  # "World! Hello"

text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"

text = "hello world"
title_text = text.title()
print(title_text)  # Output: "Hello World"
