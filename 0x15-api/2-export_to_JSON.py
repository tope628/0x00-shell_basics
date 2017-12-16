#!/usr/bin/python3
"""
fetches employee info from API in csv
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user_link = requests.get(link + "users/{}".format(
        userId), verify=False).json()
    todo_link = requests.get(link + "todos?userId={}".format(
        userId), verify=False).json()
    user_list = []
    for todo in todo_link:
        task_dict = {}
        task_dict["complete"] = todo.get("completed")
        task_dict["task"] = todo.get("title")
        task_dict["username"] = user_link.get("username")
        user_list.append(task_dict)
    user_dict = {}
    user_dict["{}".format(userId)] = user_list
    filename = "{}.json".format(userId)
    with open(filename, "w") as f:
        json.dump(user_dict, f)
