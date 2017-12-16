#!/usr/bin/python3
"""
fetches employee info from API in csv
"""
import json
import requests

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/'
    user_link = requests.get(link + "users/", verify=False).json()
    todo_link = requests.get(link + "todos/", verify=False).json()
    user_dict = {}
    uname_dict = {}
    for user in user_link:
        userId = user.get("id")
        user_dict[userId] = []
        uname_dict[userId] = user.get("username")
    for todo in todo_link:
        task_dict = {}
        task_dict["complete"] = todo.get("completed")
        task_dict["task"] = todo.get("title")
        userId = todo.get("userId")
        task_dict["username"] = uname_dict.get(userId)
        user_dict.get(userId).append(task_dict)
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(user_dict, f)
