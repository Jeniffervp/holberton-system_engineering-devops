#!/usr/bin/python3
""" export to json file """
import json
from requests import get
from sys import argv

if __name__ == "__main__":

    to_do = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(argv[1])).json()
    usr = get('https://jsonplaceholder.typicode.com/users/{}'
              .format(argv[1])).json()

    with open('{}.json'.format(argv[1]), 'w') as my_json:

        data = {}
        id_u = usr.get('id')
        data[id_u] = []

        for a in to_do:
            data_2 = a.get("title"), a.get("completed"), usr.get("username")
            data[id_u].append({
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": usr.get("username")})

        json.dump(data, my_json)
