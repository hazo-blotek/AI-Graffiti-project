import random
import time
from colorama import Fore, Style, init
import pyfiglet

# Initialize Colorama
init(autoreset=True)

# List of colors to randomly apply to each line
colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

# List of graffiti-style fonts
graffiti_fonts = [
    "slant", "3-d", "banner3-D", "epic", "isometric1", "graffiti",
    "colossal", "doom", "block"
]

def generate_graffiti(text):
    font = random.choice(graffiti_fonts)
    art = pyfiglet.figlet_format(text, font=font)
    lines = art.split("\n")

    for line in lines:
        color = random.choice(colors)
        print(color + line)
        time.sleep(0.05)  # Delay for visual effect

    # Add some digital paint splashes
    paint = "".join(random.choice([" ", "*", "-", "/", ".", "#"]) for _ in range(50))
    print(Fore.LIGHTBLACK_EX + paint)
    time.sleep(0.2)

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\nWelcome to the AI Graffiti Wall")
    print(Fore.LIGHTBLUE_EX + "Type anything and watch it become digital art!\n")

    while True:
        user_input = input(Fore.LIGHTWHITE_EX + "What do you want to graffiti? (or type 'exit'): ")
        if user_input.lower() == "exit":
            print(Fore.LIGHTGREEN_EX + "Goodbye!")
            break
        else:
            generate_graffiti(user_input)
            print("\n")
