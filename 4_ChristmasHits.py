#Reading the lyrics of a song from a text file
print("""List of the top 5 most streamed Christmas songs based on streams on Spotify between Jan. 1 to Dec. 7, 2020:
 
 1. "All I Want for Christmas Is You", Mariah Carey
    2. "Last Christmas", Wham! 
        3. "Santa Tell Me", Ariana Grande
            4. "It's Beginning to Look a Lot like Christmas", Michael Bublé 
                5. "Rockin' Around the Christmas Tree", Brenda Lee

source: https://www.foxnews.com/entertainment/most-streamed-christmas-songs-2020""")

SongChoice = int(input("\nIt's karaoke time and you're up next! Select an option from above (e.g. enter 2 for \"Last Christmas\" by Wham!): " ))

if SongChoice == 1:
    lyrics = open('MariahCarey.txt', 'r')
    for line in lyrics:
        print(line)

    #Closing the text file
    lyrics = open('MariahCarey.txt', 'r')
    print(lyrics.read())
    lyrics.close()

if SongChoice == 2:
    lyrics = open('Wham!.txt', 'r')
    for line in lyrics:
        print(line)

    # Closing the text file
    lyrics = open('Wham!.txt', 'r')
    print(lyrics.read())
    lyrics.close()

if SongChoice == 3:
    lyrics = open('Ariana Grande.txt', 'r')
    for line in lyrics:
        print(line)

    # Closing the text file
    lyrics = open('Ariana Grande.txt', 'r')
    print(lyrics.read())
    lyrics.close()

if SongChoice == 4:
    lyrics = open('MichaelBublé.txt', 'r')
    for line in lyrics:
        print(line)

    # Closing the text file
    lyrics = open('MichaelBublé.txt', 'r')
    print(lyrics.read())
    lyrics.close()

if SongChoice == 5:
    lyrics = open('BrendaLee.txt', 'r')
    for line in lyrics:
        print(line)

    # Closing the text file
    lyrics = open('BrendaLee.txt', 'r')
    print(lyrics.read())
    lyrics.close()

else:
    print("Oops, looks like you didn't pick on of the options!")