#!/usr/bin/python3
""" export to json file all the users info"""
import json
from requests import get

if __name__ == "__main__":

    to_do = get('https://jsonplaceholder.typicode.com/todos/').json()
    usr = get('https://jsonplaceholder.typicode.com/users/').json()

    with open('todo_all_employees.json', 'w') as my_json:

        data = {}

        for u in usr:
            data[u.get('id')] = []
            for a in to_do:
                if u.get('id') == a.get("userId"):
                    data[u.get('id')].append({
                        "task": a.get("title"),
                        "completed": a.get("completed"),
                        "username": u.get("username")})
        json.dump(data, my_json)
