import turtle
import random
from tkinter import *


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


def draw_pie(probabilities, cv):
    """
    Given a dictionary of characters and their probabilities,
    draws a pie chart with a different random color for each character
    :param probabilities: a dictionary of characters to probablities
    :return: none
    """

    t = turtle.RawTurtle(cv)
    screen = t.getscreen()
    screen.clear()
    screen.colormode(255)

    radius = 200
    t.up()
    t.sety(-radius)
    t.down()
    t.speed(0)

    for character, probability in probabilities.items():
        r = random.randrange(0, 257, 10)
        g = random.randrange(0, 257, 10)
        b = random.randrange(0, 257, 10)

        t.fillcolor((r, g, b))
        t.color((r, g, b))
        t.begin_fill()
        t.circle(radius, probability * 360)
        position = t.position()
        t.goto(0, 0)
        t.end_fill()
        t.setposition(position)

    radius = 250
    t.up()
    t.sety(-radius)
    t.color("black")

    for character, probability in probabilities.items():
        t.circle(radius, probability * 360 / 2)
        if character == "\n":
            t.write("\\n, " + str(round(probability, 4)), align="center")
        elif character == " ":
            t.write("space, " + str(round(probability, 4)), align="center")
        else:
            t.write(character + ", " + str(round(probability, 4)), align="center")
        t.circle(radius, probability * 360 / 2)

    t.goto(0, 0)


def main():
    """
    Runs the main program
    :return: none
    """
    root = Tk()
    root.title("Letter Frequency")
    cv = Canvas(root, width=600, height=600)
    cv.pack(side=LEFT)
    label = Label(root, text="Enter your n:")
    label.pack()
    entry = Entry(root)
    entry.pack()
    entry.focus_set()
    probabilities = read_file()

    def callback():
        n = int(entry.get())
        if n > 54:
            n = 54
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

        draw_pie(new_probabilities, cv)
        print(entry.get())

    b = Button(root, text="get", width=10, command=callback)
    b.pack()

    root.mainloop()


main()
