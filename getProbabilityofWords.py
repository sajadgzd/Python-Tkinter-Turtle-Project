

def probabilities():

    Words = open("Words.txt")
    frequencies = {}

    for line in Words:
        for character in line:
            if character not in frequencies:
                frequencies[character] = 1
            else:
                frequencies[character] += 1

    sum_of_frequencies = 0
    for character in frequencies:
        sum_of_frequencies += frequencies[character]

    probabilities = {}
    for character in frequencies:
        probabilities[character] = frequencies[character]/sum_of_frequencies

    return probabilities
