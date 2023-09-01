text = input("Write your string: ")

# Divide the line into words by spaces
word = text.split()

# Reverse the list of words in reverse order
reversed_words = word[::-1]

# Combine the words again into a line
output = ' '.join(reversed_words)

print(output)