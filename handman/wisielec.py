from re import A
import sys
from random import *


no_of_tries = int(input("Podaj ilość żyć: "))
#word_to_rand = ['Piotr' 'Jakub' 'Laurencjusz' 'Kacper' 'Konstantyn']
word = "kamila"
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word): #enumerate przypisuje index do danej litery w tym przypadku
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print()
    print("Pozostało prób: ", no_of_tries)
    print()
    print("Użyte litery: ", used_letters)
    print()

#######

for _ in word:
    user_word.append("_")

while True: #pętla nieskończona
    letter = input("Podaj literę: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(letter) == 1 or len(letter) == 0:
        if len(letter) != 0:
            if letter.isalpha():        



                if len(found_indexes) == 0:
                    print()
                    print("Nie ma takiej litery")
                    no_of_tries -= 1            

                    if no_of_tries == 0:
                        print("Przegrałeś :( \n \n \n Koniec gry")
                        sys.exit(0)

                else:
                    for index in found_indexes:
                        user_word[index] = letter
                                    

                    if "".join(user_word) == word:
                        print("Brawo! To jest to słowo!")
                        sys.exit(0)

                show_state_of_game()



            else:
                print("Wprowadź literę, nie liczbę")
        else:
            print("Musisz podać jakąś literę") 
    else:
        print("Możesz podać tylko jeden znak na raz")