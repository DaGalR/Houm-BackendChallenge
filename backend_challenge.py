import logging
import math

import httpx
from typing import AnyStr, Dict, List, Tuple

# r = httpx.get("https://pokeapi.co/api/v2/pokemon/ditto")

# print(base_url)
# ditto = r.json()
# print(type(ditto))
# response = httpx.get(base_url+'pokemon?limit=1118')
# print(response.json())
# response: Dict = httpx.get(base_url + 'pokemon?limit=1118').json()
# names: List = response['results']
# for i in range(0, 9):
#     print(names[i]['name'])

# a = 'atremover'
# print(a)
# if 'at' in a:
#     a = a.replace('at', '')
#     print(a)

base_url: AnyStr = 'https://pokeapi.co/api/v2/'
Integer = int

logging.basicConfig(filename='houm_challenge_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# raichu_info: Dict = httpx.get(base_url + 'pokemon-species/raichu/').json()
# egg_groups: List = raichu_info['egg_groups']
# print(egg_groups)


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


logger.info(str(first_question()))


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
            if name not in species_checked:
                species_checked.append(name)
                question_answer += 1
            else:
                pass

    return question_answer


logger.info(str(second_question()))


def third_question() -> List:
    max_weigh: Integer = math.inf
    min_weigh: Integer = 0
