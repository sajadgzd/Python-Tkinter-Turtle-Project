import turtle
import random
from tkinter import *
import getProbabilityofWords


def pie(trtl,probabilities):
    trtl
    screen = trtl.getscreen()
    screen.colormode(255)

    radius_of_circle = 270
    trtl.up()
    trtl.sety(-radius_of_circle)
    trtl.down()
    trtl.speed(0)

    for letter, probability in probabilities.items():
        r = random.randrange(0, 257, 10)
        g = random.randrange(0, 257, 10)
        b = random.randrange(0, 257, 10)

        trtl.fillcolor((r, g, b))
        trtl.color((r, g, b))
        trtl.begin_fill()
        trtl.circle(radius_of_circle, probability * 360)
        pos = trtl.position()
        trtl.goto(0, 0)
        trtl.end_fill()
        trtl.setposition(pos)


    radius_of_legend = 305
    trtl.up()
    trtl.sety(-radius_of_legend)
    trtl.color("black")

    for letter, probability in probabilities.items():

        trtl.circle(radius_of_legend, probability * 360 / 2)

        if letter == "\n":
            trtl.write("\\n, " + str(round(probability, 4)), align="center")
        elif letter == " ":
            trtl.write("white space, " + str(round(probability, 4)), align="center")
        elif letter == "\t":
            trtl.write("\\t, " + str(round(probability, 4)), align="center")
        else:
            trtl.write(letter + ", " + str(round(probability, 4)), align="center")
        trtl.circle(radius_of_legend, probability * 360 / 2)

    trtl.goto(0, 0)

def main():

    master = Tk()
    master.title("Letter Frequency Chart (Ali - Sajad - Francisco)")
    canvas = Canvas(master, width = 850, height = 750)
    canvas.pack(side = BOTTOM)
    label = Label(master, text="Please enter your n which is < 55 :")
    label.pack()
    input = Entry(master)
    input.pack()
    trtl = turtle.RawTurtle(canvas)

    probabilities = getProbabilityofWords.probabilities()

    def draw():
        trtl.reset()
        n = int(input.get())
        if n > 54:
            c = Label(master, text = "You entered a number greater than 54, we fixed it for you and set it to 54", width = 100)
            c.pack()
            n = 54
        sorted_list = sorted(probabilities, key = probabilities.get, reverse = True)

        if n > len(sorted_list):
            n = len(sorted_list)

        sum_probability = 0;
        ordered_probabilities = {}
        for i in range(n):
            character = sorted_list[i]
            probability = probabilities[character]
            ordered_probabilities[character] = probability
            sum_probability += probability
        ordered_probabilities["All other letters"] = 1 - sum_probability
        pie(trtl,ordered_probabilities)
        print(input.get())

    b = Button(master, text = "Run the Chart", width = 11, command = draw)

    b.pack()
    master.mainloop()



main()

