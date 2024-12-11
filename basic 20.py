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
def factor(num) -> int:
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