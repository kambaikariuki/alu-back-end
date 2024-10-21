#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns information about their TODO list progress.
It fetches user and TODO data from a placeholder API and displays the number of completed tasks.
"""

import requests
import sys

id = int(sys.argv[1])
todos_url = 'https://jsonplaceholder.typicode.com/todos/'
users_url = 'https://jsonplaceholder.typicode.com/users/'

def get_info(id):
   completed_todos = []
   todos_list = []
   completed_titles = []
   user_details = requests.get(f"{users_url}/{id}").json() 
   todos = requests.get(todos_url).json()
   for todo in todos:
      if todo["userId"] == id:
         todos_list.append(todo)
      if todo["userId"] == id and todo["completed"] == True:
         completed_todos.append(todo["title"])
   
   print(f"Employee {user_details["name"]} is done with tasks({len(completed_todos)}/{len(todos_list)}):")
   for title in completed_todos:
      print(f"  {title}")   
#    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
get_info(id)
