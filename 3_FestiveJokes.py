#Ask for user input
Start = str(input("Would you like to hear a joke? Type yes or no: "))

#Set Boolean variable
Yes = Start == "Yes" or Start =="yes"

#Nested if statement containing multiple jokes with user input
if Yes:
    print("Knock, knock.")
    question_1 = str(input())
    #print(question_1)
    answer_1 = "Mary"
    print(answer_1)
    question_2 = str(input())
    answer_2 = "Mary Christmas!"
    print(answer_2)

    SecondJoke = str(input("\nWould you like to hear another joke? Type yes or no: "))

    if SecondJoke == "yes" or SecondJoke == "Yes":

        #Creating a function as alternative method to deliver joke
        def Santa():
            Joke2 = ["Ho Ho.", "Your Santa impression needs a little work!"]

            print("\nKnock, knock.")
            question_1 = str(input())
            print(Joke2[0])
            question_2 = str(input())
            print(Joke2[1])
            return


        Santa()

    elif SecondJoke == "no" or "No":
        print("Bah humbug!!")

else:
    print("Bah humbug!!")








