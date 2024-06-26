#!/usr/bin/python3
"""Text_indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each
    of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_characters = {'.', '?', ':'}
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in special_characters:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end='')
