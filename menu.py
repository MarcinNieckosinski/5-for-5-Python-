from os import system, name
from game import game
from time import sleep


def terminal_clear():
    """
    Clears the terminal.
    """
    if name == 'nt':
        x = system('cls')
    else:
        x = system('clear')


def terminal_exit():
    """
    Shuts down the terminal.
    """
    system("exit")


def menu():
    """
    Main menu function.
    """
    terminal_clear()
    print("========== MENU ==========\n")
    print("1. Play 5for5")
    print("2. Rules of the game")
    print("3. Exit")
    print("\nScript by Marcin Nieckosinski")

    users_choice = input("Choice: ")

    if users_choice == "1":
        terminal_clear()
        game()
        menu()

    elif users_choice == "2":
        terminal_clear()
        print("1. Use input to guess letters that are in the word.")
        print("2. You have 5 chances to guess the word.")
        print("3. If a letter is in drawn word and is in place - you'll see @ sign.")
        print("4. If a letter is in drawn word but is not in place - you'll see * sign. ")
        print("----------------------------------------")
        print("Send \"m\" to get back to menu.")
        if input() == "m":
            menu()

    elif users_choice == "3":
        terminal_exit()

    else:
        print("ERROR! Use only given options - from 1 to 3!")
        sleep(2)
        menu()
