#!/usr/bin/python3
"""Retrives data from an API.

Retrives data of employees on ToDos.
And writes them into a JSON file.
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
    # Check if employee ID is passed.
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
            usernames = {}
            for data in user_response:
                user_id = data.get('id')
                usernames[user_id] = data.get('username')
        else:
            print(f"Employee Not Found. (Invalid ID ({user_id}))")

        # Process Todos data from the API.
        if todos_response:
            data_dict = {}
            task_list = []
            for data in todos_response:
                user_id = data.get('userId')
                username = usernames.get(user_id)
                task_status = data.get('completed')
                task_title = data.get('title')

                # Create a dictinary of employee data of lists
                task_info = {
                        "task": task_title,
                        "completed": task_status,
                        "username": username
                        }
                task_list.append(task_info)
                data_dict[user_id] = task_list

            # Export data to JSON file.
            filename = "{}.json".format(user_id)
            export_to_json(filename, data_dict)
