print('loading words from file')
print("")
import hangman1
o=hangman1.read_file()
print('ARE YOU READY???\nenter y or Y to start') #asking the user if he is ready
a=input()
if a=='y':
    import hangman3
    hangman3.char(a)
    import hangman4
    hangman4.guess(o)




