#Calculator

from art import logo

#Add Function
def add(n1, n2):
  return n1 + n2

#Subtract Function
def subtract(n1, n2):
  return n1 - n2

#Multiply Function
def multiply(n1, n2):
  return n1 * n2

#Divide Function
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("Whats the first number?: "))
  
  cont = True
  while cont == True:
    
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("Whats the next number?: "))
  
    answer = operations[operation_symbol](num1, num2)
    print (f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart calculation.: ").lower() == 'y':
      num1 = answer
    else: 
      cont = False
      calculator()

calculator()
    





