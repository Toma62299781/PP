import re
def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    ex = ''
    length = len(word)
    if word.isupper():
        for element in word:
            if word.index(element) != length-1:
                ex += repr(pow(10, length-1-word.index(element))) + '*' + element + '+'
            else:
                ex += repr(pow(10, length-1-word.index(element))) + '*' + element
        return '(' + ex + ')'
    else:
        return word

print compile_word('*')