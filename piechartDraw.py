
#fileRead()

#piechartDraw.py

#import tkinter module

import tkinter

#import module to find the probability of letters

from filereadPiechart import fileRead

from decimal import Decimal

#save the numberofletters from file

(returnNumberofLetters,individualProbabilitylist,sumofProbability) = fileRead()

individualProbabilitylist= list(individualProbabilitylist)

AllotherProbability = sumofProbability -(individualProbabilitylist[0]+individualProbabilitylist[1]+individualProbabilitylist[2])

#Display statement

print()

print("return Number of Letters ",returnNumberofLetters)

print()

#definition of the pie chart with drawDiagram method

def drawDiagram(n):

    return 360. * n / 500

#create canvas with width and height

canvasOutput = tkinter.Canvas(width=300, height=250);

canvasOutput.pack()

#create arc in the pie chart through canvas

canvasOutput.create_arc((2,2,98,98), fill="black", start=drawDiagram(0), extent = drawDiagram(100))

canvasOutput.create_text((120,30),text = "i ," + str(round(individualProbabilitylist[0],4)))

canvasOutput.create_arc((2,2,98,98), fill="gray", start=drawDiagram(100), extent = drawDiagram(400))

canvasOutput.create_text((120,70),text = "s , "+ str(round(individualProbabilitylist[1],4)))

canvasOutput.create_arc((2,2,98,98), fill="red", start=drawDiagram(400), extent = drawDiagram(100))

canvasOutput.create_text((70,110),text = "e, " + str(round(individualProbabilitylist[2],4)))

canvasOutput.create_arc((2,2,98,98), fill="white", start=drawDiagram(600), extent = drawDiagram(200))

canvasOutput.create_text((80,5),text = "All other letters, " + str(round(AllotherProbability,4)))

print("---------")

canvasOutput.mainloop()
