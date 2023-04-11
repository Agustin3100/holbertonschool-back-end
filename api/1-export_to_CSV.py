#!/usr/bin/python3
"""Export data to CSV file type."""
import csv
import requests
from sys import argv


if len(argv) == 2:
    employee_id = int(argv[1])

    full_url = "https://jsonplaceholder.typicode.com/"
    employee_info = full_url + "users/{}".format(employee_id)
    todo_url = full_url + "todos?userId={}".format(employee_id)

    employee_get = requests.get(employee_info)
    todo_get = requests.get(todo_url)

    employee_data = employee_get.json()
    todo_data = todo_get.json()

    # Name csv after user id
    csv_name = "{}.csv".format(employee_id)

    # Open csv file and call writer function *
    with open(csv_name, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for line in todo_data:
            csv_writer.writerow(
                [employee_id, employee_data["username"],
                 line["completed"], line["title"]])
