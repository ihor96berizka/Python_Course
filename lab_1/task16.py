def reverse_string(text):
    # Divide the line into words by spaces
    word = text.split()

    # Reverse the list of words in reverse order
    reversed_words = word[::-1]

    # Combine the words again into a line
    output = ' '.join(reversed_words)

    return output


text = input("Write your string: ")
result = reverse_string(text)
print(result)
