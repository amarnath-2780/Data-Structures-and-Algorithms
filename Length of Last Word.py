
word = "No matter how good your chain"


def find_length_of_last_word(word):
    last_word = word.split(' ')
    return len(last_word[-1])


print("The Length Of The Last Word is  : %s",find_length_of_last_word(word))
