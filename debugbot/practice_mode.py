import random

BUGS = [
    {
        "title": "Missing Colon",
        "buggy": "def greet(name)\n    print(f'Hello, {name}!')",
        "fixed": "def greet(name):\n    print(f'Hello, {name}!')",
        "explanation": "Every `def`, `if`, `for`, `while`, `class`, and `try` statement in Python must end with a colon `:`."
    },
    {
        "title": "Undefined Variable",
        "buggy": "x = 10\ny = z + 5\nprint(y)",
        "fixed": "x = 10\nz = 3\ny = z + 5\nprint(y)",
        "explanation": "The variable `z` is used before it is defined. Always define a variable before using it."
    },
    {
        "title": "Wrong Comparison Operator",
        "buggy": "age = 20\nif age = 20:\n    print('You are 20!')",
        "fixed": "age = 20\nif age == 20:\n    print('You are 20!')",
        "explanation": "In conditions, use `==` (comparison) not `=` (assignment)."
    },
    {
        "title": "Indentation Error",
        "buggy": "if True:\nprint('Hello')",
        "fixed": "if True:\n    print('Hello')",
        "explanation": "Code inside an `if` block must be indented (typically 4 spaces)."
    },
    {
        "title": "Mismatched Parentheses",
        "buggy": "print('Hello, World!'",
        "fixed": "print('Hello, World!')",
        "explanation": "Opening parenthesis `(` is not closed. Every `(` must have a matching `)`."
    },
    {
        "title": "Mismatched Quotes",
        "buggy": "print('Hello, World!)",
        "fixed": "print('Hello, World!')",
        "explanation": "The opening quote `'` is not closed with the same type of quote."
    },
    {
        "title": "Divide by Zero",
        "buggy": "numerator = 10\ndenominator = 0\nresult = numerator / denominator\nprint(result)",
        "fixed": "numerator = 10\ndenominator = 2\nresult = numerator / denominator\nprint(result)",
        "explanation": "Division by zero raises a `ZeroDivisionError`. Make sure the divisor is never zero."
    },
    {
        "title": "Wrong Data Type in Operation",
        "buggy": "name = 'Alice'\nage = 25\nresult = name + age\nprint(result)",
        "fixed": "name = 'Alice'\nage = 25\nresult = name + str(age)\nprint(result)",
        "explanation": "You cannot add a string and an integer directly. Convert the integer to a string first using `str()`."
    },
    {
        "title": "Index Out of Range",
        "buggy": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits[3])",
        "fixed": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits[2])",
        "explanation": "Lists are zero-indexed. `fruits[3]` tries to access the 4th element, but there are only 3 elements (indices 0, 1, 2)."
    },
    {
        "title": "Infinite Loop",
        "buggy": "count = 0\nwhile count < 5:\n    print(count)",
        "fixed": "count = 0\nwhile count < 5:\n    print(count)\n    count += 1",
        "explanation": "The `while` loop runs forever because `count` never changes. You need to update the variable inside the loop."
    },
    {
        "title": "Using `is` for Value Comparison",
        "buggy": "a = [1, 2, 3]\nb = [1, 2, 3]\nif a is b:\n    print('Same list!')",
        "fixed": "a = [1, 2, 3]\nb = [1, 2, 3]\nif a == b:\n    print('Same list!')",
        "explanation": "`is` checks if two variables point to the same object in memory, not if they have the same value. Use `==` for value comparison."
    },
    {
        "title": "Wrong Loop Variable",
        "buggy": "for i in range(5):\n    print(x)",
        "fixed": "for i in range(5):\n    print(i)",
        "explanation": "The loop variable is `i`, but you are printing `x` which is undefined."
    },
    {
        "title": "Missing Return Statement",
        "buggy": "def add(a, b):\n    result = a + b",
        "fixed": "def add(a, b):\n    result = a + b\n    return result",
        "explanation": "The function calculates `result` but never returns it. Add a `return` statement."
    },
    {
        "title": "Wrong File Mode",
        "buggy": "f = open('data.txt', 'r')\nf.write('Hello, World!')\nf.close()",
        "fixed": "f = open('data.txt', 'w')\nf.write('Hello, World!')\nf.close()",
        "explanation": "Opening a file in read mode (`'r'`) and then trying to write to it will raise an error. Use `'w'` for writing."
    },
    {
        "title": "Mutable Default Argument",
        "buggy": "def add_item(item, items=[]):\n    items.append(item)\n    return items",
        "fixed": "def add_item(item, items=None):\n    if items is None:\n        items = []\n    items.append(item)\n    return items",
        "explanation": "Using a mutable default argument (like `[]`) in a function can lead to unexpected behavior. Use `None` as the default and create a new list inside the function."
    },
    {
        "title": "Swapped Variables",
        "buggy": "a = 5\nb = 10\na = b\nb = a\nprint(f'a={a}, b={b}')",
        "fixed": "a = 5\nb = 10\na, b = b, a\nprint(f'a={a}, b={b}')",
        "explanation": "When swapping variables, the naive approach `a=b; b=a` doesn't work. Use Python's tuple unpacking: `a, b = b, a`."
    },
    {
        "title": "String Immutability",
        "buggy": "name = 'Alice'\nname[0] = 'B'\nprint(name)",
        "fixed": "name = 'Alice'\nname = 'B' + name[1:]\nprint(name)",
        "explanation": "Strings are immutable in Python. You cannot change a character directly. Create a new string instead."
    },
    {
        "title": "Wrong Method Call",
        "buggy": "numbers = [3, 1, 4, 1, 5]\nresult = numbers.sort()\nprint(result)",
        "fixed": "numbers = [3, 1, 4, 1, 5]\nnumbers.sort()\nprint(numbers)",
        "explanation": "The `sort()` method sorts the list in-place and returns `None`. It doesn't return the sorted list."
    },
    {
        "title": "Using `input` in Condition",
        "buggy": "if input('Enter yes or no: ') == 'yes':\n    print('You said yes!')\nelse:\n    print('You said no!')\n\nprint('This prints regardless')",
        "fixed": "user_input = input('Enter yes or no: ')\nif user_input == 'yes':\n    print('You said yes!')\nelse:\n    print('You said no!')\n\nprint('This prints regardless')",
        "explanation": "The code is correct but may be confusing. Storing the input in a variable first makes it more readable and reusable."
    },
    {
        "title": "Wrong Boolean Check",
        "buggy": "is_valid = True\nif is_valid == True:\n    print('Valid!')",
        "fixed": "is_valid = True\nif is_valid:\n    print('Valid!')",
        "explanation": "You don't need to compare with `== True`. Just use the variable directly in the condition."
    },
]

