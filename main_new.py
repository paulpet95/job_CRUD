from data1 import load_jobs
from list_CRUD1 import *

jobs = load_jobs()
id_counter = 4

while True:
    print_info()
    choice = input()
    match choice:
        case '1':
          print_job(jobs)
        case '2':
            id_counter = create_job(jobs,id_counter)
        case '3':
            edit_job(jobs)
        case '4':
            delete_job(jobs)
        case '5':
            print("Exit")
            break
        case _:
            print("Invalid selection, please try again :).")