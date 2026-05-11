from time import sleep
from random import randint

# ---------------------------------------------------------
# MINI GAME MENU
# ---------------------------------------------------------

def MiniGameMenu():
    choice = 0

    while choice < 1 or choice > 3:
        try:
            print("1) See Rules\n2) Play Game\n3) Return to Main Menu\n")
            choice = int(input("Please choose from the menu: "))
            if choice < 1 or choice > 3:
                print("Please enter only 1, 2, or 3\n")  # <-- FIX: menu validation
        except ValueError:
            print("\nMust type a number\n")  # <-- FIX: numeric validation

    return choice   # <-- FIX: return correct variable


# ---------------------------------------------------------
# DICE SIDES (ASCII ART)
# ---------------------------------------------------------

def sideOne():
    print(" ___________")
    print("|           |")
    print("|     *     |")
    print("|           |")
    print("|___________|")

def sideTwo():
    print(" ___________")
    print("|   *       |")
    print("|           |")
    print("|       *   |")
    print("|___________|")

def sideThree():
    print(" ___________")
    print("|   *       |")
    print("|     *     |")
    print("|       *   |")
    print("|___________|")

def sideFour():
    print(" ___________")
    print("| *       * |")
    print("|           |")
    print("| *       * |")
    print("|___________|")

def sideFive():
    print(" ___________")
    print("| *       * |")
    print("|     *     |")
    print("| *       * |")
    print("|___________|")

def sideSix():
    print(" ___________")
    print("| *       * |")
    print("| *       * |")
    print("| *       * |")
    print("|___________|")


# ---------------------------------------------------------
# DICE DISPLAY FUNCTION
# ---------------------------------------------------------

def diceDisplay():
    diceNum = randint(1, 6)  # <-- FIX: generate random 1–6

    if diceNum == 1:
        sideOne()
    elif diceNum == 2:
        sideTwo()
    elif diceNum == 3:
        sideThree()
    elif diceNum == 4:
        sideFour()
    elif diceNum == 5:
        sideFive()
    elif diceNum == 6:
        sideSix()

    return diceNum   # <-- FIX: return dice value


# ---------------------------------------------------------
# GUESS THE ROLL GAME
# ---------------------------------------------------------

def GuessTheRoll(name):
    ROUNDS = 5

    playerGuess = diceTotal = diceOne = diceTwo = 0
    score = compScore = 0
    menuSelection = 0

    print("\n\nWelcome to my dice game!\n")
    sleep(.5)

    while menuSelection != 3:
        menuSelection = MiniGameMenu()   # <-- FIX: correct function name

        if menuSelection == 1:
            print("\n" + "*" * 40)
            print("RULES:")
            print("You guess the total of 2 dice.")
            print("If you're right, you get a point.")
            print("If you're wrong, the computer gets a point.")
            print("Highest score after 5 rounds wins.")
            print("*" * 40)

        elif menuSelection == 2:
            score = compScore = 0   # <-- FIX: reset scores each game

            for i in range(ROUNDS):
                print("\n" + "*" * 40)
                print(f"ROUND {i+1}".center(40))
                print("*" * 40)

                playerGuess = 0  # <-- FIX: reset guess each round

                while playerGuess < 2 or playerGuess > 12:
                    try:
                        playerGuess = int(input("Guess a sum (2–12): "))
                        if playerGuess < 2 or playerGuess > 12:
                            print("Guess must be between 2 and 12.")
                    except ValueError:
                        print("Must type a number.")

                sleep(1)
                print("\nRolling first die...")
                diceOne = diceDisplay()

                sleep(1)
                print("\nRolling second die...")
                diceTwo = diceDisplay()

                diceTotal = diceOne + diceTwo
                print(f"\nThe dice total is {diceTotal}")

                if playerGuess == diceTotal:
                    print(f"\nCorrect! You guessed {playerGuess}.")
                    score += 1
                else:
                    print(f"\nIncorrect. You guessed {playerGuess}.")
                    compScore += 1

                print(f"\nScore:\n{name}: {score}\nComputer: {compScore}")

            print("\n" + "*" * 40)
            if score > compScore:
                print(f"{name} wins the game!")
            elif compScore > score:
                print("Computer wins the game!")
            else:
                print("It's a tie!")
            print("*" * 40)

        else:
            print(f"\nReturning to main menu, {name}...\n")


