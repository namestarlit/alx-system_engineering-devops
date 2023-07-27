#!/usr/bin/python3
"""Retrives data from an API.

Retrives data of employees on ToDos.
And writes them into a csv file.
"""

import csv
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


def export_to_csv(filename, employee_data):
    """Exports Employee data into csv file

    Args:
        filename (str): The name of the CSV file to export the data.
        employee_data (list): a list of employee's data

    Raises:
        TypeError: If 'filename' is not a string or 'employee_data'
        is not a list.
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a stringr")

    if not isinstance(employee_data, list):
        raise TypeError("employee_data must be a list")

    # Check if employee data is a list of lists
    if not all(isinstance(row, list) for row in employee_data):
        raise TypeError("employee_data must be a list of lists")

    try:
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerows(employee_data)
    except csv.Error as e:
        print(f"Error: There was an issue with the CSV data: {e}")


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
            data_lists = []
            for data in todos_response:
                user_id = data.get('userId')
                username = usernames.get(user_id)
                task_status = data.get('completed')
                task_title = data.get('title')

                # Create a data list and append to data lists
                data = [user_id, username, task_status, task_title]
                data_lists.append(data)

            # Export data to CSV file.
            filename = "{}.csv".format(user_id)
            export_to_csv(filename, data_lists)
