from data1 import load_data

def print_info():
    print("-------------------------")
    print("1. Display positions.")
    print("2. Include positions.")
    print("3. Edit positions.")
    print("4. Delete positions.")
    print("5. Exit.")
    print("-------------------------")

def load_jobs():
    return load_data()

def print_job(jobs):
    for job in jobs:
        print(
            f"{job['id']}. "
            f"{job['position']}"
            f" Wage: €{job['salary']:.2f} "
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
        id_counter += 1
        job = {
            'id': id_counter,
            "position": title,
            "salary": amount,
            "location": city,
            "required_skills": skills
        }
        jobs.append(job)
        return id_counter

def edit_job(jobs):
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

def delete_job(jobs):
                print("Delete position:")
                print('insert position ID you want to delete')
                del_id = int(input())
                for job in jobs:
                    if job['id'] == del_id:
                        jobs.remove(job)
                        print("Position successfully deleted")
                        break