# ---------------------------------------------------------
# HIGH CARD WINS GAME
# ---------------------------------------------------------

def HighCardWins(name):

    ACE = """*- - -*
| ♣   |
|  A  |
|   ♣ |
*- - -*"""

    KING = """*- - -*
| ♣   |
|  K  |
|   ♣ |
*- - -*"""

    QUEEN = """*- - -*
| ♣   |
|  Q  |
|   ♣ |
*- - -*"""

    JACK = """*- - -*
| ♣   |
|  J  |
|   ♣ |
*- - -*"""

    TEN = """*- - -*
| ♣   |
| 10  |
|   ♣ |
*- - -*"""

    NINE = """*- - -*
| ♣   |
|  9  |
|   ♣ |
*- - -*"""

    EIGHT = """*- - -*
| ♣   |
|  8  |
|   ♣ |
*- - -*"""

    SEVEN = """*- - -*
| ♣   |
|  7  |
|   ♣ |
*- - -*"""

    SIX = """*- - -*
| ♣   |
|  6  |
|   ♣ |
*- - -*"""

    FIVE = """*- - -*
| ♣   |
|  5  |
|   ♣ |
*- - -*"""

    FOUR = """*- - -*
| ♣   |
|  4  |
|   ♣ |
*- - -*"""

    THREE = """*- - -*
| ♣   |
|  3  |
|   ♣ |
*- - -*"""

    TWO = """*- - -*
| ♣   |
|  2  |
|   ♣ |
*- - -*"""

    cardList = [TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE]

    menuSelection = 0
    playerScore = 0
    compScore = 0

    print("\n\nWelcome to HIGH CARD WINS!\n")

    while menuSelection != 3:
        print("1) See Rules\n2) Play Game\n3) Return to Main Menu\n")
        try:
            menuSelection = int(input("Choose from the menu: "))
        except:
            print("Must type a number.\n")
            continue

        if menuSelection == 1:
            print("\n" + "*" * 40)
            print("RULES:")
            print("You draw a card, then the computer draws a card.")
            print("Highest card wins the round.")
            print("First to 5 points wins the game.")
            print("*" * 40)

        elif menuSelection == 2:
            playerScore = 0
            compScore = 0
            roundNum = 0

            while playerScore < 5 and compScore < 5:
                roundNum += 1
                print("\n" + "*" * 40)
                print(f"ROUND {roundNum}".center(40))
                print("*" * 40)

                playerCard = randint(2, 14)   # <-- FIX: 2–14 for 2–Ace
                compCard = randint(2, 14)

                print("\nYour card:")
                print(cardList[playerCard - 2])  # <-- FIX: index offset

                sleep(.5)

                print("\nComputer's card:")
                print(cardList[compCard - 2])

                if playerCard > compCard:
                    playerScore += 1
                    print(f"\n{name} wins the round!")
                elif compCard > playerCard:
                    compScore += 1
                    print("\nComputer wins the round!")
                else:
                    print("\nIt's a tie! No points awarded.")

                print(f"\nScore:\n{name}: {playerScore}\nComputer: {compScore}")

            print("\n" + "*" * 40)
            if playerScore == 5:
                print(f"{name} wins the game!")
            else:
                print("Computer wins the game!")
            print("*" * 40)

        elif menuSelection == 3:
            print(f"\nReturning to main menu, {name}...\n")
        else:
            print("Please choose only 1–3.\n")


# ---------------------------------------------------------
# TRIVIA GAME
# ---------------------------------------------------------

