#defining the entire game program as a funtion, to call it whenever the user wants to restart the game.

def start():
    
    #Pick a random animal.

    mammals = ["Cat", "Cow", "Camel", "Cheetah"]
    snakes = ["Anaconda", "Python", "Cobra"]
    fishes = ["Catfish", "Goldfish", "Shark"]

    animals = [mammals, snakes, fishes]

    import random
    
    category_num = random.randint(0, 2)
    
    if category_num == 0:
        num_of_animals = len(mammals)
    elif category_num == 1:
        num_of_animals = len(snakes)
    elif category_num == 2:
        num_of_animals = len(fishes)

    animal_num = random.randint(0, num_of_animals - 1)

    animal = animals[category_num][animal_num].lower()
    
    #Generate blanks with few words to output, for user to fill.
    
    length_of_animal = len(animal)

    blanks_list = []
    lenght_of_blanks_list = len(blanks_list)

    while lenght_of_blanks_list < length_of_animal:
        blanks_list.append("_")
        lenght_of_blanks_list += 1

    blanks_list[1] = animal[1]
    blanks_list[-1] = animal[-1]

    #defining hint.

    if category_num == 0:
        hint = "mammal! 🐾"
    if category_num == 1:
        hint = "snake! 🐍"
    if category_num == 2:
        hint = "fish! 🐠"

    #Converting the blanks to string.

    blanks_str = ""

    for char in blanks_list:
        blanks_str += char

    #defining the starting of the game as a function, to call it when the user inputs to start the game.

    def game_start():

        print(f"\nAlright! Guess what animal is: {blanks_str}")
        print(f"Hint: It is a {hint}")

        def prompt():

            user_answer = input("What do you think? 🤔\nEnter your answer here: ").lower()

            if user_answer == animal:
                print(f"Congratulations! you guessed it right! the animal is {animal}.")
                user_replay = input('"Re" to restart the game or "Q" to quit the game.\n').lower()
                if user_replay == "re":
                    start()
                else:
                    print("Invalid input")

            else:
                print("Oh, Thats wrong anwer, keep trying you'll get it!")
                user_retry = input('Enter "R" to retry the animal, "Re" to restart the game or "Q" to quit the game.\n').lower()
                if user_retry == "r":
                    prompt()
                elif user_retry == "re":
                    start()
                elif user_retry == "q":
                    input("Enter anything to quit the game\n")
                else:
                    print("invalid input")
        
        prompt()

    #Building the starting screen prompts and statements for user.

    print("Welcome to guess the animal game!")
    print("In this game you'll be given a random animal name with blanks to guess the animal.")
    user_input_start = input('Type "S" to start the game or "Q" to quit the game.\n').lower()

    if user_input_start == "s":
        game_start()
    elif user_input_start == "q":
        input("Enter anything to close the program")
    else:
        print("Invalid input")

#callig the main game program "start()" function to start the game program.

start()