import logging
import httpx
from typing import AnyStr, Dict, List

# Define a Base URL from which the API calls will be made by adding the required endpoint detail
base_url: AnyStr = 'https://pokeapi.co/api/v2/'
# Use Typing's alias to implement int type as "Integer"
Integer = int

# Configure logging to store results from each function
logging.basicConfig(filename='houm_challenge_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Function to answer the first question of the challenge. Receives no parameters and returns int (Integer)
# Retrieves the entire pokemon list from the endpoint 'pokemon'. The limit is set to 1118 as it was found by
# trial in the API. This way of retrieving all pokemon was chosen as it saves the need to request once per
# pokemon, by retrieving all pokemon in one request.
def first_question() -> Integer:

    response: Dict = httpx.get(base_url + 'pokemon?limit=1118').json()
    pokemons_list: List = response['results']
    question_answer: Integer = 0

    for pokemon_dictionary in pokemons_list:
        pokemon_name = pokemon_dictionary['name']
        if 'at' in pokemon_name:
            pokemon_name.replace('at', '')
            if 'a' in pokemon_name:
                question_answer += 1

    return question_answer


# Stores the result of the first question by calling the function "first_question()"
logger.info(str(first_question()))


# Function to answer the second question of the challenge. Receives no parameters and returns int (Integer).
# Takes Raichu's information, where his egg groups are stored, to then count all pokemon belonging to those egg
# groups. A list with pokemon names is used to store the names of Pokemons counted and avoid duplicates.
def second_question() -> Integer:
    raichu_info: Dict = httpx.get(base_url + 'pokemon-species/raichu/').json()
    egg_groups: List = raichu_info['egg_groups']
    question_answer: Integer = 0
    species_checked: List = []

    for egg_group in egg_groups:
        group_data: Dict = httpx.get(egg_group['url']).json()
        pokemon_species: List = group_data['pokemon_species']

        for species in pokemon_species:
            name = species['name']
            # Ensures duplicates are not counted by checking if a Pokemon has not already been counted
            if name not in species_checked:
                species_checked.append(name)
                question_answer += 1
            else:
                pass

    return question_answer


# Stores the result of the first question by calling the function "second_question()"
logger.info(str(second_question()))


# Function to answer the third question of the challenge. Receives no parameters and returns a list.
# Retrieves all Pokemon from Generation 1 and then checks if their 'id' is less than or equal to 151.
# Then checks if the Pokemon's type(s) include 'fighting'. If that's the case, it stores the Pokemon's
# weight in a list, to which ma and min functions are applied to return the desired answer.
def third_question() -> List:
    weight_list: List = []
    gen_i_information: Dict = httpx.get(base_url + 'generation/1/').json()
    pokemon_gen_i: List = gen_i_information['pokemon_species']

    for pokemon in pokemon_gen_i:
        pokemon_url = pokemon['url']
        pokemon_name = pokemon['name']
        split_url = pokemon_url.split('species/')
        pokemon_index = int(split_url[1].replace('/', ''))

        if pokemon_index < 152:
            pokemon_info = httpx.get(base_url + 'pokemon/' + pokemon_name + '/').json()
            pokemon_types = pokemon_info['types']

            for info_type in pokemon_types:
                type_name = info_type['type']['name']

                if type_name == 'fighting':
                    pokemon_weight = pokemon_info['weight']
                    weight_list.append(pokemon_weight)

    return [max(weight_list), min(weight_list)]


# Stores the result of the first question by calling the function "third_question()"
logger.info(str(third_question()))
