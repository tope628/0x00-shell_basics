#!/usr/bin/python3
"""
fetches employee info from API in csv
"""
import requests
from sys import argv

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user_link = requests.get(link + "users/{}".format(
        userId), verify=False).json()
    todo_link = requests.get(link + "todos?userId={}".format(
        userId), verify=False).json()
    filename = "{}.csv".format(userId)
    with open(filename, 'w') as f:
        for todo in todo_link:
            complete = todo.get("completed")
            title = todo.get("title")
            f.write('"{}","{}","{}","{}"\n'.format
                    (userId, user_link.get("username"), complete, title))
