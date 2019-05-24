import turtle
import random


def read_file():
    """
    Reads the "Words.txt" file and creates a dictionary
    of the probabilities of each character in the file.
    :return: a dictionary of character probabilities
    """
    frequencies = dict()
    file = open("Words.txt")

    for line in file:
        for character in line:
            if character not in frequencies:
                frequencies[character] = 1
            else:
                frequencies[character] += 1

    total = 0
    for character in frequencies:
        total += frequencies[character]

    probabilities = dict()
    for character in frequencies:
        probabilities[character] = frequencies[character]/total

    return probabilities


def draw_pie(probabilities):
    """
    Given a dictionary of characters and their probabilities,
    draws a pie chart with a different random color for each character
    :param probabilities: a dictionary of characters to probablities
    :return: none
    """
    radius = 200
    turtle.up()
    turtle.sety(-radius)
    turtle.down()
    turtle.colormode(255)
    turtle.speed(0)

    for character, probability in probabilities.items():
        r = random.randrange(0, 257, 10)
        g = random.randrange(0, 257, 10)
        b = random.randrange(0, 257, 10)

        turtle.fillcolor((r, g, b))
        turtle.color((r, g, b))
        turtle.begin_fill()
        turtle.circle(radius, probability * 360)
        position = turtle.position()
        turtle.goto(0, 0)
        turtle.end_fill()
        turtle.setposition(position)

    radius = 250
    turtle.up()
    turtle.sety(-radius)
    turtle.color("black")

    for character, probability in probabilities.items():
        turtle.circle(radius, probability * 360 / 2)
        if character == "\n":
            turtle.write("\\n, " + str(round(probability, 4)), align="center")
        elif character == " ":
            turtle.write("space, " + str(round(probability, 4)), align="center")
        else:
            turtle.write(character + ", " + str(round(probability, 4)), align="center")
        turtle.circle(radius, probability * 360 / 2)
    turtle.goto(0, 0)
    turtle.done()


def main():
    """
    Runs the main program
    Asks the user for the number of characters to report in the pie chart
    If the number is greater than 54, it asks again
    :return: none
    """
    n = int(input("Please enter n: "))
    while n > 54:
        print("n must be 54 or less")
        n = int(input("Please enter n: "))
    probabilities = read_file()

    ordered = sorted(probabilities, key=probabilities.get, reverse=True)
    new_probabilities = dict()
    remaining = 1

    if n > len(ordered):
        n = len(ordered)

    for i in range(n):
        character = ordered[i]
        probability = probabilities[character]
        new_probabilities[character] = probability
        remaining -= probability
    new_probabilities["All other letters"] = remaining

    draw_pie(new_probabilities)


main()
