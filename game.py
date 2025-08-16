print("Welcome to adventure game!")

def startGame():
    path = input("You are right next to a creepy forest, will you go in or stay out?(in/out): ").lower()
    if path == "out":
        print("Congrats, you didn't even start the adventure but you live! :D")
    else:
        scarySoundPath = input("You hear a scary sound from the right side, which way you go?(right/left): ").lower()
        if scarySoundPath == "left":
            possibleEnd = input("Now you see the exit, do you want to leave or stay?(stay/leave): ").lower()
            if possibleEnd == "leave":
                print("Congrats, you didn't die!")
            else:
                print("A bear attacked you and you died! =(")
        else:
            print("The sound you heard is from a vampire!!!!!!! OH NOOOOOOOO, YOU DIED HAHAHAHAHAH")

while True:
    startGame()
    playAgain = input("Do you want to play again?(Y/N): ").lower()
    if playAgain == "n":
        break