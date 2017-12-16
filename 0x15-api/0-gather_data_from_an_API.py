#!/usr/bin/python3
"""
fetches employee info from API
"""
import requests
from sys import argv

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com'
    userId = argv[1]
    user_link = requests.get(link + "users/{}".format(userId)).json()
    todo_link = requests.get(link + "todos?userId={}".format(userId)).json()
    name = user.get("name")
    total = len(todo_link)
    for todos in todo_link:
        count = 0
        if todo.get("completed"):
            count += 1
            title = todo.get("title")
            task = "\t {}\n".format(title)

