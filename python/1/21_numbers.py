def nearestMultiples(num):
    # finds nearest multiple of 4 greater than num
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose1():
    # prints losing message and exits game
    print("\nYou loss!")
    print("Better Luck next Time")
    exit(0)


def checks(xyz):
    # checks if numbers are consecutive
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i += 1
    return True


def start1():
    xyz = []
    last = 0

    print("Enter 'F' to take the first chance")
    print("Enter 'S' to take the second chance")
    chances = input("> ").upper()

    # COMPUTER PLAYS FIRST IF PLAYER CHOOSES SECOND
    if chances == "S":
        print("\nComputer's Turn:")
        xyz.append(1)
        print("Numbers:", xyz)
        last = 1

    while True:
        # PLAYER TURN
        print("\nYour Turn")
        inp = int(input("How many numbers do you wish to enter? (1-3)\n> "))

        if inp < 1 or inp > 3:
            print("Wrong input")
            lose1()

        print("Enter your numbers:")
        for _ in range(inp):
            xyz.append(int(input("> ")))

        if not checks(xyz):
            print("Numbers are not consecutive")
            lose1()

        last = xyz[-1]

        if last >= 21:
            lose1()

        # COMPUTER TURN
        near = nearestMultiples(last)
        comp = near - last

        if comp > 3:
            comp = 3

        print("\nComputer's Turn:")
        for i in range(1, comp + 1):
            xyz.append(last + i)

        print("Numbers:", xyz)
        last = xyz[-1]

        if last >= 21:
            print("\nCONGRATULATIONS!!!")
            print("YOU WON!")
            exit(0)


game = True
while game:
    print("\nPlayer 2 is Computer.")
    ans = input("Do you want to play the 21 number game? (Yes / No)\n> ")

    if ans.lower() == 'yes':
        start1()
    else:
        nex = input("Do you want to quit the game? (Yes / No)\n> ")

        if nex.lower() == "yes":
            print("You are quitting the game...")
            exit(0)
        elif nex.lower() == "no":
            print("Continuing...")
        else:
            print("Wrong choice")
