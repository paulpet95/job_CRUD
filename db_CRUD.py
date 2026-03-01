import pymysql

DB_C0NFIG = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Spravadlyva1234%',
    'database' : 'company'
}

headers = ['id',"position","salary","location","required_skills"]

def get_conn():
    return pymysql.connect(**DB_C0NFIG)

def load_jobs():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    jobs = []
    for row in rows:
        single_job = {}
        for col_num in range(len(headers)):
            single_job[headers[col_num]] = row[col_num]
        jobs.append(single_job)
    return jobs

def print_info():
    print("-------------------------")
    print("1. Display positions.")
    print("2. Include positions.")
    print("3. Edit positions.")
    print("4. Delete positions.")
    print("5. Exit.")
    print("-------------------------")

def print_job(jobs):
    jobs = load_jobs()
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
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO `company`.`jobs`(`position`,`salary`,`location`,`required_skills`) VALUES (%s,%s,%s,%s);", (title,amount,city,skills))
    conn.commit()
    cur.close()
    conn.close()

def edit_job(jobs):
    print("Edit position")
    print('Insert position ID you want to edit')
    edit_id = input()
    print("Edit position:")
    title = input()
    print("Edit salary:")
    amount = float(input())
    print("Edit location:")
    city = input()
    print("Edit skills:")
    skills = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE `company`.`jobs`SET `position` = %s, " "`salary` = %s, `location` = %s," " `required_skills` = %s" " WHERE `id` = %s;",(title, amount, city, skills,edit_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_job(jobs):
    print("Delete position:")
    print('Insert position ID you want to delete:')
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs where id = %s", (del_id,))
    row = cur.fetchone()
    if row:
        print(
            f"{row[0]}. "
            f"{row[1]}"
            f" Wage: €{float(row[2]):.2f} "
            f"Place: {row[3]} "
            f"Competencies: {row[4]}")
        cur.execute("delete from jobs where id = %s", (del_id,))
        conn.commit()
    else:
        print('No record has been found')
    cur.close()
    conn.close()
