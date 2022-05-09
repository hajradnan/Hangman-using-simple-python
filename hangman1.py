def read_file():
    with open('words.txt')as f:
        contents=[] #initializing the list
        warnings=3 #initial warnings
        guesses=6 #initial guesses
        print("55900 words loaded")
        print("")
        x=f.read() #reading whole file
        s=x.split() #splitting the words
        contents+=s #to make it a list
        print('GAME TIME')
        print("")
        print('welcome to the game "HANGMAN"') #welcoming the user
        import random
        x=random.choice(contents) #making a random choice
        print('I am thinking of a number which is',len(x),'letters long') #thinking of a number
        print("")
        print('you have',warnings,'warnings left')
        print('---------------')
        print('you have',guesses,'guesses left')
        return x
        
