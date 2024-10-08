# Introduce the player and give them options
print("Welcome to Toontown Web Adventure!")
print("I'm Anthony, the creator of this project.")
print("Thank you and I hope you enjoy!")
input("Press Enter to continue...")

print("\nACT ONE: TOONTORIAL")

playerName = input("\nHello! Toontorial Tom here, what might your name be?\n")

print("\nWonderful! Welcome %s!" % (playerName))
print("And what might your species be?")
playerSpecies = input("Options: Bear, Cat, Crocodile, Deer, Dog, Duck, Horse, Monkey, Mouse, Pig, Rabbit.\n")

print("\nAhh, so you are that %s! My associates have talked of you, %s the %s." % (playerName, playerName, playerSpecies))
input("Press Enter to continue...")

print("\nYIKES!!!! THERE'S A FLUNKY COMING INSIDE!")
print("\nQuickly, pick your preferred gag tracks!")
print("Your options include: Trap, Lure, Sound, Throw, Squirt, Drop.")
print("Do you need any information on these tracks or have you made your mind?")

track_1 = input("Enter 'Yes' for more, or type your first preferred track!\n")

if track_1 == "Yes":
    info = input("Which track do you want to know more about?\n")
# Trap
    if info == "Trap":
        print("Trap is a gag track with perfect accuracy, but you need lure to activate it! There is high damage, but also a long set-up with the need for lure.")
        input("Press Enter to continue...")
        info = input("Would you like more information on any other tracks?")
        if info == "No":
            pass
        if info == "Yes":
                info = input("Which track do you want to know more about?")
# Lure
    if info == "Lure":
        print("Lure is gag track that does no damage, but it stuns the cogs! You get a 50% knockback bonus on Throw and Squirt, and can activate Trap!")
        input("Press Enter to continue...")
        info = input("Would you like more information on any other tracks?")
        if info == "No":
            pass
        if info == "Yes":
                info = input("Which track do you want to know more about?")
# Sound
    if info == "Sound":
        print("Sound is a gag track with high accuracy, comprised of attacks that hit all Cogs at once! P.S. Don't use this on lured cogs!!!!")
        input("Press Enter to continue...")
        info = input("Would you like more information on any other tracks?")
        if info == "No":
            pass
        if info == "Yes":
                info = input("Which track do you want to know more about?")
# Throw
    if info == "Throw":
        print("Throw is gag track that has medium accuracy, while packing a punch! Pairs nicely with lure.")
        input("Press Enter to continue...")
        info = input("Would you like more information on any other tracks?")
        if info == "No":
            pass
        if info == "Yes":
                info = input("Which track do you want to know more about?")
# Squirt
    if info == "Squirt":
        print("Squirt is a gag track that has high accuracy, while doing solid amounts! Pairs nicely with lure.")
        input("Press Enter to continue...")
        info = input("Would you like more information on any other tracks?")
        if info == "No":
            pass
        if info == "Yes":
                info = input("Which track do you want to know more about?")
# Drop
    if info == "Drop":
        print("Drop has low accuracy, but it is the second most powerufl track! Just make sure you don't use this on lured cogs.")
        input("Press Enter to continue...")
        info = input("Would you like more information on any other tracks?")
        if info == "No":
            pass
        if info == "Yes":
                info = input("Which track do you want to know more about?")
elif track_1 == {"Trap, Lure, Sound, Throw, Squirt, Drop"}:
    pass
track_2 = input("Now pick your second track!\n")

print("\n%s and %s! Excellent choices, I must say." % (track_1, track_2))
print("I can actually take care of this Flunky here, so go along to the Playground!")
print("\n*Toontorial Tom throws a Birthday Cake at the Level 1 Flunky.*")
print("\nGood luck and goodbye! You will do great things, I am sure.")

print("\n ACT ONE: TOONTORIAL - COMPLETE")
input("Press Enter to continue...")


