#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={emplyee_id}'

    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Failed to fetch employee data : {employee_response.status_code}")
        return
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Failed to fetch TODO list: {todo_response.status_code}")
        return
    todo_list = todo_response.json()

    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_list)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

        if __name__ == "__main__":
            if len (sys.argv) != 2:
                print("Usage: python script.py <employee_id>")
                sys.exit(1)

                employee_id = int(sys.argv[1])
                get_employee_todo_progress(employee_id)
