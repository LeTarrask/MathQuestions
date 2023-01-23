import random


def ask_question():
    # Generate a random operation
  operation = random.choice(["+", "-", "*", "/"])

# Generate two random numbers under 100
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)
  
  # Restrict divisions to exact numbers
  while operation == '/' and (num2 == 0 or num1 % num2 != 0 or num2 > 10 or num1 / num2 > 10):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 10)

  # Restrict multiplications to numbers lower than 10
  while operation == '*' and (num1 > 10 or num2 > 10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

  # Restrict subtraction so first number is always > second number
  while operation == '-' and num1 < num2:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

  # Ask the question
  question = f"Quanto é {num1} {operation} {num2}?\n"
  answer = input(question)

  # Check the answer
  if operation == "+":
    correct_answer = num1 + num2
  elif operation == "-":
    correct_answer = num1 - num2
  elif operation == "*":
    correct_answer = num1 * num2
  else:
    correct_answer = num1 // num2
  if float(answer) == correct_answer:
    print("Correto!")
  else:
    print(f"Incorreto. A resposta certa é {correct_answer}.")
