import requests


def get_number_fact(number: int):
    return requests.get(f'http://numbersapi.com/{number}').text


def get_date_fact(dd: int, mm: int):
    return requests.get(f'http://numbersapi.com/{mm}/{dd}').text


def get_cat_fact():
    facts_json = requests.get("https://cat-fact.herokuapp.com/facts").json()
    return facts_json[0]["text"]


# def get_anime_list():
#     data_json = requests.get(
#         'https://anime-facts-rest-api.herokuapp.com/api/v1').json()
#     anime_list = [entry["anime_name"] for entry in data_json["data"]]
#     return anime_list
#
#
# def get_anime_fact(anime):
#     data_json = requests.get(
#         f'https://anime-facts-rest-api.herokuapp.com/api/v1/{anime}')
#     return random.choice(data_json["data"])["fact"]


def get_useless_fact():
    return requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random").json()["text"]
