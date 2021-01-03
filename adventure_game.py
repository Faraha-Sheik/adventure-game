import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def fight(items, option):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is the dark cave")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger\n")


def field(items, option):
    print_pause("Enter 1 to knock on the door of the game")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    while True:
        route = input("(Please enter 1 or 2.)\n")
        if route == "1":
            house(items, option)
            break
        elif route == "2":
            cave(items, option)
            break


def house(items, option):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                "and out steps a " + option + ".")
    print_pause("Eep! This is the " + option + "'s house!")
    print_pause("The " + option + " attacks you!\n")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        answer = input("Would you like to (1) fight or (2) run away?")
        if answer == "1":
            if "sword" in items:
                print_pause("As the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + option + " takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + option + ". "
                            "You are victorious!\n")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            + option + ".")
                print_pause("You have been defeated!\n")
            play_again()
            break
        elif answer == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.\n")
            field(items, option)
            break


def cave(items, option):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("You walk back to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
    field(items, option)


def play_again():
    print_pause("GAME OVER")
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game ...\n")
        main()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.\n")
    else:
        play_again()


def main():
    items = []
    option = random.choice(["wicked fairy", "dragon", "gorgon",
                            "pirate", "troll"])
    fight(items, option)
    field(items, option)


main()
