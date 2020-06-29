import time
import random


def print_pause(message):
    # had to set flush=True or my bash would perform all the sleep
    # commands before printing messages all at once
    print(message, flush=True)
    time.sleep(.2)


def display_intro(antagonist):
    #
    # display opening scenario
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {antagonist} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dagger.")


def fight(items, antagonist):
    #
    # if player does not have sword, they lose
    if("sword" not in items):
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the "
                    f"{antagonist}.")
        print_pause("You have been defeated!")
    # player is equipped with sword and wins
    else:
        print_pause(f"As the {antagonist} moves to attack, you "
                    "unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your "
                    "hand as you brace yourself for the attack.")
        print_pause(f"But the {antagonist} takes one look at your shiny "
                    "new toy and runs away!")
        print_pause(f"You have rid the town of the {antagonist}. "
                    "You are victorious!")


def go_to_cave(items, antagonist):
    #
    # if the player has a dagger, then this is first vist
    if "dagger" in items:
        # display message
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("You walk back out to the field.")
        # replace dagger with sword
        items.remove("dagger")
        items.append("sword")
    # already has sword
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")


def go_to_house(items, antagonist):
    #
    # display house approach messages
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {antagonist}.")
    print_pause(f"Eep! This is the {antagonist}'s house!")
    print_pause(f"The {antagonist} attacks you!")
    #
    # get input from player
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if (choice == "1" or choice == "2"):
            break
    #
    # player chooses to fight, call fight function
    if (choice == "1"):
        fight(items, antagonist)
        # exit function indicating game over
        return True
    #
    # only other option is to run away
    else:
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
    #
    # exit function indicating game not over
    return False


def got_to_field(items, antagonist):
    #
    # initialize end_of_game boolean
    end_of_game = False
    #
    # display house or field options
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    #
    # loop until valid option is entered
    while True:
        print_pause("(Please enter 1 or 2.)")
        choice = input()
        if (choice == "1" or choice == "2"):
            break
    #
    # if user selects house
    if choice == "1":
        end_of_game = go_to_house(items, antagonist)
    # only other option is cave (input validated in house_field function)
    else:
        go_to_cave(items, antagonist)
    #
    # if end_of_game is False, continue
    if (not end_of_game):
        got_to_field(items, antagonist)


def play_game():
    #
    ######################################
    # initialize game (one time actions)
    ######################################
    # (1) select random antagonist from list
    # (2) set initial items. i could accomplish this with an empty list, but
    # i want to get practice with removing and item from a list later
    # (3) display opening scenario just once per game
    ######################################
    #
    antagonist = random.choice(["troll", "wicked fairy", "pirate",
                                "dragon", "gorgon"])
    items = ["dagger"]
    display_intro(antagonist)
    #
    # ask user to select where to search
    got_to_field(items, antagonist)
    #
    # does player wish to play again?
    while True:
        choice = input("Would you like to play again? (y/n)").lower()
        if (choice == "y") or (choice == "n"):
            break
    #
    # if players selects "y", call play_game function;
    # otherwise, display message and end of function
    if (choice == "y"):
        print_pause("Excellent! Restarting the game ...")
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")


#############################################################
# main
#############################################################
play_game()
