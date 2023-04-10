#!/usr/bin/python3
"""Gather data from an API."""
import requests
from sys import argv


if len(argv) == 2:
    employee_id = argv[1]

    full_url = "https://jsonplaceholder.typicode.com/"
    employee_info = full_url + "users/{}".format(employee_id)
    todo_url = full_url + "todos?userId={}".format(employee_id)

    employee_get = requests.get(employee_info)
    todo_get = requests.get(todo_url)

    employee_data = employee_get.json()
    todo_data = todo_get.json()

    employee_name = employee_data["name"]
    num_total_tasks = len(todo_data)
    num_done_tasks = sum(task["completed"] for task in todo_data)
    completed_tasks = [task["title"]
                       for task in todo_data if task["completed"]]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_done_tasks, num_total_tasks))
    for task_title in completed_tasks:
        print("\t {}".format(task_title))
