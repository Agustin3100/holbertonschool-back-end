#!/usr/bin/python3
"""Gather data from an API and export it in JSON format."""
import json
import requests

full_url = "https://jsonplaceholder.typicode.com/"
employees_url = full_url + "users"

employees_get = requests.get(employees_url)
employees_data = employees_get.json()

all_tasks = {}

for employee in employees_data:
    employee_id = str(employee["id"])
    employee_name = employee["username"]

    todo_url = full_url + "todos?userId={}".format(employee_id)
    todo_get = requests.get(todo_url)
    todo_data = todo_get.json()

    tasks = [{"username": employee_name, "task": task["title"],
             "completed": task["completed"]} for task in todo_data]

    all_tasks[employee_id] = tasks

filename = "todo_all_employees.json"

with open(filename, "w") as f:
    json.dump(all_tasks, f)
