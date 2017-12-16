#!/usr/bin/python3
"""
fetches employee info from API in csv
"""
import requests
from sys import argv

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com'
    userId = argv[1]
    user_link = requests.get(link + "users/{}".format(userId)).json()
    todo_link = requests.get(link + "todos?userId={}".format(userId)).json()
    for user in user_link:
        username = user["username"]
    for todo in todo_link:
        filename = "{}.csv".format(userId)
        complete = todo.get("completed")
        title = todo.get("title")
        with open(filename, 'w') as f:
            f.write('"{}","{}","{}","{}"\n'.format
                         (userId, username, complete, title))
