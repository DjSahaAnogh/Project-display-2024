# All imports

from math import factorial

# 1. Print Your Name
name: str = "Dhanonjoy"
print(f"Hello! {name}")

# 2. Basic Arithmetic

def calculator() -> None:
  while True:
    try:
      num1: float = float(input("Enter the first number: "))
      num2: float = float(input("Enter the second number: "))
      op: str = input("Provide a operator(+, -, *, /, %, ^):")
    except ValueError:
      print("An error ocured. You entered an invalid value.")
      calculator()
    
    def check_op() -> bool:
      if op in ["+", "-", "*", "/", "%", "^"]:
        return True
      else:
        return False
    
    if check_op():
      if op == "+":
        print(num1 + num2)
        break
      if op == "-":
        print(num1 - num2)
        break
      if op == "*":
        print(num1 * num2)
        break
      if op == "/":
        if num2 != 0:
          print(num1/num2)
          break
        else:
          print("Divison by Zero Error!")
          break
      if op == "%":
        print(num1 % num2)
        break
      if op == "^":
        print(num1 ** num2)
        break
    else:
      print("Invalid operator! Try again.")
      calculator()
      break
  if input("Do you want to do another calculation?\nIf yes enter 'y' or enter any to exit: ").lower() == "y":
    calculator()

# calculator()

# 3. Area of a Rectangle
def area_rectangle() -> None:
  try:
    x: int = int(input("Enter the lenght(cm): "))
    y: int = int(input("Enter the breath(cm):"))
  except ValueError:
    print("Invalid input. Please try again.")
    area_rectangle()
  print(x * y)


# area_rectangle()

# 4. Simple Interest
class Profit:
  def __init__(self, capital: int, rate: float, time: int) -> None:
    self.capital = capital
    self.rate = rate
    self.time = time
  
  def interest(self, capital: int, rate: float, time: int) -> int:
    return capital*rate*time

p1: Profit = Profit(1000, 0.1, 2)
# print(p1.interest(1000, 0.1, 2))

# or

def intrest_cal(calpital: int, rate: float, time: int) -> int:
  return calpital*rate*time


# print(intrest_cal(1000, 0.1, 2))

# 5. Convert Temperature

def tem_cal_c_2_f(celcius: float) -> float:
  fharenhite: float= (celcius/5)*9+32
  return fharenhite
# print(tem_cal_c_2_f(37))

# 6. Check for Positive or Negative

def check_positive_or_negative(num: int) -> None:
  if num > 0:
    print(f"{num} is positive")
  else:
    print(f"{num} is negative")

# check_positive_or_negative(-5)

# 7. Calculate Factorial
def factor(num: int) -> int:
  return factorial(num)

# print(factor(5))

# 8. Sum of a List

num: list = [5, 6, 8, 12, 52, 12, 19, 55, 10, 14]

def sum_of_num(lis: list) -> None:
  x: int= 0
  for i in lis:
    x: int= x + i
  print(x)

# sum_of_num(num)

# 9. Count Characters in a String

def count_cha(cha: str) -> None:
  lis: list = list(cha)
  count = len(lis)
  print(count)

# count_cha("Hello")

# 10. Fizzbuzz

def fizzbuzz(num: int) -> None:
  if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
  elif num % 3 == 0:
    print("fizz")
  elif num % 5 == 0:
    print("buzz")
  else:
    print("Not divisible by 3 or 5")

# fizzbuzz(8)

# 11. Find Minimum and Maximum

x: list = [2, 6, 8, 12, 46, 52, 89, 852, 455, 22, 6, 52, 48, 66, 156, 45, 852, 75, 795, 52]

def min_max(lis: list) -> int:
  lis.sort()
  min_num: int = lis[0]
  max_num: int = lis[-1]
  return min_num, max_num

print(min_max(x))

# 12.Check Leap Year

def check_leap_year(year: int) -> bool:
  if year % 4 == 0:
    return True
  else:
    return False

# print(check_leap_year())

# 13. Count Words in a String

def word_count(data: str) -> int:
  info_lis: list = data.split(" ")
  ans = len(info_lis)
  return ans

print(word_count("Hey! I'm hope that u liked it so far!"))

# 14. Sum of Digits
def sum_digits(data: int) -> int:
    total_num: int = 0
    while data > 0:
        digit: int = data % 10  
        total_num += digit  
        data = data // 10
    return total_num

# print(sum_digits(123))


# 15. Multiplication Table

def multiplication(num: int, mul_range: int):
  for i in range(0, mul_range+1):
    data: int = num * i
    print(data)

# multiplication(5, 10)

# 16. Find All Divisors

def divisiors(num: int) -> int:
  divisiors: list = []
  for i in range(1, num+1):
    if num % i == 0:
      divisiors.insert(-1, i)
      divisiors.sort()
    else:
      continue
  return divisiors

# print(divisiors(12))

# 17. Check Palindrome (Number)
def palindrome(num: int) -> None:
  new_num: str = str(num)
  reverse: str = new_num[::-1]
  if new_num == reverse:
    print("It is a palindrome number.")
  else:
    print("It is not a palindrome number.")

# palindrome(121)

# 18. Armstrong Number

def is_armstrong_num(num: int) -> bool:
  data: str = str(num)
  lis: list = list(data)
  count: int = len(lis)
  total: int = 0
  for i in lis:
    x: int = int(i)
    total += x ** count
  if total == num:
    return True
  else:
    return False

# print(is_armstrong_num(158))

# 19. Count Occurrences of an Element

def count_occurrences(lis: list, element: any) -> None:
  lis.sort()
  count_instence: int = lis.count(element)
  print(count_instence)

# count_occurrences(x, 6)

# 20. Generate a List of Squares

def square_list(start_num: int, end_num: int) -> list:
  generated_list: list = []
  for i in range(start_num, end_num+1):
    generated_list.insert(-1, i**2)
    generated_list.sort()
  return generated_list

# print(square_list(6, 10))
