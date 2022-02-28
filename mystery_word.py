import random
from colorama import Fore

# colors
black  = '\033[30m'      
Red = '\033[31m'     
Green = '\033[32m'     
Yellow = '\033[33m'     
Blue = '\033[34m'     
Magenta= '\033[35m'     
Cyna = '\033[36m'      
White = '\033[37m'      
Reset = '\033[39m' 

print()

def play_game():
    # theirname = input("What is name?")
    # print("Good luck", theirname)

    with open("words.txt") as test_word:   
        words_list = test_word.read()                      #defining word_list as the txt doc and making it read whatever is in the doc
        words = list(map(str, words_list.split()))
        global the_word, current_guess                                    #global is supposed to make you use it anywhere
        the_word = random.choice(words)
        count = 8                                         #gives the number of tries they are allowed                                                                                
        print(Blue + "!Your wonderful word is", len(the_word), "letters long!" + Reset)   #len(the_word) gets the length of the random word
    display = ["_"] * len(the_word)
    wrong_answers = []
    while count > 0:
        current_guess = input("Hey, do you want to make your guess or just stare at the screen: ").casefold()
        i = 0
        if len(current_guess) != 1:
            print(Red + "Only use 1 letter plz" + Reset)
        elif current_guess in wrong_answers:
            print(Yellow + "Hey fool, you guessed this already" + Reset)
        elif current_guess in the_word:
            for letter in the_word:
                if letter == current_guess:
                    print(Green + "AYO!! that letter matched" + Reset)
                    display[i] = letter
                i += 1
        else:
            count = count - 1
            wrong_answers.append(current_guess)
            print(Red + "Oooopsie, wrongo! Now you have", count, "guesses left" + Reset)
        if "_" not in display:
            print(Green + Blue +"OMG Yay, you have guessed the word,", the_word, "! Go have yourself a cookie now" + Reset)
            print(display)
            exit()

        print(display)
    print(Red + "Sorry you have no more tries. The word was clearly {}".format(the_word) + Reset)

# I want to create a loop after the game so they can hit [y/n] to play the game again.



if __name__ == "__main__":
    play_game()
