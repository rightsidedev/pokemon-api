'''
Written by Mandy Kopelke for CSB2019

Exercise to experiment with restful web api's
Uses the pokemon api: https://pokeapi.co/api/v2/
More info at: https://pokeapi.co/

This client module defines the classes and methods used
This module is referenced from the main.py controlling program
 

Good practice to call class same as file name
NOTE if requests is not installed use: pip3 install requests package

# ?limit=964 added onto URL to get all pokemon
'''
import requests

MAX_POKEMON = 20

class Client():
    URL="https://pokeapi.co/api/v2"
    
    def __init__(self):
        self.pokemon = self._get_list_of_pokemon(MAX_POKEMON)

    ''' 
    This method is internal to the class, not to be called by class consumers, therefore prefix name with 1 single underscore which keeps it protected (NOTE: that double underscore means its private)
    This method gets a list of all Pokemon, limited by MAX_POKEMON
    '''
    def _get_list_of_pokemon(self, limit):
        r = requests.get(f"{self.URL}/pokemon?limit={limit}")
        return r.json()['results']

    '''
    This method gets a list of abilities by pokemon name
    '''
    def get_pokemon_moves(self, pokemon_name):
        moves = requests.get(f"{self.URL}/pokemon/{pokemon_name}")
        return moves.json()['abilities']

    ''' 
    This method gets  alist of pokemon that have the same ability
    '''
    def get_other_pokemon(self, ability_url):
        other_pokemon = requests.get(f"{ability_url}")
        return other_pokemon.json()['pokemon']
    
'''
This will only execute if this file is directly
if it's called from another file this step won't run
'''
if __name__ == "__main__":
    c = Client()
    print(c.pokemon)



