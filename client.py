''' 
Good practice to call class same as file name
NOTE if requests is not installed use: pip3 install requests package
'''
import requests

class Client():
    URL="https://pokeapi.co/api/v2"
    
    def __init__(self):
        self._setup()

    ''' This method is internal to the class, not to be called by class consumers, therefore prefix name with 1 single underscore which keeps it protected (NOTE: that double underscore means its private)
    '''
    
    def _setup(self):
        r = requests.get(f"{self.URL}/pokemon")
        self.pokemon = r.json()['results']

'''
This will only execute if this file is directly
if it's called from another file this step won't run
'''
if __name__ == "__main__":
    c = Client()
    print(c.pokemon)