def TriviaGame(name):

    Animals = [
        ["What animal runs the fastest?", ["Cheetah", "Gazelle", "Pronghorn", "Zebra"], "A"],
        ["Which animal is the largest?", ["Elephant", "Hippo", "Giraffe", "Rhino"], "A"],
        ["Which animal can fly?", ["Lion", "Eagle", "Shark", "Snake"], "B"],
        ["Which animal lives in water?", ["Dog", "Cat", "Whale", "Monkey"], "C"],
        ["Which animal barks?", ["Cat", "Dog", "Cow", "Horse"], "B"]
    ]

    Cars = [
        ["Which brand is known for the Mustang?", ["Ford", "Toyota", "Honda", "BMW"], "A"],
        ["Which car is electric?", ["Camry", "Civic", "Model S", "Accord"], "C"],
        ["Which brand is German?", ["Ford", "Chevy", "BMW", "Kia"], "C"],
        ["Which is a luxury brand?", ["Honda", "Lexus", "Nissan", "Hyundai"], "B"],
        ["Which is a sports car?", ["Corvette", "Prius", "Minivan", "Truck"], "A"]
    ]

    People = [
        ["Who is the CEO of Amazon?", ["Jeff Bezos", "Elon Musk", "Bill Gates", "Mark Cuban"], "A"],
        ["Who is the wealthiest actor?", ["The Rock", "Tom Cruise", "Tyler Perry", "Will Smith"], "C"],
        ["Who teaches Python best?", ["Sammy", "Bob", "Joe", "Mike"], "A"],
        ["Who is famous for boxing?", ["Jordan", "Ali", "Messi", "Brady"], "B"],
        ["Who is known for Tesla?", ["Bezos", "Musk", "Jobs", "Cuban"], "B"]
    ]

    score = 0
    menuSelection = 0

    print("\n\nWelcome to Trivia!\n")

    while menuSelection != 4:
        print("1) Animals\n2) Cars\n3) People\n4) Return to Main Menu\n")

        try:
            menuSelection = int(input("Choose a category: "))
        except:
            print("Must type a number.\n")
            continue

        if menuSelection == 4:
            print(f"\nReturning to main menu, {name}...\n")
            break

        if menuSelection == 1:
            category = Animals
        elif menuSelection == 2:
            category = Cars
        elif menuSelection == 3:
            category = People
        else:
            print("Choose only 1–4.\n")
            continue

        score = 0  # <-- FIX: reset score per category

        for q in category:
            print("\n" + "*" * 40)
            print(q[0])
            print("A)", q[1][0])
            print("B)", q[1][1])
            print("C)", q[1][2])
            print("D)", q[1][3])
            print("*" * 40)

            answer = input("Your answer (A-D): ").upper()

            if answer == q[2]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        print(f"\nYou scored {score} out of 5!\n")


# ---------------------------------------------------------
# MATH GAME
# ---------------------------------------------------------

def MathGame(name):
    score = 0

    print("\n\nWelcome to the Math Game!\n")

    for i in range(5):  # <-- FIX: 5 questions
        num1 = randint(1, 10)
        num2 = randint(1, 10)

        print(f"\nQuestion {i+1}: What is {num1} + {num2}?")
        try:
            answer = int(input("Your answer: "))
        except:
            print("Must type a number.")
            continue

        if answer == num1 + num2:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer was {num1 + num2}.")

    print(f"\n{name}, your final score is {score}/5!\n")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():
    name = ""

    print("SAMMY'S GAME ROOM".center(40, "?"))
    name = input("\nPlease enter your name: ").strip().capitalize()

    menuChoice = ""

    while menuChoice != "5":
        print("\n1) Guess The Roll\n2) High Card Wins\n3) Trivia Game\n4) Math Game\n5) Exit")
        menuChoice = input("Choose from the menu: ")

        if menuChoice == "1":
            GuessTheRoll(name)
        elif menuChoice == "2":
            HighCardWins(name)
        elif menuChoice == "3":
            TriviaGame(name)
        elif menuChoice == "4":
            MathGame(name)
        elif menuChoice == "5":
            print(f"\nThanks for playing, {name}!\n")
        else:
            print("Please choose only 1–5.\n")


# Start program
main()

