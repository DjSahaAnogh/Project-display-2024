# Note: The practicepythonorg_probles.py file became too large, causing the code to execute slowly. 
# Therefore, I created a second part of it. 😇

# URL OF THE WEBSITE https://www.practicepython.org/

# ALL IMPORTS
import random
import requests
from bs4 import BeautifulSoup

# 18. Decode A Web Page Two

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
responce = requests.get(url)

soup = BeautifulSoup(responce.text, "html.parser")
title = soup.title.string

article = soup.find_all("p")
x: int = 0
# for i in article:
#   x += 1
#   print(f"{x}:\n {i.get_text()}\n")

# 19.  Write a function that takes an ordered list of numbers and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def check_list(num_list: list, num: int) -> bool:
  if num in num_list:
    return True
  else:
    return False
  
# print(check_list([1, 2, 3, 4, 5], 3))

# or

def binary_search(arr: list, target: int) -> bool:
    low: int = 0
    high: int = len(arr) - 1
    
    while low <= high:
        mid: int = (low + high) // 2 
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        return False
    
# print(binary_search([1, 2, 3, 4, 5], 3))

# 20. Write To A File
with open("emaple.txt", "w") as text:
    text.write("hello")

# 21. Read from a file
with open("nameslist.txt", "r") as read_file:
   names: list = []
   for line in read_file:
      names.append(line.strip())
new_name_set = set(names)
# print(new_name_set)

# 22. File overlap

with open("primenumbers.txt", "r") as prime_nums:
   prime_list: list = []
   for line in prime_nums:
        prime_list.append(line.strip())

with open("happynumbers.txt", "r") as happy_nums:
    happy_list: list = []
    for line in happy_nums:
          happy_list.append(line.strip())

overlap_list: list = []
for i in prime_list:
    if i in happy_list:
        overlap_list.append(i)
# print(overlap_list)

# 23. Draw A Game Board
def draw_board() -> None:
    size: int = int(input("Enter the size of the board: "))
    for i in range(size):
        print(" ---" * size)
        print("|   " * (size + 1))
    print(" ---" * size)

# draw_board()

# 24. Guessing Game Two
def computer_guess() -> None:
    high_point: int = int(input("Please enter a range of numbers you want the computer to guesses from: "))
    number_line: list = [i for i in range(1, high_point + 1)]
    low: int = number_line.index(1)
    high: int = number_line.index(high_point)
    guesses: int = 1
    while True:
        num = number_line[len(number_line) // 2]
        print(f"Is your number {num}?")
        ans = input("Enter 'c' if it's correct, 'h' if your number is higher, and 'l' if your number is lower: ").lower()
        if ans == "c":
            print(f"I got it right in {guesses} guesses.")
            break
        elif ans == "h":
            high = number_line.index(num)
            number_line = number_line[:high]
        elif ans == "l":
            low = number_line.index(num)
            number_line = number_line[low:]
        else:
            print("Invalid input, please enter only c, h or l according to the instructions.")
            continue
        guesses += 1

# computer_guess()

# 25. Tic Tac Toe
def sum(a, b, c):
    return a + b + c

def print_board() -> None:
    zero = "X" if xState[0] else ("O" if yState[0] else 0)
    one = "X" if xState[1] else ("O" if yState[1] else 1)
    two = "X" if xState[2] else ("O" if yState[2] else 2)
    three = "X" if xState[3] else ("O" if yState[3] else 3)
    four = "X" if xState[4] else ("O" if yState[4] else 4)
    five = "X" if xState[5] else ("O" if yState[5] else 5)
    six = "X" if xState[6] else ("O" if yState[6] else 6)
    seven = "X" if xState[7] else ("O" if yState[7] else 7)
    eight = "X" if xState[8] else ("O" if yState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkwin(xState, yState) -> int:
    wins: int = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X wins!")
            return 1
        elif sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3:
            print("O wins!")
            return 0
    return -1

xState: list = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 means empty, 1 means X, O
yState: list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def game():
    player_turn: int = 1
    print_board()
    while True:
        if player_turn == 1:
            print("X player's turn, enter a position from 1 to 9")
            try:
                x: int = int(input("Here: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            if type(x) == int:
                xState[x] = 1
                player_turn = 2
                print_board()
            else:
                print("Invalid input.")
        elif player_turn == 2:
            print("O player's turn, enter a position from 1 to 9")
            try:
                y: int = int(input("Here: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            if type(y) == int:
                yState[y] = 1
                player_turn = 1
                print_board()
            else:
                print("Invalid input.")
        if checkwin(xState, yState) != -1:
            break

# game()

# 26. Max Of Three
def largest(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
# print(largest(1, 2, 3))
    
# 27. Pick a word
with open("common_words_uppercase.txt", "r") as file:
    words: list = []
    for line in file:
        words.append(line.strip())
    word = random.choice(words)
    pass
    # print(word)

# 28. Guess Letters
def guess_word() -> None:
    word: str = random.choice(words)
    guess: str = "-" * len(word)
    guess_letter: list = []
    letter_list: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    word_list: list = list(word)
    guess_list: list = list(guess)
    mistake: int = 0
    while mistake != 10:
        print(guess)
        print(f"You have {10 - mistake} mistakes left.")
        print(f"Letters you have guessed: {guess_letter}")
        print(f"Letters you haven't guessed: {letter_list}")
        guess_letter.append(input("Enter a letter: ").upper())
        letter_list.remove(guess_letter[-1])
        for i in range(len(word)):
            if word[i] in guess_letter:
                guess_list[i] = word[i]
                guess = "".join(guess_list)
        if guess_letter[-1] not in word:
            mistake += 1
        if "-" not in guess:
            print("You win!")
            print(f"The word was {word}")
            break

    if mistake == 10:
        print("You lose!")
        print(f"The word was {word}")

# guess_word()

# 28. Birthday Dictionaries
def birthday_dictionary() -> None:
    birthdays = {
        "Arijit": "28/03/2009",
        "Naimur": "28/03/2009",
        "Maruf": "10/04/2009",
        "Samiul": "19/04/2009", 
        "Anish": "30/06/2009",
        "Joyanto": "22/07/2009"
    }
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthdays:
        print(name)

    name = input("Who's birthday do you want to look up?: ")
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}")
    else:
        print("Sorry, we don't have birthday information for that person.")