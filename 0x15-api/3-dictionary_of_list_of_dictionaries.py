#!/usr/bin/python3
"""Retrives data from an API.

Retrives progress of employees on ToDos.
And exports the data into a JSON file.
"""

import json
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


def export_to_json(filename, employee_data):
    """Exports employee data to JSON file.

    Args:
        filename (str): The name of the file to export employee data to.
        employee_data (dict): A dictionary of employee data.
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    if not isinstance(employee_data, dict):
        raise TypeError("employee_data must be a dictionary.")
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(employee_data, json_file)
    except TypeError as e:
        message = f"Error: 'employee_data' is not serializable to JSON: {e}"
        raise TypeError(message)
    except UnicodeEncodeError as e:
        message = (
                f"Error: There was a problem with enconding"
                f"the data to UTF-8: {e}"
                )
        raise UnicodeEncodeError(message)


if __name__ == '__main__':
    # Get EMPLOYEE_ID from the user.
    try:
        # Get User Data from the API.
        user_resource = 'users'
        user_response = get_resource(user_resource)

        # Get Todos data from the API.
        todos_resource = 'todos'
        todos_response = get_resource(todos_resource)
    except Exception as e:
        print(f"Error: {e}")
    else:
        # Process User Data from the API.
        if user_response:
            usernames = {}
            for data in user_response:
                id = data.get('id')
                usernames[id] = data.get('username')
        else:
            print(f"Employee Not Found. (Invalid ID ({user_id}))")

        # Process Todos data from the API.
        if todos_response:
            employee_dict = {}
            for data in todos_response:
                user_id = data.get('userId')
                username = usernames[user_id]
                task_title = data.get('title')
                task_status = data.get('completed')

                # Create employees dictionary of lists
                task_info = {
                        'username': username,
                        'task': task_title,
                        'completed': task_status
                        }
                if user_id in employee_dict:
                    employee_dict[user_id].append(task_info)
                else:
                    employee_dict[user_id] = [task_info]

            # Export employee data to JSON file.
            filename = 'todo_all_employees.json'
            export_to_json(filename, employee_dict)
