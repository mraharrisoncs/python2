#Function to return the value of a letter
def value(letter):
    letter = letter.upper()
    alphabet = "EARIOTNSLCUDPMHGBFYWKVXZJQ"
    pos = alphabet.find(letter)
    val = pos + 1
    return val

# Function to return the value of a word
def points(word):
    total = 0
    # Get value of each letter
    for letter in (word):
        total = total + value(letter)
    return total

# Main program
print(points("we"))
