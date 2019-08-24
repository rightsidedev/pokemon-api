#!/usr/bin/env python

from client import Client

def main():

    exit_flag = False
    c = Client()

    while exit_flag == False:
        command = input("Enter command: ")
        if command == "hello":
            print("Hello world")
        elif command == "exit":
            exit_flag = True
        elif command == "pokemon":
            n_pokemon = len(c.pokemon)
            print(f'There are {n_pokemon} pokemon')

'''
This will only execute if the main function is being called from main.py - if not it won't run
'''
if __name__ == "__main__":
    main()
