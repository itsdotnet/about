import os
import time
import pyfiglet
import signal

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_big_text(text):
    custom_fig = pyfiglet.Figlet(font='big')
    print(custom_fig.renderText(text))

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def ctrl_c_handler(signum, frame):
    clear_screen()
    animate_text("Thank you for wasting your time!")
    exit()

def main_menu():
    clear_screen()
    print_big_text("Iskandar")
    print("\n1. Know my birthday")
    print("2. Tell me more about yourself")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            animate_text("Your birthday is on October 13, 2006.")
            break
        elif choice == '2':
            animate_text("What will you gonna do.")
            break
        elif choice == '3':
            animate_text("Exiting...")
            time.sleep(1)
            clear_screen()
            exit()
        else:
            animate_text("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ctrl_c_handler)
    while True:
        main_menu()
