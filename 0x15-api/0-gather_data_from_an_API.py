#!/usr/bin/python3
""" return information about an employee """
import requests
from sys import argv

if __name__ == "__main__":

    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                         format(argv[1])).json()
    nm_usr = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(argv[1])).json()

    info = []

    for algo in to_do:
        if algo.get('completed') is True:
            info.append(algo.get('title'))
    print ("Employee {} is done with tasks({}/{}):"
           .format(nm_usr.get('name'),len(info), len(to_do)))
    for otro in info:
        print('\t{}'.format(otro))
