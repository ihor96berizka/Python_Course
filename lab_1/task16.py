def func(text):
    # Divide the line into words by spaces
    word = text.split()

    # Reverse the list of words in reverse order
    reversed_words = word[::-1]

    # Combine the words again into a line
    output = ' '.join(reversed_words)

    return output


text1 = input("Write your string: ")
result = func(text1)
print(result)
