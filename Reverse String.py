word  = "They are really good at presenting confidence what they don't have"


def reverse_string_method_one(word):
    return word[::-1] 

def reverse_string_method_two(word):
    reversed_string = ''
    for letter in word:
        reversed_string = letter + reversed_string
    return reversed_string

def reverse_string_method_three(word):
    return "".join(reversed(word))


def reverse_string_method_four(word):
    word = list(word)
    word.reverse()
    return "".join(word)

print("The First Method to reverse a string :- %s",reverse_string_method_one(word))
print("The Second Method to reverse a string :- %s",reverse_string_method_two(word))
print("The Third Method to reverse a string :- %s",reverse_string_method_three(word))
print("The Fourth Method to reverse a string :- %s",reverse_string_method_four(word))
