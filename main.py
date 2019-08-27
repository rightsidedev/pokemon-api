#!/usr/bin/env python
'''
Written by Mandy Kopelke for CSB2019

Exercise to experiment with restful web api's
Uses the pokemon api: https://pokeapi.co/api/v2/
More info at: https://pokeapi.co/

Displays a user menu allowing user to:
    1.  get a list of existing pokemon names returned by the api
    2.  find a pokemon by name and display ability info, along with a 
        list of other pokemon sharing the same abilities
    3.  Exit the menu
 
'''
from client import Client
import os
import json

'''
Function to clear screen output
Note! that this function may not work on all platforms
'''
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

'''
Function to decode bool_flag from True to Yes, and false to No 
used in the print statement
'''
def decode(bool_flag):
    if bool_flag:
        return('Yes')
    else: # bool_flag = False
        return('No')

'''
Function calling the main menu and processing
'''
def main():

    exit_flag = False
    c = Client()
    
    # create a list of all pokemon names retrieved, making initial validation more efficient
    valid_pokemon = []
    for each in c.pokemon:
        valid_pokemon.append(each["name"])
    
    # Display Main Menu and validate user choice
    while exit_flag == False:
        clear()
        print(f'Pokemon Detail Finder\n')
        print(f'(L)ist names of all Pokemon\n')
        print(f'(F)ind a Pokemon by Name\n')
        print(f'e(X)it\n')
        command = input("Enter choice: ")
        if command.upper() == "X":
            # e(X)it menu option
            exit_flag = True
        elif command.upper() == "L":
            # (L)ist names of all retrieved pokemon option
            print('\n')
            for each in c.pokemon:
                print(f'Pokemon name: {each["name"]}')
            input('\nPress any key to continue...')
        elif command.upper() == "F":
            # (F)ind a pokemon by name option
            pokemon_name = input(f'Enter the Pokemon Name: ')
            # validate pokemon name exists and continue if it does:
            if pokemon_name in valid_pokemon:
                # use get_pokemon_moves method to return abilities information
                pokemon_moves = c.get_pokemon_moves(pokemon_name)
                # count number of abilities returned  
                ability_count = len(pokemon_moves)
                # print abilities summary
                print(f'\n{pokemon_name} has {ability_count} abilities:\n')
                # for each ability print it's name, whether it's hidden and which slot it is in
                for each in range(0,int(ability_count)):
                    print(f'ABILITY Name: {pokemon_moves[each]["ability"]["name"]}; Ability Hidden: {decode(pokemon_moves[each]["is_hidden"])}; Slot: {pokemon_moves[each]["slot"]}\n')
                    # print(json.dumps(pokemon_moves, indent=4)) # data output test
                    # for each ability, display a list of all other pokemon with the same ability
                    # using the get_other_pokemon method
                    other_pokemon_url = pokemon_moves[each]["ability"]["url"]
                    other_pokemon = c.get_other_pokemon(other_pokemon_url)
                    others_count = len(other_pokemon)
                    print(f'These {others_count - 1} pokemon share the same ability:')
                    # build up a string of pokemon names sharing the ability
                    display_others = ""
                    first_loop = True
                    for others in range(0,int(others_count)):
                        if other_pokemon[others]["pokemon"]["name"] != pokemon_name:
                            # do not include the original pokemon name in the list of others with the same ability
                            if first_loop: # don't add comma at start of pokemon names string
                                display_others += other_pokemon[others]["pokemon"]["name"]
                            else:
                                display_others += ", " + other_pokemon[others]["pokemon"]["name"]
                            first_loop = False
                    print(f'{display_others}\n')
                input('\nPress any key to continue...')
            else:
                # invalid pokemon name has been entered, return to main menu
                print("invalid pokemon name")
                input('\nPress any key to continue...')

'''
This will only execute if the main function is being called from main.py - if not it won't run
'''
if __name__ == "__main__":
    main()
