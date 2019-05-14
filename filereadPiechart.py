#filereadPiechart.py

#definition of the fileRead method

def fileRead():

    #Get the file name

    filename = input("Enter file name ")

    #open the file in read mode

    fileContent = open(filename,'r')

    readContents = fileContent.readlines()

    letterdic={}

    print()

    print("####### The text from file ####### ")

    print()

    #iterate the file contents

    for eachline in readContents:

        print(eachline)

        for letter in eachline:

            letterCount = eachline.count(letter)

            letterdic[letter] =letterCount

    sumofFrequencyofAllLetters = 0

    #iterate the letterdictionary

    #find the sumofFrequencyofAllLetters

    for letter,letterCount in letterdic.items():

        sumofFrequencyofAllLetters = sumofFrequencyofAllLetters + letterCount

    #Display statement

    print()

    print("###### Frequencies of all Letters from file ####### ")

    print()

    print("?Frequencies of all Letters " ,sumofFrequencyofAllLetters)

    print()

    print("###### Probability of each letter from file ####### ")

    #iterate the letterdictionary

    #find the probability of Letter

    requiredletters =[]

    sumofProbability =0

    for letter,letterCount in letterdic.items():

        probabilityofLetter = letterCount/int(sumofFrequencyofAllLetters)

        print()

        print("probability of Letter = Frequency of letter         ",      " = ",letter," = ",probabilityofLetter)

        print("                        ____________________________")

        print("                        ?Frequencies of all Letters ")

        sumofProbability = sumofProbability + probabilityofLetter





        if letter == 'i':

            print("probability of Letter = Frequency of letter         ",      " = ",letter," = ",probabilityofLetter)

            print("                        ____________________________")

            print("                        ?Frequencies of all Letters ")

        if letter == 's':

            print("probability of Letter = Frequency of letter         ",      " = ",letter," = ",probabilityofLetter)

            print("                        ____________________________")

            print("                        ?Frequencies of all Letters ")

        if letter == 'e':

            print("probability of Letter = Frequency of letter         ",      " = ",letter," = ",probabilityofLetter)

            print("                        ____________________________")

            print("                        ?Frequencies of all Letters ")



        requiredletters.append(probabilityofLetter)

    print(set(requiredletters))

    #return the sum of frequency of all letters in file

    return (sumofFrequencyofAllLetters,set(requiredletters),sumofProbability)
