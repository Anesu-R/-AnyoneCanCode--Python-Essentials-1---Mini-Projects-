import random

DarePart1 = ["Juggle two baubles","Go outside and shout Merry Christmas","Drink your favourite Christmas beverage",
             "Do your best impersonation of Buddy from the movie Elf","Give an impromptu presentation about Christmas",
             "Start singing your favourite Christmas song","Run around the Christmas tree",
            "Dance to 'Rockin' Around the Christmas Tree' by Brenda Lee","Pretend to be a reindeer","Eat the nearest food you can see"]

DarePart2 = [
    "with your eyes closed","whilst tapping your head","without blinking",
    "as loud as you can","with a sad face","as fast as you can","with the nearest person to you",
    "whilst doing the Michael Jackson moonwalk",
    "without laughing","with the song 'I Want a Hippopotamus for Christmas' by Gayla Peevey playing in the background"]

Timer = [15,30,45,60,75]

Dare1 = random.choice(DarePart1)

Dare2 = random.choice(DarePart2)

Duration = random.choice(Timer)

print("""\n        # What a bright time, it's the right time 
        To rock the night away
        
        Jingle bell time is a swell time...
        To play Christmas Dares, who0o0! #\n\n\n"""
)

print(Dare1,Dare2,"for", "-->{}<--".format(Duration), "seconds in \n3 \n2 \n1... \nGo!")


