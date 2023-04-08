import time

def print_mario():
    print("             __")
    print("            /  \\")
    print("           / .. \\")
    print("          /  __  \\")
    print("         /_/  \\_\\")
    print("        /_/_|\\_\\")
    print("       |___||___|")
    print("       |___||___|")
    print("      /     |     \\")
    print("     /      |      \\")
    print("    /_______|_______\\")
    print("    \\       |       /")
    print("     \\      |      /")
    print("      \\_____|_____/")

print("Welcome to Simple Mario Game!")
time.sleep(2)

print("Mario is stuck in a forest and he needs to get to the castle.")
time.sleep(2)

print("Help Mario avoid obstacles and get to the castle.")
time.sleep(2)

print("Press 'r' to run.")
choice = input("> ")

if choice == 'r':
    print("Mario starts running!")
    time.sleep(1)
    print_mario()
    time.sleep(1)
    print("Mario jumps over a tree!")
    time.sleep(1)
    print_mario()
    time.sleep(1)
    print("Mario avoids a mushroom!")
    time.sleep(1)
    print_mario()
    time.sleep(1)
    print("Mario jumps over a gap!")
    time.sleep(1)
    print_mario()
    time.sleep(1)
    print("Mario reaches the castle!")
    time.sleep(1)
    print("Congratulations, you won!")
else:
    print("Invalid choice. Game over!")
