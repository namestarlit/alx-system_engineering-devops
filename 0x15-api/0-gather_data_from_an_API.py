#!/usr/bin/python3
"""Retrives data from an API.

Retrives progress of employees on ToDos.
"""

import requests
from sys import argv


API_BASE_URL = 'https://jsonplaceholder.typicode.com'
HEADERS = {'Accept': 'application/json'}


def get_resource(resource, params=None):
    """Make a GET request to the API."""
    url = f"{API_BASE_URL}/{resource}"
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error making GET request: {e}")
        return None


if __name__ == '__main__':
    # Check if EMPLOYEE_ID is passed.
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <EMPLOYEE_ID>")
        exit(1)

    # Get EMPLOYEE_ID from the user.
    user_id = argv[1]
    try:
        # Get User Data from the API.
        user_resource = 'users'
        user_params = {'id': user_id}
        user_response = get_resource(user_resource, user_params)

        # Get Todos data from the API.
        todos_resource = 'todos'
        todos_params = {'userId': user_id}
        todos_response = get_resource(todos_resource, todos_params)
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Process User Data from the API.
        if user_response:
            for data in user_response:
                employee_name = data.get('name')
        else:
            print(f"Employee Not Found. (Invalid ID ({user_id}))")

        # Process Todos data from the API.
        if todos_response:
            tasks_completed = []
            tasks_total = 0
            for data in todos_response:
                task = data.get('title')
                if task:
                    tasks_total += 1
                status = data.get('completed')
                if status:
                    tasks_completed.append(task)
            tasks_done = len(tasks_completed)

            # Print output to the console
            print("Employee {} is done with tasks({}/{}):".format(
                employee_name, tasks_done, tasks_total
                ))
            for task in tasks_completed:
                print("\t {}".format(task))
