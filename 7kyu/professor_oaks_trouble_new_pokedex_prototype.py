"""Professor Oak has just begun learning Python and he wants to program his new Pokedex prototype with it.

For a starting point, he wants to instantiate each scanned Pokemon as an object that is stored at Pokedex's memory. He needs your help!

Your task is to:

Create a PokeScan class that takes in 3 arguments: name, level and pkmntype.

Create a info method for this class that returns some comments about the Pokemon, specifying it's name, an observation about the pkmntype and other about the level.

Keep in mind that he has in his possession just three Pokemons for you to test the scanning function: Squirtle, Charmander and Bulbasaur, of pkmntypes water, fire and grass, respectively.

The info method shall return a string like this: Charmander, a fiery and strong Pokemon.

If the Pokemon level is less than or equal to 20, it's a weak Pokemon. If greater than 20 and less than or equal to 50, it's a fair one. If greater than 50, it's a strong Pokemon.

For the pkmntypes, the observations are wet, fiery and grassy Pokemon, according to each Pokemon type.

IMPORTANT: The correct spelling of "Pokémon" is "Pokémon", with the "é", but to maximize the compatibility of the code I've had to write it as "Pokemon", without the "é". So, in your code, don't use the "é"."""


class PokeScan:
    DESC_TYPE = {"water": "wet", "fire": "fiery", "grass": "grassy"}

    def __init__(self, name, lvl, pkmntype):
        self.name = name
        self.lvl = lvl
        self.pkmntype = pkmntype


    def info(self):
        if self.lvl in range(0, 21):
            power = "weak"
        elif self.lvl in range(21, 51):
            power = "fair"
        else:
            power = "strong"
        return f"{self.name}, a {self.DESC_TYPE[self.pkmntype]} and {power} Pokemon."
