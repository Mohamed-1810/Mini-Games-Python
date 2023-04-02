import random

def hangman():
    word=random.choice(["hello","superman","thor","captain","hulk","avenger",""])
    valid="abcdefghijklmnopqrstuvwxyz"
    Turns=10
    guessmade=''
    print("----START----")
    while(len(word)>0):
        main=""
        missed=0

        if Turns==0:
            print()
            print("You Let A kind Man Die")
            print(" ---------- ")
            print("      0_|   ")
            print("     /|\     ")
            print("     / \    ")
            print("You Lose ",name)
            y=input("Press Y to play again: ")
            if y.lower()=='y':
                hangman()
            print("----END----")

        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+"_"+" "

        if main==word:
            print("The Word is ",main)
            print("You Won ",name)
            y=input("Press Y to play again: ")
            if y.lower()=='y':
                hangman()
            print("----END----")
            break
        # else:
        #     print("Guess The Word in %d Turns"%Turns)


        print("Guess the Word: ",main)
        # print("%d Turns Left"%Turns)
        guess=input()

        if guess in valid:
            guessmade=guessmade+guess
        else:
            print("Enter Valid Characters: ")
            guess=input()

        if guess not in word:
            Turns-=1
            if Turns==9:
                print("9 turns left")
                print(" ---------- ")
            if Turns==8:
                print("8 Turns Left")
                print(" ---------- ")
                print("      0     ")
            if Turns==7:
                print("7 Turns Left")
                print(" ---------- ")
                print("     0      ")
                print("     |      ")
            if Turns==6:
                print("6 Turns Left")
                print(" ---------- ")
                print("      0     ")
                print("      |     ")
                print("     /      ")
            if Turns==5:
                print("5 Turns Left")
                print(" ---------- ")
                print("      0     ")
                print("      |     ")
                print("     / \    ")
            if Turns==4:
                print("4 Turns Left")
                print(" ---------- ")
                print("    \ 0     ")
                print("      |     ")
                print("     / \    ")
            if Turns==3:
                print("3 Turns Left")
                print(" ---------- ")
                print("    \ 0 /   ")
                print("      |     ")
                print("     / \    ")
            if Turns==2:
                print("2 Turns Left")
                print(" ---------- ")
                print("    \ 0 /|  ")
                print("      |     ")
                print("     / \    ")
            if Turns==1:
                print("1 Turns Left")
                print("Last Breathe")
                print(" ---------- ")
                print("    \ 0_|/  ")
                print("      |     ")
                print("     / \    ")

name=input("Enter Your Name: ")
print("Welcome,",name)

print("Guess the Word in Less than 10 Turns")

hangman()
