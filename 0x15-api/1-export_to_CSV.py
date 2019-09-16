#!/usr/bin/python3
""" export to csv file """
import csv
from requests import get
from sys import argv

if __name__ == "__main__":

    to_do = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(argv[1])).json()
    usr = get('https://jsonplaceholder.typicode.com/users/{}'
              .format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), 'w') as my_csv:
        w_csv = csv.writer(my_csv, quoting=csv.QUOTE_ALL)
        for a in to_do:
            w_csv.writerow([a.get('userId'), usr.get('username'),
                    a.get('completed'), a.get('title')])
