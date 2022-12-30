#Bug 1: if user enters the same word x5 the programme will still execute. How to prevent duplicated user input

print("\nThe festive season is full of fun and games... Here's a crossward for ya\nFind the following five words to gain points:\nscrooge, doom, marley, and, averious")

print("""\nurlttspoiinthsi
meokcesytfhemoe
lagosganldmesua
rsraooegnahcdog
psolooryriousio
doomervlndarlro
pemkscebmzlcker
slodfsdnaypalvc
shbcaiudaqocnas""")

Lyrics = ["scrooge","doom","marley","and","averious"]

Total = 0

while Total < 5:

    UserGuess = input("\nEnter a word from the crossword once you've found it: ")

    if UserGuess in Lyrics:
        Total += 1
        print("Fantastic! Total points: {}".format(Total))

print("\nFab stuff, you've found all the words!\n\nYou've earned five gold stars: *****")




