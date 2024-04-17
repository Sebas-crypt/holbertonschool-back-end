#!/usr/bin/python3
""" Gather data from an API and export it to a JSON file """

import json
import requests

def fetch_all_tasks():
    """ Fetches all tasks for all employees and exports to JSON """
    base_url = 'https://jsonplaceholder.typicode.com'

    user_response = requests.get(f"{base_url}/users")
    user_data = user_response.json()

    all_tasks = {}

    for user in user_data:
        user_id = user['id']
        username = user['username']

        todo_response = requests.get(f"{base_url}/todos", params={'userId': user_id})
        todo_data = todo_response.json()

        user_tasks = [{
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        } for task in todo_data]

        all_tasks[str(user_id)] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)

    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    fetch_all_tasks()
