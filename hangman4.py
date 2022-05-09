def  guess(x):
        c=[]
        warnings=3
        guesses=6
        lower_case='abcdefghijklmnopqrstuvwxyz'
        import hangman5
        fake='-'*len(x)
        while guesses!=0:
                b=input('please guess a letter=') #guessing the letter
                if 'a'<=b<='z' or 'A'<=b<='Z':
                        for char in b:
                                if char in x:#putting underscores
                                        print('good guess')
                                        fake=list(fake) #This will convert fake to a list, so that we can access and change it.
                                        for k in range(0,len(x)): ##For statement to loop over the answer (not really over the answer, but the numerical index of the answer)
                                                if b==x[k]: #If the guess is in the answer
                                                        fake[k]=b #change the fake to represent that, EACH TIME IT OCCURS
                                        m=''.join(fake)  #converts from list to string
                                        print(m)
                                        print('you have',guesses,'guesses left') #remaining guesses
                                        print('---------------')
                                else:
                                        if char in 'aeiouAEIOU':
                                                m=''.join(fake)
                                                guesses-=2
                                                print('oops!this letter is not in my word\ntry again!')#if the character entered by the person is not in the word
                                                print('you have',guesses,'guesses left')
                                                print(m)
                                        else:
                                                m=''.join(fake)
                                                guesses-=1
                                                print('oops!this letter is not in my word\ntry again!')#if the character entered by the person is not in the word
                                                print('you have',guesses,'guesses left')
                                                print(m)
                                if guesses==0 or warnings==0:
                                        m=''.join(fake)
                                        if m!=x:
                                                print('sorry you ran out of guesses\nbetter luck next time') #the person fails to guess the word
                                                print('the word is',x)
                                                print('your score is',hangman5.score(guesses,x))
                                                break
                                        elif m==x:
                                                print('congratulations!you have guessed the word') ##the person have won the game
                                                print('your score is',hangman5.score(guesses,x))
                                                break
                                if '-' not in m:
                                        print('congratulations!you have guessed the word') ##the person have won the gam
                                        print('your score is',hangman5.score(guesses,x))
                                        break
                else:
                        print('oops!it is not a valid character') #when the person enters a character other than alphabet
                        warnings-=1
                        print('you have',warnings,'warnings left') #remaining warnings
                        print('---------------')
                lower_case=lower_case.replace(b,'') #omitting the letter alreadyentered by the user using replace function
                m=''.join(fake)
                if m==x:
                        break
                if guesses!=0:
                        print('available letters are',lower_case) #available letters
        
