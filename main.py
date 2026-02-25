jobs = [
    {'id':1,
    "position":"Data Analyst",
     "salary": 1800,
     "location":'Vilnius',
     "required_skills":"Python, SQL, Power BI, Excel"},
    {'id':2,
    "position":"Business Analyst",
     "salary": 2000,
     "location":'Kaunas',
     "required_skills":"Power BI, SQL, Jira"},
    {'id':3,
    "position":"Financial Analyst",
     "salary": 2500,
     "location":'Utena',
     "required_skills":"Audit, Excel, Vlookup, PivotTables"},
    {'id':4,
    "position": "Project Manager",
    "salary": 2800,
    "location": "Hybrid",
    "required_skills": "Excel"},
]
id_counter = 4

while True:
    print("-------------------------")
    print("1. Display positions.")
    print("2. Include positions.")
    print("3. Edit positions.")
    print("4. Delete positions.")
    print("5. Exit.")
    print("-------------------------")

    choise = input()
    match choise:
        case '1':
            print("Show positions")
            for job in jobs:
                print(
                    f"{job['id']}. {job['position']} Wage: €{job['salary']:.2f} Place: {job['location']} Competencies:"
                    f" {job['required_skills']}")
        case '2':
            print("Include position:")
            print("Insert position:")
            title = input()
            print("Insert salary:")
            amount = float(input())
            print("insert location:")
            city = input()
            print("Insert skills:")
            skills = input()
            id_counter += 1
            job = {
                'id': id_counter,
                "position": title,
                "salary": amount,
                "location": city,
                "required_skills": skills
            }
            jobs.append(job)
        case '3':
            print("Edit position")
            print('Insert position ID you want to edit')
            edit_id = int(input())
            for job in jobs:
                if job['id'] == edit_id:
                    print("Insert position:")
                    job['position'] = input()
                    print("Insert salary:")
                    job['salary'] = float(input())
                    print("Insert location:")
                    job['location'] = input()
                    print("Insert skills:")
                    job['required_skills'] = input()
        case '4':
            print("Delete position:")
            print('insert position ID you want to delete')
            del_id = int(input())
            for job in jobs:
                if job['id'] == del_id:
                    jobs.remove(job)
                    print("Position successfully deleted")
                    break
        case '5':
            print("Exit")
            break
        case _:
            print("Invalid selection, please try again :).")