#!/usr/bin/python3
"""
fetches employee info from API
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
    name = user_link.get("name")
    total = len(todo_link)
    tasks = []
    for todos in todo_link:
        if todos.get("completed"):
            title = todos.get("title")
            tasks.append(todos)
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(tasks), total))
    for task in tasks:
        print("\t {}".format(task.get("title")))