def get_random_bug():
    return random.choice(BUGS)

def main():
    print("=" * 60)
    print("  DebugBot — Practice Mode")
    print("  Find the bug in the code snippet below!")
    print("  Type your answer or 'hint' for a hint.")
    print("  Type 'answer' to reveal the answer.")
    print("  Type 'exit' to quit.")
    print("=" * 60)

    score = 0
    total = 0

    while True:
        bug = get_random_bug()
        print(f"\n--- Challenge: {bug['title']} ---")
        print(bug["buggy"])
        print()
        user_input = input("What is the bug? ")

        if user_input.strip().lower() == "exit":
            print(f"\nFinal Score: {score}/{total} ({(score/total*100) if total else 0:.0f}%)")
            print("Goodbye!")
            return

        if user_input.strip().lower() == "hint":
            print(f"\nHint: Look carefully at the logic or syntax.")
            user_input = input("Your answer: ")

        if user_input.strip().lower() == "answer":
            print(f"\nAnswer:\n{bug['fixed']}")
            print(f"\nExplanation: {bug['explanation']}")
            total += 1
            continue

        total += 1
        if user_input.strip().lower() in bug["title"].lower() or any(word in user_input.lower() for word in bug["explanation"].lower().split()):
            print("\nCorrect!")
            score += 1
        else:
            print("\nIncorrect.")
            print(f"\nCorrect Answer:\n{bug['fixed']}")
            print(f"\nExplanation: {bug['explanation']}")

        print(f"\nScore: {score}/{total}")

if __name__ == "__main__":
    main()
