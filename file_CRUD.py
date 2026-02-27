import csv

headers = ['id',"position","salary","location","required_skills"]
def load_jobs():
    with open("./jobs.csv", mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def print_info():
    print("-------------------------")
    print("1. Display positions.")
    print("2. Include positions.")
    print("3. Edit positions.")
    print("4. Delete positions.")
    print("5. Exit.")
    print("-------------------------")

def save_jobs(jobs):
    with open('./jobs.csv',mode='w',newline='',encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(jobs)

def print_job(jobs):
    for job in jobs:
        print(
            f"{job['id']}. "
            f"{job['position']}"
            f" Wage: €{float(job['salary']):.2f} "
            f"Place: {job['location']} "
            f"Competencies: {job['required_skills']}")

def create_job(jobs, id_counter):
    # print("Include position:")
    print("Insert position:")
    title = input()
    print("Insert salary:")
    amount = float(input())
    print("insert location:")
    city = input()
    print("Insert skills:")
    skills = input()
    id_counter = int(jobs[-1]['id']) + 1 if len(jobs) > 0 else 1
    job = {
        'id': id_counter,
        "position": title,
        "salary": amount,
        "location": city,
        "required_skills": skills
    }
    jobs.append(job)
    save_jobs(jobs)
    return id_counter

def edit_job(jobs):
    print("Edit position")
    print('Insert position ID you want to edit')
    edit_id = input()
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
    save_jobs(jobs)

def delete_job(jobs):
    print("Delete position:")
    print('insert position ID you want to delete')
    del_id = input()
    for job in jobs:
        if job['id'] == del_id:
            jobs.remove(job)
            print("Position successfully deleted")
            break
    save_jobs(jobs)
