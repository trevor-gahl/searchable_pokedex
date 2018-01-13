import pandas as pd

###############
## Constants ##
###############

# Printable index values
pokemonName = 1
height = 3
weight = 4
baseExperience = 5

# first dictionary correlates type_id to string of pokemon type, the second does the inverse
typeDict = {1: 'normal', 2: 'fighting', 3: 'flying', 4: 'poison', 5: 'ground', 6: 'rock', 7: 'bug', 8: 'ghost', 9: 'steel',
            10: 'fire', 11: 'water', 12: 'grass', 13: 'electric', 14: 'psychic', 15: 'ice', 16: 'dragon', 17: 'dark', 18: 'fairy'}
typeDictSearch = {'normal': 1, 'fighting': 2, 'flying': 3, 'poison': 4, 'ground': 5, 'rock': 6, 'bug': 7, 'ghost': 8, 'steel': 9,
                  'fire': 10, 'water': 11, 'grass': 12, 'electric': 13, 'psychic': 14, 'ice': 15, 'dragon': 16, 'dark': 17, 'fairy': 18}

# import csv files with pokemon data
pokemon_ds = pd.read_csv(
    "C:/Users/Trevor/Documents/Ryans_Challenges/Pokedex/Pokemon.csv")
pokemontypes_ds = pd.read_csv(
    "C:/Users/Trevor/Documents/Ryans_Challenges/Pokedex/PokemonTypes.csv")

############################
## Search by Pokemon type ##
############################


def searchByType(search_type):
    # initializes dataframes in the desired scope
    global pokemon_ds, pokemontypes_ds

    # initializes the list where final output will be stored
    printList = []

    # creates a sub dataframe consisting of the desired pokemon type
    type_search = (pokemontypes_ds[pokemontypes_ds['type_id'] == search_type])

    # converts the dataframe to a list for easier iteration
    search_id = type_search.pokemon_id.tolist()

    # iterates through the search_id list
    for x in range(len(search_id)):
        # creates a dataframe consisting of the pokemon names correlated to the previous dataframe
        name_search = (pokemon_ds[pokemon_ds['species_id'] == search_id[x]])

        # extends the output list for ever pokemon name of the given type
        printList.extend(name_search.identifier.tolist())

    # prints the final output
    print("\nThe following pokemon are of the desired type")
    for y in range(len(printList)):
        print(printList[y])


############################
## Search by Pokemon name ##
############################

def searchByName(name):
    # initializes preliminary dataframes and constants
    global pokemon_ds, pokemontypes_ds, pokemonName, height, weight, baseExperience

    # searches through the pokemon dataframe for a specific name
    name_search = (pokemon_ds[pokemon_ds['identifier'] == name])

    # grabs the index id and converts it from a series to an int
    search_index_type = int(name_search.species_id)

    # searches through the type dataframe for the pokemon's correlating type(s)
    type_search = (
        pokemontypes_ds[pokemontypes_ds['pokemon_id'] == search_index_type])

    # converts the dataframes to lists and combines
    output = name_search.values.tolist()
    output2 = type_search.type_id.tolist()
    output.append(output2)

    # final output with a check if a pokemon has two types
    print("\nPokemon Name: ")
    print(output[0][pokemonName])
    print("\nPokemon Height: ")
    print(output[0][height])
    print("\nPokemon Weight: ")
    print(output[0][weight])
    print("\nPokemon Base Experience: ")
    print(output[0][baseExperience])
    print("\nPokemon Type 1: ")
    print(typeDict[output[1][0]])
    if len(output2) > 1:
        print("\nPokemon Type 2: ")
        print(typeDict[output[1][1]])


#################
## Main Method ##
#################

def main():
    # basic keyboard menu to select search options
    selection = int(
        input("How would you like to search? (1=Name or 2=Type)\n"))
    if(selection == 1):
        name = input(
            "What name would you like to search for? (Enter as lowercase)\n")
        searchByName(name)
    elif(selection == 2):
        print("\nSearchable options: normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, fairy")
        search_type_str = input("What type would you like to search for?\n")
        search_type_int = typeDictSearch[search_type_str]
        searchByType(search_type_int)
    else:
        print("Invalid selection")


if __name__ == '__main__':
    main()
