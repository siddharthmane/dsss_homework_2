import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generates a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def calculate_result(num1, num2, operator):
    """
    Calculates the result of an arithmetic operation based on the given numbers and operator.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator for the current question
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        # Calculate the correct answer for the current question
        correct_answer = calculate_result(num1, num2, operator)

        # Display the question to the user
        problem_statement = f"\nQuestion: {num1} {operator} {num2}"
        print(problem_statement)

        # Get user input and handle invalid input
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)
                break  # Break out of the loop if input is successfully converted to an integer
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        # Check if the user's answer is correct and update the score
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
