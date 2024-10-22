#!/usr/bin/python3

''' Python script that, for a given employee ID, returns information about their TODO list progress.
It fetches user and TODO data from a placeholder API and displays the number of completed tasks.
'''


import requests
import sys

# Get employee ID from command line arguments and convert it to an integer
id = int(sys.argv[1])

# Define URLs for fetching TODOs and user data
todos_url = 'https://jsonplaceholder.typicode.com/todos/'
users_url = 'https://jsonplaceholder.typicode.com/users/'

def get_info(employee_id):
    """
    Fetches and displays the TODO list progress for the specified employee.

    Parameters:
    employee_id (int): The ID of the employee whose TODO list will be retrieved.

    This function retrieves user details and their associated TODOs from the JSONPlaceholder API,
    counts the completed tasks, and prints the results in a formatted manner.

    Example:
    >>> get_info(1)
    Employee John Doe is done with tasks(3/5):
      Task 1
      Task 2
    """
    completed_todos = []  # List to store titles of completed TODOs
    todos_list = []       # List to store all TODOs for the employee

    # Fetch user details based on the employee ID
    user_details = requests.get(f"{users_url}/{employee_id}").json()

    # Fetch all TODOs
    todos = requests.get(todos_url).json()

    # Iterate through all TODOs to filter by employee ID
    for todo in todos:
        if todo["userId"] == employee_id:
            todos_list.append(todo)  # Append the TODO to the list for this employee
            if todo["completed"]:
                completed_todos.append(todo["title"])  # Append the title if completed

    # Print the employee's name and their TODO completion statistics
    print(f"Employee {user_details['name']} is done with tasks({len(completed_todos)}/{len(todos_list)}):")
    for title in completed_todos:
        print(f"  {title}")  # Print each completed task title

# Call the function with the provided employee ID
if __name__ == "__main__":
   get_info(id)
