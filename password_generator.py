import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special


    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_character = random.choice(characters)
        pwd += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd

def generate_passphrase(num_words, separator="-", capitalize=False):
    word_list = [
        "correct", "horse", "shoe", "foot", "house", "tree", "sword", "shield", "mice", "disc", "wear",
        "long", "store", "chain", "food", "place", "day", "wake", "seize", "mail", "fail", "life", "bake",
        "fry", "deck", "trash", "news", "turbo", "torn", "take", "room", "ball", "sack", "egg", "splat",
        "home",
    ]

    if num_words < 1:
        print("Word count must be at least 1.")
        return

    chosen_words = [random.choice(word_list)for _ in range(num_words)]
    if capitalize:
        chosen_words = [word.capitalize() for word in chosen_words]
    return separator.join(chosen_words)

print("***** Password Generator *****")
choice = input("Do you want to generate a [P]assword or Passphras[E]?").upper()

if choice == "P":
    min_length = int(input("\nInput the minimum length of your password."))
    has_number = input("\nDo you want your password to include numbers (y/n)?").lower() == "y"
    has_special = input("\nDo you want your password to include special characters (y/n)?").lower() == "y"
    pwd = generate_password(min_length, has_number, has_special)
    print(f"Your password is: {pwd}")

elif choice == "E":
    num_words = int(input("\nInput the amount of words you would like to have in your passphrase."))
    sep = input("\nWhat separator character would you like to use? (ex. -, _, @)")
    cap = input("\nDo you want to capitalize the words? (y/n)").lower() == "y"

    pphrase = generate_passphrase(num_words, separator=sep, capitalize=cap)
    print(f"Your passphrase is: {pphrase}")

input("Press Enter to exit...")
