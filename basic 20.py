# Print Your Name
name: str = "Dhanonjoy"
print(f"Hello! {name}")

# Basic Arithmetic

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

# Area of a Rectangle
def area_rectangle() -> None:
  try:
    x: int = int(input("Enter the lenght(cm): "))
    y: int = int(input("Enter the breath(cm):"))
  except ValueError:
    print("Invalid input. Please try again.")
    area_rectangle()
  print(x * y)


# area_rectangle()

# Simple Interest
class Profit:
  def __init__(self, capital: int, rate: float, time: int) -> None:
    self.capital = capital
    self.rate = rate
    self.time = time
  
  def interest(self, capital: int, rate: float, time: int) -> int:
    return capital*rate*time

p1: Profit = Profit(1000, 0.1, 2)
print(p1.interest(1000, 0.1, 2))

# or

def intrest_cal(calpital: int, rate: float, time: int) -> int:
  return calpital*rate*time


print(intrest_cal(1000, 0.1, 2))

# Convert Temperature

def tem_cal_c_2_f(celcius: float) -> float:
  fharenhite: float= (celcius/5)*9+32
  return fharenhite
print(tem_cal_c_2_f(37))