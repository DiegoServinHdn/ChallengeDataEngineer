import requests
from requests import Request


def order_by_key(items: list, key: str) -> list:
    items.sort(key=lambda item: item[key])

def get_not_null_key_values(items: list, key: str) -> list:
    return [i for i in items if i.get(key) is not None]


def connect(connection_url: str) -> Request:
    return requests.get(connection_url)
    
def number_of_answers(data: dict) -> dict:
    """
    counts the number of answered and not answered items

    Parameters
    ----------
    data: dict
        data with the values to count
    

    Returns
    -------
    dict
        a dictionary with 'answered' and 'not answered' keys
    """
    # get items with 'is_answered' key
    items = get_not_null_key_values(data['items'], 'is_answered')
    # check if number of items is at least 1
    if len(items) <= 0:
        return {}
    # initialize keys
    answers = {'answered': 0, 'not answered': 0}
    # look for answered and not answered items
    for i in items:
        if i.get('is_answered'):
            answers['answered'] += 1
        else:
            answers['not answered'] += 1
    return answers

def answer_with_less_views(data: dict) -> dict:
    # get items with 'view_count' key
    items = get_not_null_key_values(data['items'], 'view_count')
    # check if number of items is at least 1
    if len(items) <= 0:
        return {}
    # sort items by view count
    order_by_key(items, 'view_count')
    return items[0]

def oldest_and_latest_answers(data: dict) -> dict:
    # get items with 'creation_date' key
    items = get_not_null_key_values(data['items'], 'creation_date')
    # check if number of items is at least 1
    if len(items) <= 0:
        return {}
    # sort items by creation date
    order_by_key(items, 'creation_date')
    return {'oldest': items[0], 'latest': items[-1]}


def owner_with_best_reputation(data: dict) -> dict:
    # get items with owner and reputation key
    items = [i for i in data['items'] if i.get('owner')]
    items = [i for i in items if i['owner'].get('reputation')]
    # check if number of items is at least 1
    if len(items) <= 0:
        return {}
    # sort items by reputation
    items.sort(key=lambda item: item['owner']['reputation'])
    return items[-1]


if __name__ == '__main__':
    connection_url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    data = connect(connection_url).json()

    
    # with open(r'C:\Users\robin\Desktop\Public repos\ChallengeDataEngineer\first_challenge\tmp\tmp_response.json', 'r') as file:
    #     data = json.load(file)

    padding = 2

    # 2
    print("2. Obtener el número de respuestas contestadas y no contestadas:\n")
    print(number_of_answers(data))
    print('\n' * padding)
    # 3
    print("3. Obtener la respuesta con menor número de vistas:\n")
    print(answer_with_less_views(data))
    print('\n' * padding)
    # 4
    print("4. Obtener la respuesta más vieja y más actual:\n")
    print(oldest_and_latest_answers(data))
    print('\n' * padding)
    # 5
    print("5. Obtener la respuesta del owner que tenga una mayor reputación:\n")
    print(owner_with_best_reputation(data))

