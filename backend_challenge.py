import logging
import httpx
from typing import AnyStr, NewType, Dict, List

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

