# Note: The practicepythonorg_probles.py file became too large, causing the code to execute slowly. 
# Therefore, I created a second part of it. 😇

# URL OF THE WEBSITE https://www.practicepython.org/

# ALL IMPORTS
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

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print_board()